<!-- recommend.vue -->
<template>
  <div class="recommend-container">
    <h1 class="title">추천 상품</h1>
    <p class="description">연령, 자산, 소득에 따른 추천 상품입니다.</p>
    <div class="comp">
      <table class="table">
        <tr>
          <th style="width: 50%;">상품명</th>
          <th style="width: 50%;">가입자 수</th>
        </tr>
        <!-- 여기에 각 행을 반복하여 추가 -->
      </table>
      <div class="recommend-list">
        <RecommendList v-for="item in newLst" :key="item.id" :recommend="item"/>
      </div>
    </div>
  </div>
</template>

<script setup>
import RecommendList from './RecommendList.vue';
import { ref, onMounted, watch } from 'vue';
import axios from 'axios';
import { useCounterStore } from '@/stores/counter';
const store = useCounterStore();
const userInfo = store.userInfo;

defineProps({
  myAge: Number
});

const recommend = ref([]);
const age = ref(45);
const newAge = ref(Math.floor(userInfo.age / 10) * 10);
const newLst = ref([]);

// 추천 정보를 가져오는 함수
const recommendInfo = function() {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/finlife/recommend/'
  }).then((res) => {
    recommend.value = res.data.user_data;
    updateNewLst();
  }).catch(err => {
    console.log(err);
  });
};

// newAge에 따라 newLst를 업데이트하는 함수
const updateNewLst = () => {
  newLst.value = recommend.value[newAge.value] || [];
};

onMounted(() => {
  recommendInfo();
});

watch(newAge, () => {
  updateNewLst();
});
</script>

<style scoped>
.recommend-container {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  margin: 40px auto;
  text-align: center;
}

.table {
  background-color: #ddd;
  border-radius: 10px 0 0 0;
  width: 100%;
}

.table tr {
  width: 100%;
}

.table th, .table td {
  padding: 7px 5px; /* 셀에 패딩을 추가하여 높이 증가 */
  background-color: pink;
}

.comp {
  border: 1px solid #ddd;
  border-radius: 10px;
}

.title {
  font-size: 2em;
  font-weight: bolder;
  color: #333;
  margin-bottom: 20px;
}

.description {
  font-size: 1.2em;
  color: #EF4460;
  margin-bottom: 20px;
}

.recommend-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
</style>