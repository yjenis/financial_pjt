<template>
  <div class="container">
    <div class="content">
      <div class="image-container">
        <div class="image-left">
          <img src="@/assets/main.png" alt="logo" class="main">
          <a class="btn btn-primary" href="/Signup" role="button">회원가입하고 부자되기</a>
        </div>
        <img src="@/assets/illu.png" alt="logo" class="illu">
      </div>
    </div>

    <button id="chatbot" class="btn-chatbot" @click="toggleChatbot">
      <img src="@/assets/richbot.webp" alt="챗봇 열기" class="chatbot-icon" :class="{ active: isChatbotVisible }">
    </button>
    <div v-show="isChatbotVisible" class="chatbot-container">
      <iframe
        src="https://www.chatbase.co/chatbot-iframe/-lljE9xpFadkkOdFE5Vm2"
        title="REACHRICH"
        class="chatbot-iframe"
        frameborder="0"
      ></iframe>
    </div>

    <footer class="footer">
      <div>
        <p>본 사이트의 콘텐츠는 저작권법의 보호를 받는 바 무단 전재, 복사, 배포 등을 금합니다.</p>
        <p>Copyright ©리치리치 All Rights Reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const isChatbotVisible = ref(false);

const toggleChatbot = () => {
  isChatbotVisible.value = !isChatbotVisible.value;
};
</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html, body {
  width: 100%;
  height: 100%;
  overflow: hidden; /* 세로 스크롤 제거 */
}

.container {
  display: flex;
  flex-direction: column;
  height: 70vh;
  overflow: hidden; /* 세로 스크롤 제거 */
}

.content {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 20px;
  /* overflow: hidden; 필요에 따라 스크롤 제거 */
}

.image-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px; /* 필요한 경우 조정 */
  overflow: hidden;
}

.image-left {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-right: 20px;
}

.main {
  width: 400px; /* 원하는 크기로 설정 */
  height: auto;
}

.illu {
  width: 400px; /* 원하는 크기로 설정 */
  height: auto;
}

.btn-primary {
  margin-top: 20px; /* 버튼과 이미지 사이의 간격 조정 */
  width: 400px;
  height: 40px;
  background-color: #EF4460;
  border-color: #EF4460;
  color: white;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
  text-decoration: none;
}

.btn-primary:link,
.btn-primary:visited,
.btn-primary:hover,
.btn-primary:focus,
.btn-primary:active {
  background-color: #EF4460;
  border-color: #EF4460;
  color: white;
}

/* 챗봇 버튼 스타일 */
.btn-chatbot {
  position: fixed;
  bottom: 120px;
  right: 30px;
  padding: 0;
  background-color: transparent;
  border: none;
  cursor: pointer;
  z-index: 1000;
}

.chatbot-icon {
  width: 150px; /* 이미지 크기 조정 */
  height: 150px; /* 이미지 크기 조정 */
  transition: transform 0.3s ease; /* 부드러운 애니메이션 효과 */
}

.btn-chatbot:hover .chatbot-icon,
.btn-chatbot:focus .chatbot-icon,
.chatbot-icon.active {
  transform: translateY(20px); /* 아이콘을 위로 이동 */
}

.chatbot-container {
  position: fixed;
  bottom: 255px;
  right: 20px;
  width: 650px;
  height: 680px;
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  z-index: 999;
}

.chatbot-iframe {
  width: 100%;
  height: 100%;
  border: none;
  border-radius: 10px;
}

.footer {
  background-color: #FCF9F9;
  padding: 20px;
  text-align: center;
  width: 100%;
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
}
</style>
