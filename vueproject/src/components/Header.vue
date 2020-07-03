<template>
    <div>
        <b-navbar type="dark" variant="dark" class="mb-3">
            <b-navbar-brand>Elements</b-navbar-brand>
            <b-navbar-nav>
                <b-nav-item>Home</b-nav-item>
                <b-nav-item-dropdown text="Categories" right>
                    <b-dropdown-item v-for="c in categories" v-bind:key="c.id" :to="'/category/' + c.id + '/elements'">
                        {{c.title}}
                    </b-dropdown-item>
                </b-nav-item-dropdown>
                <b-nav-item-dropdown text="Types" right>
                    <b-dropdown-item v-for="t in types" v-bind:key="t.id" :to="'/type/' + t.id + '/elements'">
                        {{t.title}}
                    </b-dropdown-item>
                </b-nav-item-dropdown>
            </b-navbar-nav>
        </b-navbar>
    </div>
</template>

<script>
    export default {
        name: "Header",
        created() {
            this.findAllCategories();
            this.findAllTypes();
        },
        data() {
            return {
                categories: [],
                types: [],
            };
        },
        methods: {
            findAllCategories: function () {
                fetch("http://127.0.0.1:8000/api/category/?format=json")
                    .then(response => response.json())
                    .then(response => this.categories = response);
            },
            findAllTypes: function () {
                fetch("http://127.0.0.1:8000/api/type/?format=json")
                    .then(response => response.json())
                    .then(response => this.types = response);
            }
        },
    }
</script>

<style scoped>
</style>