import os
import uuid
from dotenv import load_dotenv
load_dotenv()
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
import boto3

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY")
)
# function to check file extension
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
        
def upload_file_to_s3(file, acl="public-read"):
    filename = f'{uuid.uuid4()}.{file.filename.rsplit(".", 1)[1].lower()}'
    try:
        s3.upload_fileobj(
            file,
            os.environ.get("AWS_BUCKET_NAME"),
            filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e
    

    # after upload file to s3 bucket, return filename of the uploaded file
    return filename