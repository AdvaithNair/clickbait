<template>
    <div>
        <Header />
        <h2>{{ hello }}</h2>
    </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Component from 'vue-class-component';
import axios from '../utils/axios';
import Header from '../components/General/Header.vue';

const IndexSettings = Vue.extend({
    name: 'Index',
    components: {
        Header,
    },
});

@Component
export default class Index extends IndexSettings {
    hello = 'lol';
    async mounted() {
        const res = await axios.get('/');
        console.log(res.data);
        this.hello = res.data;
    }
}

/*export default Vue.extend({
    props: {
        hello: {
            type: String,
            default: 'Loading...',
            required: true,
        },
    },
    mounted: () => {
        Vue.nextTick(async () => {
            const res = await axios.get('/');
            .hello = res.data;
        });
    },
});*/
</script>

<style></style>
