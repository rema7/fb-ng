import Vue from 'vue'
import VueRouter from 'vue-router'

import store from 'store'
import RootPage from 'pages/RootPage'
import LoginView from 'views/LoginView'
import RegisterView from 'views/RegisterView'


Vue.use(VueRouter)

const routes = [
    {
        path: '',
        component: RootPage,
        meta: {
            requiresAuth: true,
        },
    },
    {
        path: '/login',
        component: LoginView,
    },
    {
        path: '/register',
        component: RegisterView,
    },
    { path: '*', redirect: '/' },
]


const router = new VueRouter({
    routes,
    mode: 'history',
})

router.beforeEach((to, from, next) => {
    const account = store.getters['account/account']
    if (to.matched.some((record) => record.meta.requiresAuth)) {
        if (!account) {
            next({
                path: '/login',
                query: { redirect: to.fullPath },
            })
        } else {
            next()
        }
    } else {
        next()
    }
})

export default router
