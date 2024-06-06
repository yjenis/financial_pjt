<template>
  <div class=whole>
    <!-- <RouterLink :to="{name:'Deposit'}">예금 상품</RouterLink> |
    <RouterLink :to="{name:'Saving'}">적금 상품</RouterLink>  -->
    <!-- 전체 목록 보여주기 -->
    <!-- {{ product }} -->
    <p class="division">
      <RouterLink
        :to="{ name: 'Deposit' }"
        :class="{ active: isActiveRoute('Deposit') }"
      >
        예금 상품
      </RouterLink> |
      <RouterLink
        :to="{ name: 'Saving' }"
        :class="{ active: isActiveRoute('Saving') }"
      >
        적금 상품
      </RouterLink>
      
    </p>
    <!-- <h3>정기적금 전체목록</h3> -->

    <!-- <h5>기간 선택: {{ selected }}</h5> -->

    <select v-model="selected" class="form-select" aria-label="Default select example">
      <option value="" disabled>기간 선택</option>
      <option>전체 목록</option>
      <option>12개월</option>
      <option>24개월</option>
      <option>36개월</option>
    </select>

    <!-- <h5>정기적금 전체목록</h5> -->
    <table class="table">
      <tr>
        <th style="width: 30%;">은행명</th>
        <th style="width: 40%;">상품명</th>
        <th style="width: 30%;">최고 금리</th>
      </tr>
    <!-- 여기에 각 행을 반복하여 추가 -->
    </table>
    <!-- <DL12/> -->

    <div v-if="selected==='전체 목록'">
      <SavingList
      v-for="saving in product"
      :key="saving.id"
      :saving="saving"/>
    </div>  

    <div v-else-if="selected==='12개월'">
      <!-- <SV12 v-for="saving in twelve" :key="saving.product.fin_prdt_cd" :saving="saving.product" /> -->
      <SV12 v-for="saving in twelve" :key="saving.id" :saving="saving" />

    </div>
    
    <div v-else-if="selected === '24개월'">
      <SV24 v-for="saving in twentyfour" :key="saving.id" :saving="saving" />
    </div>

    <div v-else-if="selected === '36개월'">
      <SV36 v-for="saving in thirtysix" :key="saving.id" :saving="saving" />
    </div>

    

  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { RouterLink, useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const store=useCounterStore()
const product=store.saving

import { onMounted,ref } from 'vue';
import SavingList from './SavingList.vue';
import SV12 from './SV12.vue';
import SV24 from './SV24.vue';
import SV36 from './SV36.vue';

const route = useRoute();
const router = useRouter();

const isActiveRoute = (routeName) => {
  return route.name === routeName;
};

const selected = ref('')
onMounted(() => {
  store.savingInfo()
})

// 12개월로 정렬한 데이터 보여주기
const twelve=ref([])
const twelveInfo =function(){
  axios({
    method:'get',
    url:'http://127.0.0.1:8000/finlife/saving-products/sort_12/'
  }).then((res)=>{
    twelve.value=res.data
    // console.log(twelve)
  })
  .catch(err=>{
    console.log(err)
  })
}

onMounted(() => {
  twelveInfo(); // 컴포넌트가 마운트되면 데이터 가져오기
});

const twentyfour=ref([])
const twentyfourInfo =function(){
  axios({
    method:'get',
    url:'http://127.0.0.1:8000/finlife/saving-products/sort_24/'
  }).then((res)=>{
    twentyfour.value=res.data
  })
  .catch(err=>{
    console.log(err)
  })
}

onMounted(() => {
  twentyfourInfo(); // 컴포넌트가 마운트되면 데이터 가져오기
});

const thirtysix=ref([])
const thirtysixInfo =function(){
  axios({
    method:'get',
    url:'http://127.0.0.1:8000/finlife/saving-products/sort_36/'
  }).then((res)=>{
    thirtysix.value=res.data
  })
  .catch(err=>{
    console.log(err)

  })
}

onMounted(() => {
  thirtysixInfo(); // 컴포넌트가 마운트되면 데이터 가져오기
});

</script>

<style scoped>
.whole{
  padding-left: 20%;
  padding-right: 20%;
  margin-left: 5%;
  margin-right: 5%;
}

.form-select{
  width:30%
}

.division{
  font-size: 25px;
  font-weight: bold;
}

.division a {
  color: black;
  text-decoration: none;
}

.division a.active {
  /* background-color: pink; */
  color: #EF4460;
  /* padding: 0.5em; */
  border-radius: 5px;
}

/* .select {
  padding-top:30px
} */

th {
  padding: 10px; /* 열 간격 조절 */
  text-align: center; /* 텍스트 왼쪽 정렬 */
}

td {
  padding: 10px; /* 열 간격 조절 */
  text-align: left; /* 텍스트 왼쪽 정렬 */
}

/* tr{
  background-color: #faa4b2a4;
} */

/* 짝수 번째 행 배경색 지정 */
/* tr:nth-child(even) {
  background-color: #f2f2f2;
} */

/* 홀수 번째 행 배경색 지정 */
/* tr:nth-child(odd) {
  background-color: #ffffff;
} */

/* 테이블 전체 스타일 설정 */
table {
  border-collapse: collapse; /* 테이블 경계를 합침 */
  width: 100%; /* 테이블 전체 너비 설정 */
}

/* 테이블 경계 선 스타일 설정 */
th, td {
  border-top: 0.5px solid #dddddd; 
  border-bottom: 0.5px solid #dddddd;
  text-align: center; /* 테두리 선 스타일 및 색상 설정 */
}

select {
  margin-bottom: 20px; /* select와 table 사이 간격 조절 */
}
</style>