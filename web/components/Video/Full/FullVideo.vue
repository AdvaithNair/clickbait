<template>
    <div class="preview">
        <div class="thumbnail">
            <img :src="video.thumbnail" alt="picture" />
        </div>
        <h1 class="title">{{ video.title }}</h1>
        <h2 class="channel">{{ video.channel }}</h2>
        <p class="info">{{ video.views }} views • {{ video.date }}</p>
    </div>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue';
import Component from 'vue-class-component';
import { Video } from '../../../utils/types';
import { defaultVideo } from '../../../utils/defaults';

const FullVideoSettings = Vue.extend({
    name: 'FullVideo',
    props: {
        video: {
            type: Object as PropType<Video>,
            default: () => {
                return { ...defaultVideo, date: 'just now' };
            },
        },
    },
});

@Component
export default class FullVideo extends FullVideoSettings {}
</script>

<style scoped>
.preview {
    width: 100%;
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

.title,
.channel,
.info {
    text-overflow: ellipsis;
    overflow: hidden;
    white-space: nowrap;
    width: 100%;
}

.title {
    color: black;
    margin-top: 5px;
    font-size: 22px;
}

.channel {
    font-size: 18px;
}

.channel,
.info {
    color: grey;
}

.info {
    color: #bbb;
    font-size: 16px;
}
</style>
