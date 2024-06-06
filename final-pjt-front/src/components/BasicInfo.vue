<!-- bacis info.vue -->
<template>
  <div class="profile-container">
    <h1 class="profile-title">Profile</h1>
    <img src="@/assets/profile.png" alt="profile" class="profile-img">
    <br>
    <div class="profile-info">
      <!-- <p><strong>이름:</strong> 김철수</p> -->
      <p><strong>이름:</strong> {{ userInfo.username }}</p>
      <p><strong>e-mail:</strong> {{ userInfo.email }}</p>
      
      <p>
        <strong>나이:</strong> 
        <span v-if="!editingAge">{{ age }}</span>
        <input v-else type="number" v-model="newAge" class="input-field">
        <button class="edit-button" @click="toggleEditAge">
          <img v-if="!editingAge" src="@/assets/pencilbutton.png" alt="Edit" class="button-icon">
          <span v-else>저장</span>
        </button>
      </p>
      <p>
        <strong>자산:</strong> 
        <span v-if="!editingAssets">{{ userInfo.money }}</span>
        <input v-else type="number" v-model="newAssets" class="input-field">
        <button class="edit-button" @click="toggleEditAssets">
          <img v-if="!editingAssets" src="@/assets/pencilbutton.png" alt="Edit" class="button-icon">
          <span v-else>저장</span>
        </button>
      </p>
      <p>
        <strong>소득:</strong> 
        <span v-if="!editingIncome">{{ userInfo.salary }}</span>
        <input v-else type="number" v-model="newIncome" class="input-field">
        <button class="edit-button" @click="toggleEditIncome">
          <img v-if="!editingIncome" src="@/assets/pencilbutton.png" alt="Edit" class="button-icon">
          <span v-else>저장</span>
        </button>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();
const userInfo = store.userInfo;

const birthYear = userInfo.birth.slice(0, 4);
const birthMonth = userInfo.birth.slice(4, 6);
const birthDate = userInfo.birth.slice(6, 8);

// 생일로 나이 계산
const calculateAge = (birthYear, birthMonth, birthDate) => {
  const today = new Date();
  const year = today.getFullYear();
  const month = today.getMonth() + 1;
  const day = today.getDate();

  let age = year - birthYear;
    if (month < birthMonth || (month === birthMonth && day < birthDate)) {
        age--;
    }  
  return age;
};

const age = ref(calculateAge(parseInt(birthYear), parseInt(birthMonth), parseInt(birthDate)));


const assets = ref(50000);
const newAssets = ref(null);
const editingAssets = ref(false);

const income = ref(3000);
const newIncome = ref(null);
const editingIncome = ref(false);

const toggleEditAge = () => {
  if (editingAge.value) {
    age.value = newAge.value;
  }
  editingAge.value = !editingAge.value;
};

const toggleEditAssets = () => {
  if (editingAssets.value) {
    assets.value = newAssets.value;
  }
  editingAssets.value = !editingAssets.value;
};

const toggleEditIncome = () => {
  if (editingIncome.value) {
    income.value = newIncome.value;
  }
  editingIncome.value = !editingIncome.value;
};
</script>

<style scoped>
.profile-container {
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  margin: 40px auto;
  text-align: center;
}

.profile-img{
  width: 300px;
  height: auto;
}

.profile-title {
  font-weight: bold;
  font-size: 2em;
  color: #EF4460;
  margin-bottom: 20px;
}

.profile-info p {
  font-size: 1.2em;
  color: #555;
  margin: 5px 0;
}

.profile-info p strong {
  color: #333;
}

.input-field {
  width: 70px; /* 원하는 고정 길이 설정 */
  /* display: inline-block;
  box-sizing: border-box; */
  padding: 1px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-left: 10px;
}

/* 숫자 입력 화살표 숨기기 */
input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

input[type="number"] {
  -moz-appearance: textfield; /* Firefox에서 화살표 숨기기 */
}

.edit-button {
  /* background-color: lightcoral;  */
  background-color: #f9f9f9;
  border: none;
  color: black;
  padding: 5px 7px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 12px;
  margin: 2px 2px;
  cursor: pointer;
  border-radius: 10px;
  transition: background-color 0.3s ease;
}

.edit-button:hover {
  /* background-color: lightcoral; */
}

.button-icon {
  width: 16px;
  height: 16px;
}
</style>