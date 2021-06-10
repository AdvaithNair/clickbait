<template>
    <div class="grid">
        <div class="item" v-for="(item, index) in videos" :key="index">
            <PreviewVideo v-bind:video="item" />
        </div>
    </div>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue';
import Component from 'vue-class-component';
import { LightVideo } from '../../../utils/types';
import PreviewVideo from './PreviewVideo.vue';

const PreviewGridSettings = Vue.extend({
    name: 'PreviewGrid',
    components: {
        PreviewVideo,
    },
    props: {
        videos: {
            type: Array as PropType<Array<LightVideo>>,
            default: new Array(8).fill(undefined),
        },
    },
});

@Component
export default class PreviewGrid extends PreviewGridSettings {
    mounted() {
        console.log(this.videos);
    }
}
</script>

<style scoped>
.grid {
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

@media screen and (max-width: 850px) {
    .item {
        width: 50%;
    }
}

@media screen and (max-width: 450px) {
    .item {
        width: 100%;
    }
}
</style>
