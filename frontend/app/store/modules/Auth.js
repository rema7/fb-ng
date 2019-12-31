import {
    AUTH_REQUEST,
    AUTH_ERROR,
    AUTH_SUCCESS,
    AUTH_LOGOUT,
} from 'store/actions/Auth'
import { setToken, removeToken } from 'helpers/storage'
import { post } from 'helpers/requests'

const state = {
    loading: false,
    error: null,
    token: null,
}

const getters = {
    error: (state) => state.error,
}

const actions = {
    async login ({ state, commit, rootState }, user) {
        if (state.loading) {
            return
        }

        commit(AUTH_REQUEST)
        try {
            const result = await post(
                rootState.settings.urls.login,
                user,
            )
            commit(AUTH_SUCCESS, result)
            return result
        } catch (e) {
            commit(AUTH_ERROR, e)
        }
    },
    async logout ({ state, commit }) {
        commit(AUTH_LOGOUT)
    },
}

const mutations = {
    [AUTH_REQUEST]: (state) => {
        state.loading = true
        state.error = null
    },
    [AUTH_SUCCESS]: (state, { data }) => {
        state.loading = false
        state.token = data.token
        setToken(data.token)
        state.error = null
    },
    [AUTH_ERROR]: (state, error) => {
        state.loading = false
        state.error = error.message
    },
    [AUTH_LOGOUT]: (state) => {
        state.loading = false
        state.token = null
        removeToken()
    },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations,
}
