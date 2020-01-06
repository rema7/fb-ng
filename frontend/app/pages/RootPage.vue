<template>
    <v-flex>
        <sidebar :logout="onLogout"/>
        <v-content>
            <router-view />
        </v-content>
    </v-flex>
</template>

<script>
import Sidebar from 'components/Sidebar'
import { createNamespacedHelpers } from 'vuex'
const auth = createNamespacedHelpers('auth')

export default {
    name: 'RootPage',
    components: { Sidebar },
    methods: {
        ...auth.mapActions(['logout']),
        async onLogout () {
            await this.logout()
            this.$router.push('/login')
        },
    },
}
</script>
