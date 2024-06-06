

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter'


const store = useCounterStore()
const product = store.exchange

onMounted(() => {
  store.exchangeInfo()
})


const selectedRate = ref('ttb');
const selectedCountry = ref('USD'); // 'usd'를 'USD'로 변경
const amount = ref(0);

const filteredProduct = computed(() => {
  return product.find(p => p.cur_unit === selectedCountry.value)
})

const tempAmount = computed(() => {
  const rate = filteredProduct.value[selectedRate.value];
  if (typeof rate === 'string' && rate.includes(',')) {
    return parseFloat(rate.replace(/,/g, ''));
  }
  return rate
});

const computedAmount = computed(() => {
  return tempAmount.value * amount.value
});

</script>

<template>
  <div class="container">
    <h3>환율 계산기</h3>
    <br>

    <div class="dropdown">
      <label for="rate">환율 기준:</label>
      <select v-model="selectedRate" id="rate">
        <option value="ttb">송금 받을 때</option>
        <option value="tts">송금 보낼 때</option>
        <option value="deal_bas_r">매매 기준율</option>
      </select>
    </div>

    <div class="dropdown">
      <label for="country">환율 계산 국가:</label>
      <select v-model="selectedCountry" id="country">
        <option value="USD">미국 달러 (USD)</option>
        <option value="EUR">유로 (EUR)</option>
        <option value="JPY(100)">일본 엔 (JPY)</option>
        <option value="CNH">중국 위안 (CNH)</option>
        <option value="GBP">영국 파운드 (GBP)</option>
      </select>
    </div>

    

    <div class="amount-input">
      <label for="amount">금액:</label>
      <input type="number" v-model.number="amount" id="amount">
    </div>

    <div class="result">
      <label>계산 결과:</label>
      <div class="result-value">{{ computedAmount }}</div>
    </div>
  </div>

  <!-- <iframe
src="https://www.chatbase.co/chatbot-iframe/-lljE9xpFadkkOdFE5Vm2"
title="REACHRICH"
width="100%"
style="height: 100%; min-height: 700px"
frameborder="0"
></iframe> -->

</template>

<style scoped>
.container {
  width: 100%;
  max-width: 400px;
  margin: 100px auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

h3 {
  margin-top: 0;
  color: #EF4460;
  font-weight: bold;
}

.dropdown {
  margin-bottom: 15px;
  
}

label {
  display: block;
  font-weight: bold;
}

select, input, .result-value {
  width: 100%;
  padding: 8px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.result {
  margin-top: 20px;
}

.result label {
  font-weight: bold;
}
</style>



<!-- const computedAmount = computed(() => {
  let multiplier = 1;

  if (selectedRate.value === 'ttb') {
    multiplier = 10;
  } else if (selectedRate.value === 'tts') {
    multiplier = 100;
  } else if (selectedRate.value === 'deal_bas_r') {
    multiplier = 1000;
  }

  return amount.value * multiplier;
}); -->