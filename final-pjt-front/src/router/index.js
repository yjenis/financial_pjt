import { createRouter, createWebHistory } from 'vue-router';
import ArticleView from '@/views/ArticleView.vue';
import HomeView from '@/views/HomeView.vue';
import DetailView from '@/views/DetailView.vue';
import CreateView from '@/views/CreateView.vue';
import SignUpView from '@/views/SignUpView.vue';
import LogInView from '@/views/LogInView.vue';
import FinanceView from '@/views/FinanceView.vue';
import MapView from '@/views/MapView.vue';
import Deposit from '@/components/Deposit.vue';
import Saving from '@/components/Saving.vue';
import ExchangeView from '@/views/ExchangeView.vue';
import MyPageView from '@/views/MyPageView.vue';
import DepositDetail from '@/components/DepositDetail.vue';
import SavingDetail from '@/components/SavingDetail.vue';

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView
  },
  {
    path:'/my-page',
    name:'Mypage',
    component: MyPageView,
  },
  {
    path: '/articles',
    name: 'ArticleView',
    component: ArticleView
  },
  {
    path: '/articles/:id',
    name: 'DetailView',
    component: DetailView
  },
  {
    path: '/create',
    name: 'CreateView',
    component: CreateView
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  {
    path: '/login',
    name: 'LogInView',
    component: LogInView
  },
  {
    path:'/finance',
    name:'FinanceView',
    component:FinanceView
  },
  {
    path:'/finance/deposit-products',
    name:'Deposit',
    component:Deposit
  },
  {
    path:'/map',
    name:'Map',
    component:MapView
  },
  {
    path:'/finance/saving-products',
    name:'Saving',
    component:Saving
  },
  {
    path: '/finance/deposit-products/detail/:id',
    name: 'DepositDetail',
    component: DepositDetail,
    props: true // 라우트 파라미터를 컴포넌트의 props로 전달
  },
  {
    path: '/finance/saving-products/detail/:id',
    name: 'SavingDetail',
    component: SavingDetail,
    props: true // 라우트 파라미터를 컴포넌트의 props로 전달
  },
  {
    path:'/exchange',
    name:'Exchange',
    component:ExchangeView
  }
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
});

import { useCounterStore } from '@/stores/counter';

router.beforeEach((to, from) => {
  const store = useCounterStore();
  // 인증되지 않은 사용자는 메인 페이지에 접근할 수 없음
  if (to.name === 'ArticleView' && store.isLogin === false) {
    window.alert('로그인이 필요합니다.');
    return { name: 'LogInView' };
  }

  // 인증된 사용자는 회원가입과 로그인 페이지에 접근할 수 없음
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && store.isLogin === true) {
    window.alert('이미 로그인 했습니다.');
    return { name: 'ArticleView' };
  }
});

export default router;
