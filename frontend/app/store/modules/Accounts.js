import { ACCOUNTS_ERROR, ACCOUNTS_REQUEST, ACCOUNTS_SUCCESS } from 'store/actions/Accounts'
import { getSecured } from 'helpers/requests'

const state = {
    loading: false,
    loaded: false,
    accounts: [],
}

const getters = {
    accounts: (state) => state.accounts,
}

const actions = {
    fetch: async ({ state, commit, rootState }, params) => {
        if (state.loading) {
            return
        }
        commit(ACCOUNTS_REQUEST)
        try {
            const result = await getSecured(rootState.settings.urls.accounts, {
                query: params && params.query,
            })
            commit(ACCOUNTS_SUCCESS, result)
        } catch (e) {
            commit(ACCOUNTS_ERROR)
        }
    },
}

const mutations = {
    [ACCOUNTS_REQUEST]: (state) => {
        state.loading = true
        state.loaded = false
        state.accounts = []
    },
    [ACCOUNTS_SUCCESS]: (state, { data }) => {
        state.loading = false
        state.accounts = data
        state.loaded = true
    },
    [ACCOUNTS_ERROR]: (state) => {
        state.loading = false
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}
