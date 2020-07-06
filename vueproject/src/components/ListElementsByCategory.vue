<template>
    <div>
        <h1>Element list by category</h1>
        <ListDefault :elements-list="elements"></ListDefault>
    </div>
</template>

<script>
    import ListDefault from "./partials/_ListDefault";

    export default {
        name: "ListElementsByCategory",
        components:{
            ListDefault
        },
        created() {
            this.findElementsByCategory();
        },
        data(){
            return {
                elements: [],
            };
        },
        methods: {
            findElementsByCategory: function () {
                fetch("http://127.0.0.1:8000/api/category/" + this.$route.params.id + "/elements/?format=json")
                    .then(response => response.json())
                    .then(response => this.elements = response);
            }
        },
        watch: {
            "$route.params.id": function () {
                this.findElementsByCategory();
            }
        },
    }
</script>

<style scoped>

</style>