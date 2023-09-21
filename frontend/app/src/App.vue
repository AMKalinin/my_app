<template>
    <div>
        <NavBar></NavBar>
        <router-view></router-view>
    </div>
</template>

<script>
import NavBar from "@/components/NavBar";

export default{
    components:{
        NavBar
    },
    data(){
        return {
        }
    },
    methods: {
    }
}
</script>

<style>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
</style>