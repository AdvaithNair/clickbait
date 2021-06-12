<template>
    <div class="preview">
        <YouTube v-bind:videoId="video.id" />
        <h1 class="title">{{ video.title }}</h1>
        <h2 class="channel">{{ video.channel }}</h2>
        <p class="info">{{ video.views }} views • {{ video.date }}</p>
        <p class="description">{{ video.description }}</p>
        <div class="tags">
            <div v-for="(item, index) in video.tags" :key="index">
                <p class="tag">{{ item }}</p>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue';
import Component from 'vue-class-component';
import { Video } from '../../../utils/types';
import { defaultVideo } from '../../../utils/defaults';
import YouTube from '../YouTube/YouTube.vue';

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
    components: {
        YouTube,
    },
});

@Component
export default class FullVideo extends FullVideoSettings {}
</script>

<style scoped>
.preview {
    width: 100%;
    padding: 10px 20px;
    max-width: 1400px;
    margin: 0 auto;
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

.description {
    white-space: pre-wrap;
    margin-top: 10px;
    font-size: 14px;
    color: #aaa;
}

.tags {
    display: flex;
    justify-content: flex-start;
    flex-flow: wrap;
    flex-direction: row;
    margin-top: 20px;
}

.tag {
    background: #ef6e26;
    color: white;
    font-weight: 400;
    display: flex;
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 14px;
    margin-right: 10px;
    margin-bottom: 10px;
}
</style>
