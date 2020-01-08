<template>
    <v-card class="mx-auto" style="min-height: 209px;">
        <v-card-title style="min-height: 60px;">
            <div class="title font-weight-light">
                <b>{{ friend.name }} {{ friend.lastName }}</b>
            </div>
        </v-card-title>
        <v-card-subtitle>
        </v-card-subtitle>
        <v-card-text style="min-height: 80px;">
            <v-flex>Email: {{ friend.email }}</v-flex>
            <v-flex>Age: {{ friend.age }} Sex: {{ friend.sex }}</v-flex>
            <v-flex>Country: {{ friend.country }}</v-flex>
            <v-flex>Hobbies: {{ friend.hobbies }}</v-flex>
        </v-card-text>
    </v-card>
</template>

<script>
export default {
    name: 'FriendCard',
    props: {
        friend: {
            type: Object,
            required: true,
        },
    },
}
</script>
