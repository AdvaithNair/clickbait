<template>
    <div>
        <Header />
        <FullVideo v-bind:video="video" />
        <div class="recommended">
            <div class="item" v-for="(item, index) in recommended" :key="index">
                <PreviewVideo v-bind:video="item" />
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'nuxt-property-decorator';
import axios from '../../utils/axios';
import Header from '../../components/General/Header.vue';
import FullVideo from '../../components/Video/Full/FullVideo.vue';
import PreviewVideo from '../../components/Video/Preview/PreviewVideo.vue';
import { formatVideoArray, formatFullVideo } from '../../utils/format';
import { LightVideo } from '../../utils/types';

const WatchSettings = Vue.extend({
    name: 'Watch',
    components: { Header, FullVideo, PreviewVideo },
});

Component.registerHooks(['asyncData', 'head']);

@Component
export default class Watch extends WatchSettings {
    recommended: Array<LightVideo | undefined> = new Array(4).fill(undefined);

    async asyncData({ params, redirect }: { params: any; redirect: Function }) {
        if (!params.video) redirect('/');

        // Get Video Data
        const vid = await axios.get('/api/recommender/videos/', {
            params: { id: params.video },
        });

        // Video Does Not Exist
        const videoData = vid.data[0];
        if (!videoData) redirect('/LOL');

        console.log(videoData.description);

        formatFullVideo(videoData);

        console.log(videoData.description);
        console.log(typeof videoData.description);

        videoData.src = `https://www.youtube.com/watch?v=${videoData.id}`;

        return { video: videoData };
    }

    async mounted() {
        console.log('MOUNTED');
        if (this as any) {
            const id = (this as any).video.id;
            const recs = await axios.get('/api/recommender/videos/recommend', {
                params: { id, count: 4 },
            });

            if (recs.data != null) formatVideoArray(recs.data);
            else recs.data = new Array(4).fill(undefined);
            this.recommended = recs.data;
        } else {
            this.recommended = new Array(4).fill(undefined);
        }
    }

    head() {
        return {
            title: this
                ? `${(this as any).video.title} - Clickbait`
                : 'Clickbait',
        };
    }
}
</script>

<style scoped>
.recommended {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    flex-flow: wrap;
    max-width: 1400px;
    margin: 0 auto;
    margin-top: 20px;
}

.item {
    width: 25%;
}

@media screen and (max-width: 1000px) {
    .item {
        width: 50%;
    }
}

@media screen and (max-width: 500px) {
    .item {
        width: 100%;
    }
}
</style>
