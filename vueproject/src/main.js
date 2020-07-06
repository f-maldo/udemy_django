import Vue from 'vue'
import App from './App.vue'

import {BootstrapVue, IconsPlugin} from 'bootstrap-vue'
import VueRouter from 'vue-router'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import List from "./components/List";
import Detail from "./components/Detail";
import ListElementsByCategory from "./components/ListElementsByCategory";
import ListElementsByType from "./components/ListElementsByType";

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueRouter)

Vue.config.productionTip = false

    const routes = [
    {path: '/', component:List, name:'list'},
    {path: '/detail/:id', component:Detail, name:'detail'},
    {path: '/type/:id/elements', component:ListElementsByType, name:'ListElementsByType'},
    {path: '/category/:id/elements', component:ListElementsByCategory, name:'ListElementsByCategory'},
]

const router = new VueRouter({
    mode: 'history',
    routes
})

new Vue({
    router,
    render: h => h(App),
}).$mount('#app')
