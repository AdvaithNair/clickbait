<template>
    <div class="preview">
        <div class="thumbnail">
            <img :src="video.thumbnail" v-bind:alt="picture" />
        </div>
        <p class="title">{{ video.title }}</p>
        <p class="channel">{{ video.channel }}</p>
        <div class="info">
            <span>{{ video.views }}</span>
            <span>{{ video.date }}</span>
        </div>
    </div>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue';
import Component from 'vue-class-component';
import { LightVideo } from '../../../utils/types';

const PreviewVideoSettings = Vue.extend({
    name: 'PreviewVideo',
    props: {
        video: Object as PropType<LightVideo>,
    },
});

@Component
export default class PreviewVideo extends PreviewVideoSettings {
    mounted() {
        this.video.thumbnail = `https://i.ytimg.com/vi/${this.video.id}/hqdefault.jpg`;
        // this.video.views =
        console.log(this.video);
    }
}
</script>

<style>
.preview {
    width: 20%;
    padding: 10px 20px;
}

.thumbnail {
    width: 100%;
    overflow: hidden;
    margin: 0;
    padding-top: 56.25%;
    position: relative;
    border-radius: 5px;
}

.thumbnail img {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 100%;
    transform: translate(-50%, -50%);
}

.title {
    text-overflow: ellipsis;
    overflow: hidden;
    white-space: nowrap;
    width: 100%;
}

.channel,
.info {
    color: grey;
    font-size: 14px;
}

.info {
    color: #bbb;
}
</style>
