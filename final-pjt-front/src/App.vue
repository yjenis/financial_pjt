<template>
  <div id="app"> 
    <header>
      <nav class="nav-bar">
        <a href="/" class="logo">
          <img src="@/assets/Logo.png" alt="logo">
        </a>
        <div class="navbar-container">
          <ul class="nav nav-underline">
            <li class="nav-item">
              <a class="nav-link" href="/finance">금융상품</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/map">은행 찾기</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/exchange">환율 계산기</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/articles">커뮤니티</a>
            </li>
          </ul>
        </div>
        <div class="user">
          <div v-if="!isLogin">
            <RouterLink :to="{ name: 'SignUpView' }">
              <button class="btn">회원가입</button>
            </RouterLink>
            <RouterLink :to="{ name: 'LogInView' }">
              <button class="btn">로그인</button>
            </RouterLink>
          </div>
          <div v-else>
            <button @click.prevent="store.logOut" class="btn">로그아웃</button>
            <RouterLink :to="{ name: 'Mypage' }">
              <button class="btn">마이페이지</button>
            </RouterLink>
          </div>
        </div>
      </nav>
    </header>
    <RouterView class="router"/>
  </div>
</template>

<script setup>
import { computed } from 'vue';
import { useCounterStore } from './stores/counter';
import { useUserStore } from './stores/user';

const store = useCounterStore();
const storeU = useUserStore();
const isLogin = computed(() => store.isLogin);
const isLoggedIn = computed(() => storeU.isLoggedIn);
</script>

<style scoped>
#app {
  overflow: hidden;
}

html, body, #app {
  height: 100%;
  margin: 0;
  display: flex;
  flex-direction: column;
}

.nav-bar {
  padding: 20px;
  display: flex;
  justify-content: space-between;
  font-size: 1rem;
  color: black;
  text-decoration: none;
  font-weight: bold;
}

.nav.nav-underline .nav-link {
  color: gray;
}

.nav.nav-underline .nav-link:hover {
  color: #EF4460;
}

.left, .user {
  display: flex;
  gap: 10px;
  align-items: flex-end;
  margin-left: auto;
}

.router-link {
  color: inherit;
  text-decoration: none;
  cursor: pointer;
  margin-right: 10px;
}

.container {
  width: 100vw;
}

.navbar-container {
  position: absolute;
  top: 2%;
  left: 50%;
  transform: translateX(-50%);
}

.nav-item {
  margin-right: 15px;
  font-size: 20px;
  color: black;
}

.nav-link {
  color: black;
}

.user .btn {
  background-color: #EF4460;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 120px;
  height: auto;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  margin-right: 10px;
  border-radius: 5px;
  font-size: 16px;
}

.user .btn:hover {
  background-color: #d7374f;
}

.logo {
  margin-right: 1px;
}

.logo img {
  width: 45%;
  height: auto;
}

.router {
  padding: 5%;
}
</style>
