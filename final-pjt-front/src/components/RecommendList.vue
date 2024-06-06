<template>
  <div calss="table-container">
   <table class="recommend-table">
     <tr>
       <th style="width: 50%;">{{ recommend[0] }}</th>
       <th style="width: 50%;">{{ recommend[1] }}</th>
     </tr>
     <!-- 여기에 각 행을 반복하여 추가 -->
   </table>
 </div> 
</template>

<script setup>
defineProps({
 recommend: Object
});
</script>

<style scoped>
.table-container {
 background-color: #fff;
 border-radius: 10px;
 padding: 20px;
 box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
 margin: 20px 0;
}

.recommend-table {
 width: 100%;
 border-collapse: collapse;
}

/* .recommend-table th, .recommend-table td {
  border: 1px solid #ddd; 
  padding: 8px;
 
} */
</style>
