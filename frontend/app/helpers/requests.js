import axios from 'axios'
import humps from 'humps'
import { getToken } from './storage'


const commonHeaders = Object.assign({}, {
    Accept: 'application/json',
})

const getWrapper = async (url, headers, params, cancelToken) => {
    return axios.get(url, {
        headers,
        params: humps.decamelizeKeys(params),
        cancelToken,
    }).then((result) => {
        return {
            ...result,
            data: humps.camelizeKeys(result.data),
        }
    })
}

export const get = async (url, params, cancelToken) => {
    return getWrapper(url, commonHeaders, params, cancelToken)
}

export const getSecured = async (url, params, cancelToken) => {
    const headers = {
        ...commonHeaders,
        Authorization: getToken(),
    }
    return getWrapper(url, headers, params, cancelToken)
}

const postWrapper = async (url, data, headers, cancelToken) => {
    return axios.post(
        url,
        humps.decamelizeKeys(data),
        {
            headers,
            cancelToken,
        },
    ).then((result) => {
        return {
            ...result,
            data: humps.camelizeKeys(result.data),
        }
    })
}

export const post = async (url, data, headers, options, cancelToken) => {
    const _headers = {
        ...commonHeaders,
        ...headers,
    }
    return postWrapper(url, data, _headers, cancelToken)
}

export const postSecured = async (url, data, cancelToken) => {
    const headers = {
        ...commonHeaders,
        Authorization: getToken(),
    }
    return postWrapper(url, data, headers, cancelToken)
}


const putWrapper = async (url, data, options, cancelToken) => {
    return axios.put(
        url,
        humps.decamelizeKeys(data),
        {
            ...options,
            cancelToken,
        },
    ).then((result) => {
        return {
            ...result,
            data: humps.camelizeKeys(result.data),
        }
    })
}

export const put = async (url, data, options, cancelToken) => {
    const newOptions = {
        headers: {
            ...commonHeaders,
        },
        ...options,
    }
    return putWrapper(url, data, newOptions, cancelToken)
}

export const putSecured = async (url, data, cancelToken) => {
    const headers = {
        ...commonHeaders,
        Authorization: getToken(),
    }
    return putWrapper(url, data, headers, cancelToken)
}

const deleteWrapper = async (url, headers, params) => {
    return axios.delete(
        url,
        {
            headers,
            params: humps.decamelizeKeys(params),
        },
    ).then((result) => {
        return {
            ...result,
            data: humps.camelizeKeys(result.data),
        }
    })
}

export const deleteSecured = async (url, params) => {
    const headers = {
        ...commonHeaders,
        Authorization: getToken(),
    }
    return deleteWrapper(url, headers, params)
}

export const getCancelSource = () => {
    return axios.CancelToken.source()
}
