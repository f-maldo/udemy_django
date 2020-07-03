<template>
    <b-container>
        <b-card :title="element.title">
            <b-card-text>{{element.description}}</b-card-text>
        </b-card>
    </b-container>
</template>

<script>
    export default {
        name: "Detail",
        created() {
            this.find()
        },
        data() {
            return {
                element: Object
            };
        },
        methods: {
            find: function () {
                fetch("http://127.0.0.1:8000/api/element/" + this.$route.params.id + "/?format=json")
                    .then(response => response.json())
                    .then(response => this.element = response)
            }
        },
    }
</script>

<style scoped>

</style>