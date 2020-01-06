<template>
    <v-flex grow>
        <v-toolbar short flat color="white" v-if="!hideHeader">
            <v-toolbar-title>
                <slot name="title"></slot>
            </v-toolbar-title>
            <v-spacer></v-spacer>
            <slot name="toolbar"></slot>
            <v-toolbar-items>
                <slot name="items"></slot>
            </v-toolbar-items>
        </v-toolbar>
        <slot></slot>
    </v-flex>
</template>

<script>
export default {
    name: 'BaseView',
    props: {
        hideHeader: {
            type: Boolean,
            default: false,
        },
    },
}
</script>
