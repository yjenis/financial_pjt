// Pinia의 defineStore 함수를 import 합니다.
import { defineStore } from "pinia";

// "user"라는 이름의 스토어를 정의하고 export 합니다.
export const useUserStore = defineStore("user", {
  // state 함수는 스토어의 상태를 정의합니다.
  state: () => ({
    // 사용자 이름을 저장하는 상태 변수입니다. 초기값은 null입니다.
    username: null,
  }),
  // getters는 스토어의 상태를 기반으로 계산된 값을 반환합니다.
  getters: {
    // isLoggedIn getter는 사용자가 로그인 상태인지 여부를 반환합니다.
    // username이 null이 아니면 true, null이면 false를 반환합니다.
    isLoggedIn: (state) => {
      return state.username != null;
    },
  },
  // actions는 스토어의 상태를 변경하는 메서드를 정의합니다.
  // 현재는 비어 있습니다. 필요에 따라 액션을 추가할 수 있습니다.
  actions: {},
});
