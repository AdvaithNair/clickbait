<template>
    <div>
        <Header />
        <h2 v-if="notFound" class="could-not-fetch">Video Does Not Exist</h2>
        <div v-else>
            <FullVideo v-bind:video="video" />
            <div class="recommended">
                <div
                    class="item"
                    v-for="(item, index) in recommended"
                    :key="index"
                >
                    <PreviewVideo v-bind:video="item" />
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { Component } from 'nuxt-property-decorator';
import axios from 'axios';
import Header from '../../components/General/Header.vue';
import FullVideo from '../../components/Video/Full/FullVideo.vue';
import PreviewVideo from '../../components/Video/Preview/PreviewVideo.vue';
import { formatVideoArray, formatFullVideo } from '../../utils/format';
import { LightVideo } from '../../utils/types';
import { HOST_URL, RECOMMENDER_URL } from '../../utils/services';

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

        try {
            // Get Video Data
            const res = await axios.get(
                ((process as any).client ? HOST_URL : RECOMMENDER_URL) +
                    '/api/recommender/videos',
                {
                    params: { id: params.video },
                },
            );

            // Video Does Not Exist
            const videoData = res.data[0];
            if (!videoData) return { video: undefined, notFound: true };

            // Format Video
            formatFullVideo(videoData);
            videoData.src = `https://www.youtube.com/watch?v=${videoData.id}`;

            return { video: videoData, notFound: false };
        } catch (e) {
            console.error(e);
            return { video: undefined, notFound: true };
        }
    }

    async mounted() {
        /*if ((this as any) && (this as any).video) {
            const id = (this as any).video.id;
            const recs = await axios.get(
                HOST_URL + '/api/recommender/videos/recommend',
                {
                    params: { id, count: 4 },
                },
            );

            if (recs.data != null) formatVideoArray(recs.data);
            else recs.data = new Array(4).fill(undefined);
            this.recommended = recs.data;
        } else {
            this.recommended = new Array(4).fill(undefined);
        }*/
    }

    head() {
        return {
            title:
                this && (this as any).video
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
