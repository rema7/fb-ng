<template>
    <base-view>
        <template #title>
            Friends
        </template>
        <v-flex>
            <v-sheet class="pa-2">
                <v-text-field v-model="search" label="Search"/>
            </v-sheet>
        </v-flex>
        <v-container
            v-if="!isLoading"
            fluid
            grid-list-md
            pa-2
            ma-0
            row
            fill-height
        >
            <v-layout
                wrap
            >
                <v-flex
                    v-for="account in filtered"
                    :key="account.uuid"
                    tile
                    xs6 sm4 md4 lg3 xl3
                >
                    <friend-card
                        :friend="account"
                    />
                </v-flex>
            </v-layout>
        </v-container>
    </base-view>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'
import BaseView from 'views/base/BaseView'
import FriendCard from 'components/FriendCard'
const account = createNamespacedHelpers('account')
const accounts = createNamespacedHelpers('accounts')

export default {
    name: 'FriendsView',
    components: { FriendCard, BaseView },
    data: () => ({
        search: '',
    }),
    computed: {
        ...account.mapGetters(['account']),
        ...accounts.mapGetters(['accounts', 'isLoading']),
        filtered () {
            return this.accounts.filter((account) => {
                return account.name.includes(this.search) ||
                    account.lastName.includes(this.search) ||
                    account.email.includes(this.search)
            })
        },
    },
    methods: {
        ...accounts.mapActions(['fetch']),
    },
    mounted () {
        this.fetch()
    },
}
</script>
