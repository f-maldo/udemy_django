<template>
    <div>
        <b-table striped hover :items="elements" :fields="fields"></b-table>
    </div>
</template>

<script>
    export default {
        name: "Table",
        created() {
            this.findAll()
        },
        data(){
            return {
                elements: [],
                fields: [
                    {
                        key: "title",
                        sortable: true
                    },
                    {
                        key: "url_clean",
                        label: "URL Clean",
                        sortable: true,
                        variant: "danger",
                    },
                    {
                        key: 'description',
                        sortable: true
                    },
                    {
                        key: 'category',
                        sortable: true
                    },
                    {
                        key: 'type',
                        sortable: true
                    },
                ],
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