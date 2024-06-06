<template>
  <div class="saving-details">
    <h1>{{ saving.fin_prdt_nm }}</h1>
    <p class="company-name">{{ saving.kor_co_nm }}</p>
    <hr>

    <div class="details-section">
      <h2>만기 후 이자율</h2>
      <pre>{{ saving.mtrt_int }}</pre>
      <br>

      <h2>가입 조건</h2>
      <pre>{{ saving.etc_note }}</pre>
      <br>

      <h2>가입 가능 여부</h2>
      <pre v-if="saving.join_deny === 1">가입 불가</pre>
      <pre v-else>가입 가능</pre>
      <br>

      <h2>가입 대상</h2>
      <pre>{{ saving.join_member }}</pre>
      <br>

      <h2>가입 방법</h2>
      <pre>{{ saving.join_way }}</pre>
      <br>

      <h2>특별 우대 조건</h2>
      <pre>{{ saving.spcl_cnd }}</pre>
      <br>

      <h2>최대 한도</h2>
      <pre v-if="saving.max_limit">{{ saving.max_limit }}</pre>
      <pre v-else>제한 없음</pre>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const route = useRoute();
const store = useCounterStore();

const id = parseInt(route.params.id);
console.log(id);
const saving = store.saving.find(item => item.id === id);
</script>

<style scoped>
.saving-details {
  padding-left: 20%;
  padding-right: 20%;
  margin-left: 5%;
  margin-right: 5%;
}

.product-image {
  width: 100%;
  height: auto;
  margin-bottom: 20px;
}

.details-section {
  margin-top: 20px;
}

h1 {
  font-size: 2em;
  margin-bottom: 10px;
  font-weight: bold;
  color: #EF4460;
}

h2 {
  font-size: 1.2em;
  margin-top: 20px;
  font-weight: bold;
}

.company-name {
  font-weight: bold;
  color: #555;
}

pre {
  background-color: #f4f4f4;
  padding: 10px;
  border-radius: 5px;
  white-space: pre-wrap;
}
</style>
