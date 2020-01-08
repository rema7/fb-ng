import { HOBBIES_REQUEST, HOBBIES_ERROR, HOBBIES_SUCCESS } from 'store/actions/Hobbies'
import { get } from 'helpers/requests'

const state = {
    loading: false,
    hobbies: [],
}

const getters = {
    hobbies: (state) => state.hobbies,
}

const actions = {
    async fetch ({ state, commit, rootState }) {
        if (state.loading) {
            return
        }

        commit(HOBBIES_REQUEST)
        const result = await get(rootState.settings.urls.hobbies)
        if (result) {
            commit(HOBBIES_SUCCESS, result)
        } else {
            commit(HOBBIES_ERROR)
        }
    },
}

const mutations = {
    [HOBBIES_REQUEST]: (state) => {
        state.loading = true
        state.error = null
    },
    [HOBBIES_SUCCESS]: (state, { data }) => {
        state.loading = false
        state.hobbies = data
    },
    [HOBBIES_ERROR]: (state) => {
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
