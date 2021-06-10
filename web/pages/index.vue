<template>
    <div>
        <Header />
        <PreviewGrid v-bind:videos="videos" />
    </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Component from 'vue-class-component';
import axios from '../utils/axios';
import Header from '../components/General/Header.vue';
import PreviewVideo from '../components/Video/Preview/PreviewVideo.vue';
import PreviewGrid from '../components/Video/Preview/PreviewGrid.vue';
import { LightVideo } from '../utils/types';
import { formatCount } from '../utils/formatCount';
import { formatRelative } from '../utils/time';
import { defaultLightVideo } from '../utils/defaults';

const IndexSettings = Vue.extend({
    name: 'Index',
    components: {
        Header,
        PreviewVideo,
        PreviewGrid,
    },
});

@Component
export default class Index extends IndexSettings {
    videos: Array<LightVideo | undefined> = new Array(8).fill(undefined);
    video: LightVideo | undefined = defaultLightVideo;

    async mounted() {
        const res = await axios.get('/videos/random');
        for (let item of res.data) {
            item.thumbnail = `https://i.ytimg.com/vi/${item.id}/hqdefault.jpg`;
            item.views = formatCount(item.views ?? 0) as any;
            item.date = formatRelative(item.date);
        }
        console.log(res.data);
        this.videos = res.data;
        this.video = this.videos[0];
    }
}
</script>

<style></style>
