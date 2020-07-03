<template>
    <div>
        <b-list-group>
            <div v-for="t in types" v-bind:key="t.id">
                <b-list-group-item button>
                    <router-link to="'/type/' + t.id + '/elements'">{{t.title}}</router-link>
                </b-list-group-item>
            </div>
        </b-list-group>
    </div>
</template>

<script>
    export default {
        name: "Types",
        created() {
            this.findAll();
        },
        data(){
            return {
                types: []
            };
        },
        methods: {
            findAll: function () {
                fetch("http://127.0.0.1:8000/api/type/?format=json")
                    .then(response => response.json())
                    .then(response => this.types = response);
            }
        }
    }
</script>

<style scoped>

</style>