<template>
  <div class="container">
    <div v-if="article">
      <h2 v-if="!isEditing">{{ article.title }}</h2>
      <input v-else type="text" v-model="articleTitle" class="form-control" />

      <hr>
      <br>

      <h4 v-if="!isEditing">{{ article.content }}</h4>
      <textarea v-else v-model="articleContent" class="form-control"></textarea>

      <br><br>
      <p>작성 시간: {{ formattedCreatedAt }}</p>
      <p>수정 시간: {{ formattedUpdatedAt }}</p>
      <div class="btnz">
        <div v-if="!isEditing">
          <button class="btn-delete" @click.prevent="deleteArticle">삭제</button>
          <button class="btn-update" @click.prevent="startEditing">수정</button>
        </div>
        <div v-else>
          <button class="btn-save" @click.prevent="saveArticle">저장</button>
          <button class="btn-cancel" @click.prevent="cancelEditing">취소</button>
        </div>
      </div>
    </div>

    <div class="comments-section" v-if="article">
      <div class="comments-lst">
        <h4 style="font-weight: bolder">댓글</h4>
        <ul>
          <li v-for="comment in comments" :key="comment.id">
            <p>{{ comment.content }}</p>
            <small>작성 시간: {{ new Date(comment.created_at).toLocaleString('ko-KR') }}</small>
            <button class="btn-delete-comment" @click.prevent="deleteComment(comment.id)">삭제</button>
            <hr>
          </li>
        </ul>
      </div>

      <br>
      <form @submit.prevent="postComment" class="form">
        <div class="form-group">
          <label for="new-comment">댓글 작성</label>
          <textarea v-model="newComment" id="new-comment" class="form-control" placeholder="댓글을 입력하세요"></textarea>
        </div>
        <div class="form-group">
          <input type="submit" value="댓글 작성" class="btn-submit">
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios'
import { onMounted, ref, computed } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute, useRouter } from 'vue-router'

const store = useCounterStore()
const route = useRoute()
const router = useRouter()
const article = ref(null)
const comments = ref([])
const newComment = ref('')
const isEditing = ref(false)
const articleTitle = ref('')
const articleContent = ref('')

onMounted(() => {
  fetchArticle()
  fetchComments()
})

const fetchArticle = () => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/articles/${route.params.id}/`
  })
    .then((response) => {
      article.value = response.data
      articleTitle.value = article.value.title
      articleContent.value = article.value.content
    })
    .catch((error) => {
      console.log(error)
    })
}

const fetchComments = () => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/${route.params.id}/comments/`
  })
    .then((response) => {
      comments.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
}

const postComment = () => {
  if (!newComment.value.trim()) {
    alert('댓글을 입력하세요.')
    return
  }

  axios({
    method: 'post',
    url: `http://127.0.0.1:8000/api/v1/${route.params.id}/comments/`,
    headers: {
      Authorization: `Token ${store.token}`
  
    },
    data: {
      content: newComment.value
    }
  })
    .then((response) => {
      comments.value.push(response.data)
      newComment.value = ''
    })
    .catch((error) => {
      console.log(error)
    })
}

const deleteComment = (commentId) => {
  const answer = window.confirm('댓글을 삭제하시겠습니까?')

  if (answer) {
    axios({
      method: 'delete',
      
      url: `http://127.0.0.1:8000/api/v1/${route.params.id}/comments/${commentId}`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) => {
        comments.value = comments.value.filter(comment => comment.id !== commentId)
      })
      .catch((err) => {
        console.log(err)
      })
  }
}

const deleteArticle = function () {
  const answer = window.confirm('삭제하시겠습니까?')

  if (answer) {
    axios({
      method: 'delete',
      url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then((res) => {
        router.push({ name: 'ArticleView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }
}

const startEditing = function () {
  isEditing.value = true
}

const cancelEditing = function () {
  isEditing.value = false
  articleTitle.value = article.value.title
  articleContent.value = article.value.content
}

const saveArticle = function () {
  axios({
    method: 'put',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`
    },
    data: {
      title: articleTitle.value,
      content: articleContent.value
    }
  })
    .then((res) => {
      article.value = res.data
      isEditing.value = false
    })
    .catch((err) => {
      console.log(err)
    })
}

const formattedCreatedAt = computed(() => {
  if (!article.value || !article.value.created_at) return ''
  const date = new Date(article.value.created_at)
  return date.toLocaleString('ko-KR', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  })
})

const formattedUpdatedAt = computed(() => {
  if (!article.value || !article.value.updated_at) return ''
  const date = new Date(article.value.updated_at)
  return date.toLocaleString('ko-KR', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit'
  })
})
</script>

<style scoped>
.container {
  padding-left: 15px;
  padding-right: 15px;
  margin-left: auto;
  margin-right: auto;
  font-family: Arial, sans-serif;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.btnz {
  display: flex;
  gap: 10px;
}

button {
  padding: 5px 10px;
  border: none;
  cursor: pointer;
  font-size: 15px;
  border-radius: 10px;
}

.btn-delete {
  background-color: white;
  color: rgb(90, 88, 88);
  border: 0.7px solid grey;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.btn-update {
  background-color: white;
  color: rgb(90, 88, 88);
  border: 0.7px solid grey;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin: 0px 0px 0px 10px;
}

.btn-save {
  background-color: white;
  color: rgb(90, 88, 88);
  border: 0.7px solid grey;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.btn-cancel {
  background-color: white;
  color: rgb(90, 88, 88);
  border: 0.7px solid grey;
  border-radius: 5px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  margin: 0px 0px 0px 10px;
}

.comments-section {
  margin-top: 100px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 7px;
}

/* .comments-lst{
  margin-top: 100px;

  padding: 20px;
  border: 1px solid #ddd
} */

.comments-section h3 {
  font-weight: bold;
}

.comments-section ul {
  list-style: none;
  padding: 0;
}

.comments-section li {
  margin-bottom: 20px;
}

.comments-section .form-group {
  margin-bottom: 15px;
}

.comments-section .form-group label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.comments-section .form-group textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

.comments-section .btn-submit {
  padding: 8px 11px;
  font-size: 14px;
  background-color: #EF4460;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.comments-section .btn-submit:hover {
  background-color: #EF4460;
}
</style>
