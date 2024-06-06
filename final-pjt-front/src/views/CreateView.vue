<template>
  <div class="container">
    <h1 class="title">게시글 작성</h1>
    <br>
    <form @submit.prevent="createArticle" class="form">
      <div class="form-group">
        <label for="title">제목</label>
        <input type="text" v-model.trim="title" id="title" class="form-control" placeholder="제목을 입력하세요">
      </div>
      <div class="form-group">
        <label for="content">내용</label>
        <textarea v-model.trim="content" id="content" class="form-control" rows="10" placeholder="내용을 입력하세요"></textarea>
      </div>
      <div class="form-group">
        <input type="submit" value="작성하기" class="btn-submit">
      </div>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios'
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useCounterStore()
const title = ref(null)
const content = ref(null)
const router = useRouter()

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((response) => {
      router.push({ name: 'ArticleView' })
    })
    .catch((error) => {
      console.log(error)
    })
}
</script>

<style scoped>
.container {
  padding-left: 15px;
  padding-right: 15px;
  margin-left: auto;
  margin-right: auto;
  background-color: #ffffff;
  border-radius: 8px;
}

.title {
  margin-top: 0;
  color: #EF4460;
  font-weight: bold;
  margin-bottom: 20px;
  font-size: 28px;
}

.form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
  color: #555;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.form-control:focus {
  border-color: #EF4460;
  box-shadow: 0 0 4px rgba(0, 123, 255, 0.2);
}

.btn-submit {
  padding: 12px 20px;
  background-color: #EF4460;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-submit:hover {
  background-color: #EF4460;
}
</style>
