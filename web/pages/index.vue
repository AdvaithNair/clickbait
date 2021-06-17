<template>
    <div>
        <Header />
        <h2 v-if="notFound" class="could-not-fetch">Could Not Fetch Videos</h2>
        <PreviewGrid v-bind:videos="videos" v-else />
    </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'nuxt-property-decorator';
import axios from 'axios';
import Header from '../components/General/Header.vue';
import PreviewVideo from '../components/Video/Preview/PreviewVideo.vue';
import PreviewGrid from '../components/Video/Preview/PreviewGrid.vue';
import { formatVideoArray } from '../utils/format';
import { HOST_URL, RECOMMENDER_URL } from '../utils/services';

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
        try {
            const res = await axios.get(
                ((process as any).client ? HOST_URL : RECOMMENDER_URL) +
                    '/api/recommender/videos/random',
            );
            formatVideoArray(res.data);
            return { videos: res.data, notFound: false };
        } catch (e) {
            console.error(e);
            return { videos: [], notFound: true };
        }
    }
}
</script>

<style>
.could-not-fetch {
    text-align: center;
    margin-top: 20px;
}
</style>
