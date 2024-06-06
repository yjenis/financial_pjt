<template>
  <div class="whole">
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
    
    <!-- 전체 목록 보여주기 -->
    <!-- <h3>정기예금 전체목록</h3> -->

    <!-- <h5>기간 선택: {{ selected }}</h5> -->

    <!-- <select v-model="selected">
      <option disabled value="">기간 선택</option>
      <option>전체 목록</option>
      <option>12개월</option>
      <option>24개월</option>
      <option>36개월</option>
    </select> -->
    <!-- <p>기간 선택</p> -->
    <select v-model="selected" class="form-select" aria-label="Default select example">
      <option value="" disabled>기간 선택</option>
      <option>전체 목록</option>
      <option>12개월</option>
      <option>24개월</option>
      <option>36개월</option>
    </select>




    <table class="table">
      <tr >
        <th style="width: 30%; ">은행명</th>
        <th style="width: 40%;">상품명</th>
        <th style="width: 30%;">최고 금리</th>
      </tr>
    <!-- 여기에 각 행을 반복하여 추가 -->
    </table>

    

    <div class="select">
      <div v-if="selected === '전체 목록'">
        <DepositList v-for="deposit in product" :key="deposit.id" :deposit="deposit" />

      </div>

      <div v-else-if="selected === '12개월'">
        <DL12 v-for="deposit in twelve" :key="deposit.id" :deposit="deposit" />
      </div>
      
      <div v-else-if="selected === '24개월'">
        <DL24 v-for="deposit in twentyfour" :key="deposit.id" :deposit="deposit" />
      </div>

      <div v-else-if="selected === '36개월'">
        <DL36 v-for="deposit in thirtysix" :key="deposit.id" :deposit="deposit" />
      </div>

    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import { RouterLink, useRoute, useRouter } from 'vue-router'
import axios from 'axios'
import { onMounted, ref } from 'vue';
import DepositList from './DepositList.vue';
import DL12 from './DL12.vue';
import DL24 from './DL24.vue';
import DL36 from './DL36.vue';

// 현재 경로를 가져옵니다.
const route = useRoute();
const router = useRouter();

// 현재 경로가 활성화된 경로인지 확인하는 함수입니다.
const isActiveRoute = (routeName) => {
  return route.name === routeName;
};



const store = useCounterStore();
const product = store.deposit;

const selected = ref('');
onMounted(() => {
  store.depositInfo();
  // store.savingInfo();
});

// 12개월로 정렬한 데이터 보여주기
const twelve = ref([]);
const twelveInfo = function(){
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/finlife/deposit-products/sort_12/'
  }).then((res) => {
    twelve.value = res.data;
  })
  .catch(err => {
    console.log(err);
  });
};

const twentyfour = ref([]);
const twentyfourInfo = function(){
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/finlife/deposit-products/sort_24/'
  }).then((res) => {
    twentyfour.value = res.data;
  })
  .catch(err => {
    console.log(err);
  });
};

const thirtysix = ref([]);
const thirtysixInfo = function(){
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/finlife/deposit-products/sort_36/'
  }).then((res) => {
    thirtysix.value = res.data;
  })
  .catch(err => {
    console.log(err);
  });
};

onMounted(() => {
  twelveInfo(); // 컴포넌트가 마운트되면 데이터 가져오기
  twentyfourInfo();
  thirtysixInfo();
  if (route.name !== 'Saving') {
    router.push({ name: 'Deposit' });
  }
});
</script>

<style scoped>
.whole{
  /* overflow-y: scroll; */
  /* overflow-y: hidden; */
  padding-left: 20%;
  padding-right: 20%;
  margin-left: 5%;
  margin-right: 5%;
  /* width: 100%;
  margin:auto(); */
}

.form-select{
  width:30%
}

.table-container {
  overflow-x: auto;
  max-width: calc(100% - 40px);
  overflow-y: hidden;
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
  text-align: left; /* 텍스트 왼쪽 정렬 */
}

td {
  padding: 10px; /* 열 간격 조절 */
  text-align: left; /* 텍스트 왼쪽 정렬 */
}

tr{
  background-color: ;
  text-align: center;
}

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
  background-color: ;
  text-align: center;
}

/* 테이블 경계 선 스타일 설정 */
th, td {
  border-top: 0.5px solid #dddddd; 
  border-bottom: 0.5px solid #dddddd;
  text-align: center;
}

select {
  margin-bottom: 20px; /* select와 table 사이 간격 조절 */
}
</style>
