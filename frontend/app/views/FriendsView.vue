<template>
    <base-view>
        <template #title>
            Friends
        </template>
        <v-flex>
            <v-sheet class="pa-2">
                <v-text-field v-model="search" label="Search"/>
                <v-combobox
                    v-model="ageCmp"
                    :items="allCmp"
                    label="Age comparator"
                />
                <v-text-field v-model="age" label="Search"/>
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
                    v-for="account in accounts"
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
import debounce from 'lodash/debounce'
const account = createNamespacedHelpers('account')
const accounts = createNamespacedHelpers('accounts')

export default {
    name: 'FriendsView',
    components: { FriendCard, BaseView },
    data: () => ({
        search: '',
        ageCmp: 'eq',
        allCmp: ['lt', 'lte', 'eq', 'gt', 'gte'],
        age: null,
    }),
    computed: {
        ...account.mapGetters(['account']),
        ...accounts.mapGetters(['accounts', 'isLoading']),
    },
    methods: {
        ...accounts.mapActions(['fetch']),
        update () {
            const { age, ageCmp, search } = this
            this.fetch({
                search,
                age,
                ageCmp,
            })
        },
        debounceUpdate: debounce(function () {
            this.update()
        }, 500),
    },
    mounted () {
        this.update()
    },
    watch: {
        search () {
            this.debounceUpdate()
        },
        age () {
            this.debounceUpdate()
        },
        ageCmp () {
            this.debounceUpdate()
        },
    },
}
</script>
