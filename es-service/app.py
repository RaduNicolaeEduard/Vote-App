from flask import Flask, g, jsonify, request
from elasticsearch import Elasticsearch
from flask_oidc import OpenIDConnect
import requests
from flask_cors import CORS, cross_origin
from pprint import pprint
from util.helpers import upload_file_to_s3, allowed_file
from datetime import date
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
cors = CORS(app)
import os
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.update({
    'SECRET_KEY': os.environ.get("SECRET_KEY"),
    'DEBUG': os.environ.get("DEBUG"),
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_OPENID_REALM': 'Backend',
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post',
    'OIDC_TOKEN_TYPE_HINT': 'access_token',
    'OIDC-SCOPES': ['openid']
})
oidc = OpenIDConnect(app)


def connect_to_elastic():
    es = Elasticsearch("http://localhost:9200",
                       basic_auth=("elastic", "changeme"))
    return es


es = connect_to_elastic()


@app.route("/add/election", methods=["POST"])
@cross_origin()
@oidc.accept_token(require_token=True, scopes_required=['openid'])
def add_election():
    # Print user info
    # pprint(request.form)
    # pprint(request.form['name'])
    # print file
    pprint(request.files['file'])
    # pprint(g.oidc_token_info)
    file = request.files['file']
    if file and allowed_file(file.filename):
        output = upload_file_to_s3(file)
        print(output)
    print(file)
    election = {
        "name": request.form['name'],
        "description": request.form['description'],
        "start_date": "2020-01-01",
        "end_date": "2020-01-01",
        "created_by": g.oidc_token_info['sub'],
        "created_date": date.today(),
        "type": request.form['type'],
        "file": f"https://s3.eu-west-1.amazonaws.com/{os.environ.get('AWS_BUCKET_NAME')}/{output}"
    }
    res = es.index(index="elections", body=election)
    # pprint(res)
    return "200"


@app.route("/elections", methods=["POST", "GET"])
@cross_origin()
def elections():
    if request.form and request.form['type'] == "search":
        # match phrase query
        res = es.search(index="elections", body={"query": {
                        "match_phrase": {"name": request.form['search']}}})
        response = {
            "data": res["hits"]["hits"],
        }
        return response

    if request.form and request.form['type'] == "closing_soon":
        res = es.search(index="elections", body={"query": {
                        "range": {"end_date": {"gte": "now-1d/d", "lte": "now"}}}}, scroll="2m")
        scroll_id = res["_scroll_id"]
        response = {
            "data": res["hits"]["hits"],
            "scroll_id": scroll_id
        }
        return response



    res = es.search(index="elections", body={
                    "query": {"match_all": {}}}, scroll="2m")
    scroll_id = res["_scroll_id"]
    response = {
        "data": res["hits"]["hits"],
        "scroll_id": scroll_id
    }
    return response


@app.route("/elections/scroll", methods=["POST"])
@cross_origin()
def elections_scroll():
    scroll_id = request.form['scroll_id']
    res = es.scroll(scroll_id=scroll_id, scroll="2m")
    scroll_id = res["_scroll_id"]
    response = {
        "data": res["hits"]["hits"],
        "scroll_id": scroll_id
    }
    return response



if __name__ == "__main__":
    app.run()
