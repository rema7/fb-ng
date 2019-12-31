import axios from 'axios'
import Vue from 'vue'
import Vuetify from 'vuetify'

import store from './store/index'
import router from './router'

import App from './App.vue'

import { getToken, removeToken } from 'helpers/storage'

import '@mdi/font/css/materialdesignicons.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'
import 'vuetify/dist/vuetify.min.css'
import 'filters'

axios.interceptors.response.use((response) => {
    return response
}, (error) => {
    if (error.response && error.response.status === 401) {
        removeToken()
        store.dispatch('auth/logout')
    }
    throw error
})

axios.defaults.validateStatus = (status) => {
    return status >= 200 && status < 300
}

const opts = {
    icons: {
        iconfont: 'md',
    },
}
Vue.use(Vuetify)

const initVue = () => {
    /* eslint-disable-next-line no-new */
    new Vue({
        vuetify: new Vuetify(opts),
        el: '#app',
        i18n,
        store,
        router,
        render: (h) => h(App),
    })
}
store.dispatch('settings/fetch').then(async () => {
    if (getToken()) {
        await store.dispatch('account/fetch')
    }
    initVue()
})
