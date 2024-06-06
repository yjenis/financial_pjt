<template>
  <div class="container">
    <h1 class="title">로그인</h1>
    <br>
    <form @submit.prevent="logIn" class="form">
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" v-model.trim="username" id="username" class="form-control" placeholder="사용자명을 입력하세요">
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input type="password" v-model.trim="password" id="password" class="form-control" placeholder="비밀번호를 입력하세요">
      </div>
      <div class="form-group">
        <input type="submit" value="로그인" class="btn-submit">
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const username = ref(null)
const password = ref(null)
const store = useCounterStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style scoped>
.container {
  max-width: 400px;
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
  background-color: #d6374b;
}
</style>
