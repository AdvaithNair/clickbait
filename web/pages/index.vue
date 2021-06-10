<template>
    <div>
        <Header />
        <PreviewVideo v-bind:video="video" />
    </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Component from 'vue-class-component';
import axios from '../utils/axios';
import Header from '../components/General/Header.vue';
import PreviewVideo from '../components/Video/Preview/PreviewVideo.vue';
import { LightVideo } from '../utils/types';

const IndexSettings = Vue.extend({
    name: 'Index',
    components: {
        Header,
        PreviewVideo,
    },
});

@Component
export default class Index extends IndexSettings {
    videos: Array<LightVideo | undefined> = new Array(6).fill(undefined);
    video: LightVideo | undefined | { thumbnail: string } = {
        thumbnail: 'lol',
    };

    async mounted() {
        const res = await axios.get('/videos/random');
        this.videos = res.data;
        this.video = this.videos[0];
    }
}
</script>

<style></style>
