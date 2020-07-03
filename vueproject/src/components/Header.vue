<template>
    <div>
        <b-navbar type="dark" variant="dark" class="mb-3">
            <b-navbar-brand>Elements</b-navbar-brand>
            <b-navbar-nav>
                <b-nav-item>Home</b-nav-item>
                <b-nav-item-dropdown text="Lang" right>
                    <b-dropdown-item>EN</b-dropdown-item>
                    <b-dropdown-item>ES</b-dropdown-item>
                    <b-dropdown-item>CN</b-dropdown-item>
                </b-nav-item-dropdown>
                <b-nav-item-dropdown text="User" right>
                    <b-dropdown-item>Account</b-dropdown-item>
                    <b-dropdown-item>Settings</b-dropdown-item>
                </b-nav-item-dropdown>
            </b-navbar-nav>
        </b-navbar>
    </div>
</template>

<script>
    export default {
        name: "Header"
    }
</script>

<style scoped>
</style>