<template>
    <div>
        <b-list-group>
            <div v-for="c in categories" v-bind:key="c.id">
                <b-list-group-item button>
                    <router-link to="'/category/' + c.id + '/elements'">{{c.title}}</router-link>
                </b-list-group-item>
            </div>
        </b-list-group>
    </div>
</template>

<script>
    export default {
        name: "Categories",
        created() {
            this.findAll();
        },
        data(){
            return {
                categories: []
            };
        },
        methods: {
            findAll: function () {
                fetch("http://127.0.0.1:8000/api/category/?format=json")
                    .then(response => response.json())
                    .then(response => this.categories = response);
            }
        }
    }
</script>

<style scoped>

</style>