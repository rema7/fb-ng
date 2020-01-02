import { SETTINGS_REQUEST, SETTINGS_ERROR, SETTINGS_SUCCESS } from 'store/actions/Settings'
import { get } from 'helpers/requests'

const state = {
    loading: false,
    urls: {
        settings: '/api/settings',
    },
    error: null,
}

const getters = {
    urls: (state) => state.urls,
}

const actions = {
    async fetch ({ state, commit }) {
        if (state.loading) {
            return
        }

        commit(SETTINGS_REQUEST)
        const result = await get(state.urls.settings)
        if (result) {
            commit(SETTINGS_SUCCESS, result)
        } else {
            commit(SETTINGS_ERROR)
        }
    },
}

const mutations = {
    [SETTINGS_REQUEST]: (state) => {
        state.loading = true
        state.error = null
    },
    [SETTINGS_SUCCESS]: (state, { data }) => {
        state.loading = false
        state.urls = data.urls
        state.limit = data.limit
    },
    [SETTINGS_ERROR]: (state) => {
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
