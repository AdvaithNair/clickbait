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
import { formatCount } from '../utils/formatCount';
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
        const res = await axios.get('/videos/random');
        for (const item of res.data) {
            item.thumbnail = `https://i.ytimg.com/vi/${item.id}/hqdefault.jpg`;
            item.views = formatCount(item.views ?? 0) as any;
            item.date = formatRelative(item.date);
        }
        return { videos: res.data };
    }
}
</script>

<style></style>
