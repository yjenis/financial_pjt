<template>
    <div class="container">
      <h1>My Page</h1>
      <p>Username: {{ username }}</p>
    </div>
</template>
  
<script setup>
  import { useRoute } from 'vue-router';
  import { onMounted, ref } from 'vue';
  import { useCounterStore } from '@/stores/counter'
  import axios from 'axios';  // axios를 임포트합니다


  const userStore = useCounterStore()
  const route = useRoute();

  onMounted(() => {
  axios({
      method: 'put',
      url: `${userStore.API_URL}/users/${route.params.username}/info/`,
      headers: {
        Authorization: `Token ${userStore.token}`
      }
    })
      .then((res) => {
        userStore.getUserInfo(username)
        console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    })




  
</script>

<style scoped>

</style>