<template>
  <div>
    <!-- <RouterLink :to="{name:'Deposit'}">예금 상품</RouterLink> | -->
    <!-- <RouterLink :to="{name:'Saving'}">적금 상품</RouterLink>  -->
    <!-- <Deposit /> -->
    <!-- {{ store.bank1 }} -->
    
    <Deposit v-for="deposit in deposits" :key="deposit.id" :deposit="deposit"/>
  </div>
</template>

<script setup>
// import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import axios from 'axios'
import { onMounted, ref } from 'vue';

import Deposit from '@/components/Deposit.vue';

// const store=useCounterStore()

// import { onMounted } from 'vue';
// onMounted(() => {
//   store.Bank1()
// })

const deposits = ref([]);
const depositInfo = function(){
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/finlife/deposit-products/'
  }).then((res) => {
    deposits.value = res.data;
  })
  .catch(err => {
    console.log(err);
  });
};

onMounted(()=>{
  depositInfo()
})
</script>



<style scoped>
/* .whole{
  padding:3%
} */
</style>