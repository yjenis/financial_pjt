<template>
  <div class="container">
    <div class="header">
      <img src="@/assets/rich.png" alt="logo" class="img">
      <h3 class="title">커뮤니티</h3>
    </div>

    <div class="row">
      <div class="col"></div> <!-- 왼쪽 여백 -->
      <div class="col-auto"> <!-- 우측에 배치할 요소 -->
        <a class="btn btn-primary" href="/create" role="button" style="background-color:#EF4460; border: none;">CREATE</a>
      </div>
    </div>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import ArticleList from '@/components/ArticleList.vue'

const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>
.container {
  padding-left: 15px;
  padding-right: 15px;
  margin-left: auto;
  margin-right: auto;
  /* max-width: 1200px; 최대 너비 설정으로 중앙 정렬 유지 */
  /* box-sizing: border-box; 패딩 포함 너비 계산 */
}

.header {
  display: flex;
  align-items: center;
}

.title {
  margin-top: 0;
  color: #EF4460;
  font-weight: bold;
  margin-left: 10px; /* 제목과 이미지 사이의 간격을 조정합니다. */
}

.img {
  width: 4.5%;
  height: auto;
}
</style>
