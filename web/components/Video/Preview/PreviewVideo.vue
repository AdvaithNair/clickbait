<template>
    <div class="preview">
        <NuxtLink v-bind:to="`/watch/${video.id}`">
            <div class="thumbnail">
                <img :src="video.thumbnail" alt="picture" />
            </div>
        </NuxtLink>

        <p class="title">{{ video.title }}</p>
        <p class="channel">{{ video.channel }}</p>
        <p class="info">{{ video.views }} views • {{ video.date }}</p>
    </div>
</template>

<script lang="ts">
import Vue, { PropType } from 'vue';
import Component from 'vue-class-component';
import { LightVideo } from '../../../utils/types';
import { defaultLightVideo as defaultVideo } from '../../../utils/defaults';

const PreviewVideoSettings = Vue.extend({
    name: 'PreviewVideo',
    props: {
        video: {
            type: Object as PropType<LightVideo>,
            default: () => {
                return { ...defaultVideo, date: 'just now' };
            },
        },
    },
});

@Component
export default class PreviewVideo extends PreviewVideoSettings {
    mounted() {
        // console.log(this.video);
    }
}
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
