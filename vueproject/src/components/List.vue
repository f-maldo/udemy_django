<template>
    <div>
        <ListDefault :elements-list="elements"></ListDefault>
    </div>
</template>

<script>
    import ListDefault from "./partials/_ListDefault";

    export default {
        name: "List",
        components: {
            ListDefault
        },
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
        },
    }
</script>

<style scoped>
</style>