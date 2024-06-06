<template>
  <div calss="table-container">
    <table>
      <tr>
        <th style="width: 30%;">{{ deposit.kor_co_nm }}</th>
        <th style="width: 40%;">
        <RouterLink :to="{ name: 'DepositDetail', params: { id: deposit.id } }">
          
          {{ deposit.fin_prdt_nm }}
        </RouterLink>
        </th>   
        <th style="width: 30%;">{{ none }}</th>

      </tr>
      
      <!-- 여기에 각 행을 반복하여 추가 -->
    </table>
    <hr>
  </div>  
</template>

<script setup>
defineProps({
  deposit:Object
})

</script>

<style scoped>
/* .table-container { */
  /* overflow-y: hidden; 수평 스크롤을 숨기기 위한 설정 */
  /* height: 100%; 부모 요소의 너비 설정 */
/* } */
/* .table-container {
  overflow-y: scroll
} */

th {
  padding: 10px; /* 열 간격 조절 */

  text-align: center;
}

td {
  padding: 10px; /* 열 간격 조절 */
  text-align: center;/* 텍스트 왼쪽 정렬 */
}


/* 테이블 전체 스타일 설정 */
table {
  overflow-y: hidden;
  border-collapse: collapse; /* 테이블 경계를 합침 */
  width: 100%; /* 테이블 전체 너비 설정 */
  /* table-layout: fixed; */
  /* padding: 100% */
}

/* 테이블 경계 선 스타일 설정 */

</style>