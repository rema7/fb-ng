<template>
    <v-card class="mx-auto" style="min-height: 209px;">
        <v-card-title style="min-height: 60px;">
            <div class="title font-weight-light">
                <b>{{ friend.name }} {{ friend.lastName }}</b>
            </div>
            <v-spacer/>
        </v-card-title>
        <v-card-text style="min-height: 80px;">
        </v-card-text>
        <v-divider/>
        <v-card-actions>
        </v-card-actions>
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
