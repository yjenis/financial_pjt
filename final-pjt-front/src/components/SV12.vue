<template>
  <table>
    <tr>
      <th style="width: 30%;">{{ saving.product.kor_co_nm }}</th>
      <th style="width: 40%;">
        <RouterLink :to="{ name: 'SavingDetail', params: { id: saving.product.id } }">
          {{ saving.product.fin_prdt_nm }}
        </RouterLink>
      </th>
      <th style="width: 30%;">{{ saving.option.intr_rate2 }}</th>
    </tr>
    <!-- 여기에 각 행을 반복하여 추가 -->
  </table>
  <hr>
</template>

<script setup>
defineProps({
  saving: Object
});
</script>

<style scoped>


th {
  padding: 10px; /* 열 간격 조절 */
  text-align: center;/* 텍스트 왼쪽 정렬 */
}

td {
  padding: 10px; /* 열 간격 조절 */
  text-align: left; /* 텍스트 왼쪽 정렬 */
}


/* 테이블 전체 스타일 설정 */
table {
  border-collapse: collapse; /* 테이블 경계를 합침 */
  width: 100%; /* 테이블 전체 너비 설정 */
  /* padding: 100% */
}

/* 테이블 경계 선 스타일 설정 */

</style>
