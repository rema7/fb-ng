<template>
    <v-navigation-drawer
        stateless
        width="300px"
        disable-resize-watcher
        permanent
        fixed
        app
    >
        <v-list-item>
            <v-list-item-content>
                <v-list-item-title class="title">
                    Facebook
                </v-list-item-title>
                <v-list-item-subtitle>
                    Next Generation
                </v-list-item-subtitle>
            </v-list-item-content>
        </v-list-item>
        <v-divider></v-divider>
        <v-list>
            <v-list-item :to="{path: '/friends'}">
                <v-list-item-icon>
                    <v-icon>contacts</v-icon>
                </v-list-item-icon>
                <v-list-item-title>Friends</v-list-item-title>
            </v-list-item>
        </v-list>
        <template #append>
            <div class="pa-2" @click="logout">
                <v-btn block text>
                    <v-icon>exit_to_app</v-icon>&nbsp;Logout
                </v-btn>
            </div>
        </template>
    </v-navigation-drawer>
</template>

<script>
export default {
    name: 'Sidebar',
    props: {
        logout: {
            type: Function,
            default: () => {},
        },
    },
}
</script>

