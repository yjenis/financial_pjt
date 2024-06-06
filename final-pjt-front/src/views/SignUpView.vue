<template>
  <div class="container">
    <h1 class="title">회원가입</h1>
    <br>
    <form @submit.prevent="signUp" class="form">
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" v-model.trim="username" id="username" class="form-control" placeholder="사용자명을 입력하세요">
      </div>
      <div class="form-group">
        <label for="password1">Password</label>
        <input type="password" v-model.trim="password1" id="password1" class="form-control" placeholder="비밀번호를 입력하세요">
      </div>
      <div class="form-group">
        <label for="password2">Password Confirmation</label>
        <input type="password" v-model.trim="password2" id="password2" class="form-control" placeholder="비밀번호를 다시 입력하세요">
      </div>
      <div class="form-group">
        <label for="email">email</label>
        <input type="text" v-model.trim="email" id="email" class="form-control" placeholder="이메일을 입력하세요">
      </div>
      <div class="form-group">
        <label for="age">나이</label>
        <input type="text" v-model.trim="age" id="age" class="form-control" placeholder="나이를 입력하세요">
      </div>
      <div class="form-group">
        <label for="money">자산</label>
        <input type="text" v-model.trim="money" id="money" class="form-control" placeholder="자산을 입력하세요">
      </div>
      <div class="form-group">
        <label for="salary">연봉</label>
        <input type="text" v-model.trim="salary" id="salary" class="form-control" placeholder="연봉을 입력하세요">
      </div>
      <div class="form-group">
        <label for="birth">생년월일</label>
        <input type="text" v-model.trim="birth" id="birth" class="form-control" placeholder="YYYYMMDD">
      </div>
      <div class="form-group">
        <input type="submit" value="회원가입" class="btn-submit">
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const age = ref(null)
const money = ref(null)
const salary = ref(null)
const email = ref(null)
const birth = ref(null)

const store = useCounterStore()

const signUp = function () {
  if (!username.value || !password1.value || !password2.value || !email.value || !age.value || !money.value || !salary.value) {
    alert('모든 필드를 입력해주세요.');
    return;
  }

  if (password1.value !== password2.value) {
    alert('비밀번호가 일치하지 않습니다.');
    return;
  }

  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    age: age.value,
    money: money.value,
    salary: salary.value,
    email: email.value,
    birth: birth.value,

  }
  store.signUp(payload)
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
