<template>
    <div class="mt-3 mt-md-0">
        <div v-for="e in elementsList" v-bind:key="e.id" class="mt-2">
            <router-link :to="'/detail/' + e.id" class="card-link">
                <b-card
                :header="e.title"
                header-bg-variant="primary"
                header-text-variant="white">
                    <b-card-text>{{e.description}}</b-card-text>
                </b-card>
            </router-link>
        </div>
    </div>
</template>

<script>
    export default {
        name: "ListDefault",
        props: [
            'elementsList'
        ],
        data(){
            return {
                elements: []
            };
        },
        methods: {
        },
    }
</script>

<style scoped>
    a.card-link,
    a.card-link:hover {
        color: black;
        text-decoration: none;
    }
</style>