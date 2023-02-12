import Vue from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import authentication from "./plugins/keycloak";
import axios from 'axios';
import VueI18n from 'vue-i18n'
Vue.config.productionTip = false
Vue.use(authentication)
Vue.prototype.$http = axios;

// new Vue({
//   router,
//   store,
//   vuetify,
//   render: h => h(App)
// }).$mount('#app')
// import plugin
import { TiptapVuetifyPlugin } from 'tiptap-vuetify'
// don't forget to import CSS styles
import 'tiptap-vuetify/dist/main.css'
// Vuetify's CSS styles 
import 'vuetify/dist/vuetify.min.css'

Vue.$keycloak
  .init({ checkLoginIframe: false, onLoad: 'check-sso' })
  .then(() => {
    new Vue({
      router,
      store,
      vuetify,
      render: h => h(App)
    }).$mount('#app')
  })
Vue.use(VueI18n)
Vue.use(TiptapVuetifyPlugin, {
  // the next line is important! You need to provide the Vuetify Object to this place.
  vuetify, // same as "vuetify: vuetify"
  // optional, default to 'md' (default vuetify icons before v2.0.0)
  iconsGroup: 'md'
})

function refreshToken () {
  return new Promise((resolve, reject) => {
    Vue.prototype.$keycloak
      .updateToken(5)
      .then(() => {
        resolve()
      })
      .catch(() => {
        Vue.prototype.$keycloak.login()
        reject()
      })
  })
}

// set interval to refresh token
setInterval(() => {
  if (Vue.prototype.$keycloak.authenticated) {
    refreshToken()
  }
}, 1)

axios.interceptors.request.use(
  async config => {
    if (Vue.prototype.$keycloak.authenticated) {
      await refreshToken()
      config.headers.Authorization = `Bearer ${Vue.prototype.$keycloak.token}`
    }
    return config
  },
  error => {
    Promise.reject(error)
  }
)
