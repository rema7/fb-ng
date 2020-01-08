import Vue from 'vue'
import Vuex from 'vuex'


import account from 'store/modules/Account'
import accounts from 'store/modules/Accounts'
import auth from 'store/modules/Auth'

import hobbies from 'store/modules/Hobbies'
import settings from 'store/modules/Settings'


Vue.use(Vuex)

const actions = {

}

const state = {
}

const mutations = {
}

const getters = {

}

const modules = {
    account,
    accounts,
    auth,
    hobbies,
    settings,
}

export default new Vuex.Store({
    state,
    mutations,
    getters,
    modules,
    actions,
})
