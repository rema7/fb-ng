<template>
    <v-container fluid fill-height>
        <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4>
                <v-card class="elevation-12">
                    <v-toolbar dark color="primary">
                        <v-toolbar-title>Registration</v-toolbar-title>
                    </v-toolbar>
                    <v-card-text>
                        <v-form
                            v-model="valid"
                            :lazy-validation="false"
                        >
                            <v-text-field
                                v-model="email"
                                :rules="emailRules"
                                type="email"
                                label="Email"
                                required
                            />
                            <v-text-field
                                v-model="password"
                                :rules="requiredRules"
                                label="Password"
                                type="password"
                                required
                            />
                            <v-text-field
                                v-model="name"
                                label="Name"
                                :rules="requiredRules"
                                required
                            />
                            <v-text-field
                                v-model="lastName"
                                label="Last Name"
                                :rules="requiredRules"
                                required
                            />
                            <v-select
                                v-model="selectedSex"
                                label="Sex"
                                :items="sex"
                                :rules="requiredRules"
                                required
                            />
                            <v-text-field
                                v-model="age"
                                label="Age"
                                type="number"
                                :rules="requiredRules"
                                required
                            />
                            <v-text-field
                                v-model="country"
                                label="Country"
                                :rules="requiredRules"
                                required
                            />
                        </v-form>
                    </v-card-text>
                    <v-card-actions
                        class="justify-space-between"
                    >
                        <v-btn
                            text
                            small
                            color="primary"
                            to="login"
                        >Login</v-btn>
                        <v-btn
                            :disabled="!valid"
                            color="primary"
                            text
                            @click="onRegister"
                        >Register</v-btn>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'
const auth = createNamespacedHelpers('auth')
const account = createNamespacedHelpers('account')

export default {
    name: 'RegisterView',
    data: () => ({
        valid: false,
        email: null,
        password: null,
        name: null,
        lastName: null,
        country: null,
        selectedSex: null,
        sex: ['male', 'female', 'other'],
        age: 0,
        emailRules: [
            (v) => !!v || 'E-mail is required',
            (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid',
        ],
        requiredRules: [
            (v) => !!v || 'Required',
        ],
    }),
    computed: {
        ...auth.mapGetters(['error']),
    },
    methods: {
        ...auth.mapActions(['register']),
        ...account.mapActions(['fetch']),
        async onRegister () {
            const { valid, email, password, name, lastName, selectedSex, age, country } = this
            valid && await this.register({
                email,
                password,
                name,
                lastName,
                sex: selectedSex,
                age: +age,
                country,
            })
            if (!this.error) {
                await this.fetch()
                await this.$router.push(this.$route.query.redirect || '/')
            }
        },
    },
}
</script>
