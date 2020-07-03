<template>
    <b-container>
        <div v-for="e in elements" v-bind:key="e.id">
            <router-link :to="'/detail/' + e.id">
                <b-card :title="e.title">
                    <b-card-text>{{e.description}}</b-card-text>
                </b-card>
            </router-link>
        </div>
    </b-container>
</template>

<script>
    export default {
        name: "List",
        created() {
            this.findAll()
        },
        data(){
            return {
                elements: []
            };
        },
        methods: {
            findAll: function () {
                fetch("http://127.0.0.1:8000/api/element/?format=json")
                    .then(response => response.json())
                    .then(response => this.elements = response)
            }
        }
    }
</script>

<style scoped>
</style>