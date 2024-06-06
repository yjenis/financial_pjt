<template>
  <div>
    <!-- <h4>Article List</h4> -->
    <table class="table">
      <thead>
        <tr>
          <th style="width: 10%;">No</th>
          <th style="width: 80%; text-align: center;">Title</th>
          <th style="width: 10%;">Posted By</th>
        </tr>
      </thead>
      <tbody>
        <ArticleListItem 
          v-for="article in store.articles"
          :key="article.id"
          :article="article"
        />
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { useCounterStore } from '@/stores/counter'
import ArticleListItem from '@/components/ArticleListItem.vue'

const store = useCounterStore()
</script>

<style scoped>
thead{
  font-size: 18px;
}
tbody{
  font-size: 16px;
}
</style>
