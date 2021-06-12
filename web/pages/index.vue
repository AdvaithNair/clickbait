<template>
    <div>
        <Header />
        <PreviewGrid v-bind:videos="videos" />
    </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'nuxt-property-decorator';
import axios from '../utils/axios';
import Header from '../components/General/Header.vue';
import PreviewVideo from '../components/Video/Preview/PreviewVideo.vue';
import PreviewGrid from '../components/Video/Preview/PreviewGrid.vue';
import { formatCount, formatVideoArray } from '../utils/format';
import { formatRelative } from '../utils/time';

const IndexSettings = Vue.extend({
    name: 'Index',
    components: {
        Header,
        PreviewVideo,
        PreviewGrid,
    },
});

Component.registerHooks(['asyncData', 'head']);

@Component
export default class Index extends IndexSettings {
    async asyncData() {
        const res = await axios.get('/api/videos/random');
        console.log('API');
        console.log(res.data);
        formatVideoArray(res.data);
        return { videos: res.data };
    }
}
</script>

<style></style>
