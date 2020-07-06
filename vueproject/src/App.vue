<template>
    <div id="app">
        <Header></Header>
        <b-container>
            <b-row>
                <div class="col-md-4">
                    <Categories></Categories>
                    <br>
                    <Types></Types>
                </div>
                <div class="col-md-8">
                    <router-view></router-view>
                </div>
            </b-row>
        </b-container>
    </div>
</template>

<script>
    import Header from "./components/Header";
    import Categories from "./components/Categories";
    import Types from "./components/Types";

    export default {
        name: 'App',
        components: {
            Types,
            Categories,
            Header,
        }
    }
</script>

<style>
</style>
