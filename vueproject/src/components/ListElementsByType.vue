<template>
    <b-container>
        <h1>Element list by type</h1>
        <ListDefault :elements-list="elements"></ListDefault>
    </b-container>
</template>

<script>
    import ListDefault from "./partials/_ListDefault";

    export default {
        name: "ListElementsByType",
        components:{
            ListDefault
        },
        created() {
            this.findElementsByType();
        },
        data(){
            return {
                elements: [],
            };
        },
        methods: {
            findElementsByType: function () {
                fetch("http://127.0.0.1:8000/api/type/" + this.$route.params.id + "/elements/?format=json")
                    .then(response => response.json())
                    .then(response => this.elements = response);
            }
        },
    }
</script>

<style scoped>

</style>