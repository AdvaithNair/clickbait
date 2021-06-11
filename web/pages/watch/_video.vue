<template>
    <h1>{{ p }}</h1>
</template>

<script>
import Vue from 'vue';
import { Component } from 'nuxt-property-decorator';
// import axios from '../utils/axios';

const WatchSettings = Vue.extend({
    name: 'Watch',
});

Component.registerHooks(['asyncData', 'head']);

@Component
export default class Watch extends WatchSettings {
    async asyncData({ params, redirect }) {
        if (process.server) {
            if (!params.video) redirect(`/`);
            return { p: params.video };
        }
    }
}
</script>

<style></style>
