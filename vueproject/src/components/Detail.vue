<template>
    <div>
        <b-card>
            <h1>{{ element.title }}</h1>
            <div class="p-3">
                <router-link class="btn btn-primary" :to="{ name:'ListElementsByCategory', params:{id:element.category} }">
                    {{ category.title }}
                </router-link>
                <router-link class="btn btn-primary ml-2" :to="{ name:'ListElementsByType', params:{id:element.type} }">
                    {{ type.title }}
                </router-link>
                <b-card-text>{{element.description}}</b-card-text>
            </div>
        </b-card>
    </div>
</template>

<script>
    export default {
        name: "Detail",
        created() {
            this.find()
        },
        data() {
            return {
                element: Object,
                category: Object,
                type: Object,
            };
        },
        methods: {
            find: function () {
                fetch("http://127.0.0.1:8000/api/element/" + this.$route.params.id + "/?format=json")
                    .then(response => response.json())
                    .then(response => {
                        this.element = response
                        this.findCategory(this.element.category)
                        this.findType((this.element.type))
                    });
            },
            findCategory: function (id) {
                fetch("http://127.0.0.1:8000/api/category/" + id + "/?format=json")
                    .then(response => response.json())
                    .then(response => this.category = response);
            },
            findType: function (id) {
                fetch("http://127.0.0.1:8000/api/type/" + id + "/?format=json")
                    .then(response => response.json())
                    .then(response => this.type = response);
            },
        },
    }
</script>

<style scoped>

</style>