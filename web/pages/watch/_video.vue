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
import { formatVideoArray, formatVideo } from '../../utils/format';
import { LightVideo } from '../../utils/types';

const WatchSettings = Vue.extend({
    name: 'Watch',
    components: { Header, FullVideo, PreviewVideo },
});

Component.registerHooks(['asyncData', 'head']);

@Component
export default class Watch extends WatchSettings {
    recommended: Array<LightVideo | undefined> = new Array(4).fill(undefined);

    async asyncData({ params, redirect }) {
        if ((process as any).server) {
            if (!params.video) redirect('/');

            // Get Video Data
            const vid = await axios.get('/api/videos/', {
                params: { id: params.video },
            });

            // Video Does Not Exist
            if (!vid.data[0]) redirect('/LOL');

            formatVideo(vid.data[0]);

            return { video: vid.data[0] };
        }
    }

    async mounted() {
        console.log('MOUNTED');
        const id = (this as any).video.id;
        const recs = await axios.get('/api/videos/recommend', {
            params: { id, count: 4 },
        });

        if (recs.data != null) formatVideoArray(recs.data);
        else recs.data = new Array(4).fill(undefined);
        this.recommended = recs.data;
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
