<template>
    <v-app v-if="!isLoading">
        <router-view />
    </v-app>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'
const settings = createNamespacedHelpers('settings')

export default {
    computed: {
        ...settings.mapGetters(['isLoading']),
    },
    watch: {
    },
    methods: {
    },
    components: {
    },
}
</script>
