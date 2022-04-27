<template>
  <div id="app">
    <h1> TWEET LIST </h1>
    <TweetList />
  </div>
</template>

<script>
import TweetList from './components/TweetList.vue'
export default {
  name: 'App',
  components: {
    TweetList
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>