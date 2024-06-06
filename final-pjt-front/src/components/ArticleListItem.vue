<template>
  <tr>
    <td style="width: 10%; text-align: left;">{{ article.id }}</td>
    <td style="width: 80%; text-align: center;">
      <RouterLink 
        :to="{ name: 'DetailView', params: { id: article.id }}"
        class="article-title"
      >
        {{ article.title }}
      </RouterLink>
    </td>      
    <td style="width: 10%; text-align: center;">{{ article.username }}</td>
  </tr>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  article: Object
})
</script>

<style scoped>
.article-title {
  text-decoration: none; /* 링크의 밑줄 제거 */
  color: black; /* 링크 색상 */
}

.article-title:hover {
  color: #0056b3; /* 링크를 호버할 때의 색상 */
  text-decoration: underline; /* 호버 시 밑줄 추가 */
}

.table {
  width: 100%;
  border-collapse: collapse;
}

.table th, .table td {
  padding: 8px;
  /* border: 1px solid #ddd; */
  text-align: left;
}
</style>
