<template>
    <v-container fluid fill-height>
        <v-layout align-center justify-center>
            <v-flex xs12 sm8 md4>
                <v-card class="elevation-12">
                    <v-toolbar dark color="primary">
                        <v-toolbar-title>Login</v-toolbar-title>
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
                                :rules="passwordRules"
                                label="Password"
                                type="password"
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
                            to="register"
                        >Registration</v-btn>
                        <v-btn
                            :disabled="!valid"
                            color="primary"
                            @click="onLogin"
                        >Login</v-btn>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import { createNamespacedHelpers } from 'vuex'
const { mapActions } = createNamespacedHelpers('auth')

export default {
    name: 'LoginView',
    data: () => ({
        valid: false,
        email: null,
        password: null,
        emailRules: [
            (v) => !!v || 'E-mail is required',
            (v) => /.+@.+\..+/.test(v) || 'E-mail must be valid',
        ],
        passwordRules: [
            (v) => !!v || 'Password is required',
        ],
    }),
    methods: {
        ...mapActions(['login']),
        onLogin () {
            const { valid, email, password } = this
            valid && this.login({
                email,
                password,
            })
        },
    },
}
</script>
