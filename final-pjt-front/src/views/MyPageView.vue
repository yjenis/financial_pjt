<template>
  <div class="container">
    <div class="header">
      <img src="@/assets/rich.png" alt="logo" class="img">
      <h3 class="title">{{ userInfo.username }}님의 마이페이지</h3>
    </div>
    <br>
    <ul class="nav nav-tabs">
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeTab === 'basicInfo' }" @click="activeTab = 'basicInfo'" href="#">기본 정보</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" :class="{ active: activeTab === 'recommend' }" @click="activeTab = 'recommend'" href="#">추천 상품</a>
      </li>
    </ul>

    <div id="tabContent">
      <component :is="currentComponent"></component>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, markRaw } from 'vue';
import { useCounterStore } from '@/stores/counter';
import BasicInfo from '@/components/BasicInfo.vue';
import Recommend from '@/components/Recommend.vue';

const store = useCounterStore();
const userInfo = store.userInfo;

const activeTab = ref('basicInfo');
const currentComponent = ref(markRaw(BasicInfo));

watch(activeTab, (newTab) => {
  if (newTab === 'basicInfo') {
    currentComponent.value = markRaw(BasicInfo);
  } else if (newTab === 'recommend') {
    currentComponent.value = markRaw(Recommend);
  }
});
</script>

<style scoped>
.container {
  padding-left: 15px;
  padding-right: 15px;
  padding-bottom: 0px;
  margin-left: auto;
  margin-right: auto;
}

#tabContent {
  width: 100%;
}

.header {
  display: flex;
  align-items: center;
}

.title {
  margin-top: 0;
  color: #EF4460;
  font-weight: bold;
  margin-left: 10px;
}

.img {
  width: 4.5%;
  height: auto;
}

.nav-tabs {
  display: flex;
  justify-content: flex-start;
  list-style: none;
  padding: 0;
  border-bottom: 1px solid #ddd;
  margin-bottom: 15px;
}

.nav-item {
  margin-right: 10px;
}

.nav-link {
  text-decoration: none;
  padding: 10px;
  color: black;
  cursor: pointer;
}

.nav-link:hover {
  color: black; /* 마우스 오버 시에도 글자색을 검은색으로 유지 */
}

.nav-link.active {
  color: #EF4460;
  font-weight: bold;
}
</style>
