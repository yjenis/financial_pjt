<template>
  <div class="deposit-details">
    <h1>{{ deposit.fin_prdt_nm }}</h1>
    <p class="company-name">{{ deposit.kor_co_nm }}</p>
    <hr>
    <!-- <br> -->

    <div class="details-section">
      <!-- <h2>상품 코드</h2>
      <p>{{ deposit.fin_prdt_cd }}</p> -->

      <h2>만기 후 이자율</h2>
      <pre>{{ deposit.mtrt_int }}</pre>
      <br>

      <h2>가입 조건</h2>
      <pre>{{ deposit.etc_note }}</pre>
      <br>

      <h2>가입 가능 여부</h2>
      <pre v-if="deposit.join_deny === 1">가입 불가</pre>
      <pre v-else>가입 가능</pre>
      <br>

      <h2>가입 대상</h2>
      <pre>{{ deposit.join_member }}</pre>
      <br>

      <h2>가입 방법</h2>
      <pre>{{ deposit.join_way }}</pre>
      <br>

      <h2>특별 우대 조건</h2>
      <pre>{{ deposit.spcl_cnd }}</pre>
      <br>

      <h2>최대 한도</h2>
      <pre v-if="deposit.max_limit">{{ deposit.max_limit }}</pre>
      <pre v-else>제한 없음</pre>
    </div>
  </div>
  <!-- {{ deposit.kor_co_nm}} -->
  <!-- {{ name }} -->

  <!-- <br> -->
  <!-- {{ deposit }} -->
  
  <!-- <div v-if="product">
    <h1>{{ product.fin_prdt_nm }}</h1>
    <p>Company: {{ product.kor_co_nm }}</p>
    <p>Interest Rate: {{ product.intr_rate2 }}</p>
    <p>Product Code: {{ product.fin_prdt_cd }}</p>
  </div>
  <div v-else>
    <p>다시 해봐바</p>
  </div> -->
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const route = useRoute();
const store = useCounterStore();
const product = ref(null);

// onMounted(() => {
//   const id = parseInt(route.params.id); // URL 파라미터로부터 id를 가져옴
//   console.log(id)
//   if (id) {
//     const deposit = store.deposit.find(item => item.id === id);
//   } 
// });

const id=parseInt(route.params.id)
console.log(id)
const deposit = store.deposit.find(item => item.id === id)
// const name=deposit.kor_co_nm
// console.log(name)
// const imageSrc = `@/assets/${name}.jpg`
// // const ur=imageSrc.value
// console.log(imageSrc)

// console.log({imageSrc})
</script>

<style scoped>
/* 스타일 설정 */
.deposit-details {
  /* padding-top:20px;
  padding-bottom: 0%; */
  padding-left: 20%;
  padding-right: 20%;
  margin-left: 5%;
  margin-right: 5%;
  /* max-width: 800px; */
  /* margin: auto;
  padding: 20px; */
  /* font-family: Arial, sans-serif; */
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
