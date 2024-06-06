// counter.js

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const finance=ref([])
  ////////////////////// 예금
  const deposit=ref([])
  const saving=ref([])
  // ///////////////// 환율
  const exchange=ref([])

  const userInfo = ref([])



  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  const router = useRouter()

  const getMoney=function(){
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/finlife/'
    })
    .then(res=>{
      // console.log(res.data)
      finance.value=res.data
      // console.log(finance.value)
    })
    .catch(error=>{
      console.log(error)
    })
  }


  ////////////////////// 예금
  // 전체 목록
  const depositInfo=function(){
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/finlife/deposit-products/'
    })
    .then(res=>{
      // console.log(res.data)
      deposit.value=res.data
      // console.log(deposit.value)
    })
    .catch(error=>{
      console.log(error)
    })
  }



  // //////////////////적금
  const savingInfo=function(){
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/finlife/saving-products/'
    })
    .then(res=>{
      // console.log(res.data)
      saving.value=res.data
      // console.log(deposit.value)
    })
    .catch(error=>{
      console.log(error)
    })
  }


  // /////////////////환율 데이터
  const exchangeInfo=function(){
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/exchange/'
    })
    .then(res=>{
      // console.log(res.data)
      exchange.value=res.data
      // console.log(deposit.value)
    })
    .catch(error=>{
      console.log(error)
    })
  }
  
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then(response => {
        articles.value = response.data
      })
      .catch(error => {
        console.log(error)
      })
  }

  const signUp = function (payload) {
    // 1. 사용자 입력 데이터를 받아
    // const username = payload.username
    // const password1 = payload.password1
    // const password2 = payload.password2
    const { username, password1, password2, age , money, salary, email, birth } = payload

    // 2. axios로 django에 요청을 보냄
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        // username: username,
        // password1: password1,
        // password2: password2
        username, password1, password2, age, money, salary, email, birth
      }
    })
     .then((response) => {
       console.log('회원가입 성공!')
       const password = password1
       logIn({ username, password })
     })
     .catch((error) => {
       console.log(error)
     })
  }

  const logIn = function (payload) {
    // 1. 사용자 입력 데이터를 받아
    const { username, password } = payload
    // 2. axios로 django에 요청을 보냄
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        // console.log('로그인 성공!')
        // console.log(response)
        // console.log(response.data.key)
        // 3. 로그인 성공 후 응답 받은 토큰을 저장
        token.value = response.data.key
        getUserInfo(username)
        router.push({ name : 'ArticleView' })
      })
      .catch((error) => {
        console.log(error)
      })
  }

  const getUserInfo = function (username) {
    axios({
      method: 'get',
      url: `${API_URL}/users/${username}/info/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        userInfo.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const logOut = function () {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/accounts/logout/',
    })
      .then((res) => {
        token.value = null
        userInfo.value = []
        router.push({ name: 'HomeView' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { articles, API_URL, userInfo, getUserInfo, getArticles, signUp, logIn, token, isLogin, 
    getMoney, finance, deposit, depositInfo, saving, savingInfo, exchange, exchangeInfo, logOut}
}, { persist: true })