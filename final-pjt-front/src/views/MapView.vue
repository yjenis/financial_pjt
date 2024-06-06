<script setup>
import { ref,onMounted } from 'vue'
const { VITE_MAP_API_KEY } = import.meta.env;
const searchKeyword = ref('');
const places = ref([]);
const mapContainer = ref(null)
const showPlacesList = ref(false); // 변수 정의 및 초기값 설정

const loadKakaoMap = (container) => {
  console.log(searchKeyword.value)
  const script = document.createElement('script')
  script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=${VITE_MAP_API_KEY}&libraries=services,clusterer,drawing&autoload=false`;
  document.head.appendChild(script)

  script.onload = () => {
    window.kakao.maps.load(() => {
      const options = {
        center: new window.kakao.maps.LatLng(37.5038623, 127.0428012), // 지도 중심 좌표
        level: 3, // 지도 확대 레벨
        maxLevel: 10, // 지도 축소 제한 레벨
      }

      const map = new window.kakao.maps.Map(container, options) // 지도 생성

      // 장소 검색 객체를 생성합니다
      const ps = new window.kakao.maps.services.Places(); 

      const placesSearchCB = (data, status, pagination) => {
        if (status === kakao.maps.services.Status.OK) {
          // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
          // LatLngBounds 객체에 좌표를 추가합니다
          const bounds = new kakao.maps.LatLngBounds();
          places.value = []; // 이전 검색 결과 초기화

          for (let i = 0; i < data.length; i++) {
            displayMarker(data[i]);
            bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
            places.value.push({
              id: data[i].id,
              name: data[i].place_name,
              address: data[i].address_name // 주소 정보 추가
            });
          }

          // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
          map.setBounds(bounds);
        }
      }

      const infowindow = new kakao.maps.InfoWindow({zIndex:1});

      // 지도에 마커를 표시하는 함수입니다
      function displayMarker(place) {
        // 마커를 생성하고 지도에 표시합니다
        const marker = new kakao.maps.Marker({
          map: map,
          position: new kakao.maps.LatLng(place.y, place.x)
        });

        // 마커에 클릭이벤트를 등록합니다
        kakao.maps.event.addListener(marker, 'click', function() {
          // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
          infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
          infowindow.open(map, marker);
        });
      }

      ps.keywordSearch(searchKeyword.value, placesSearchCB);
    })
  }
}

const searchPlaces = () => {
  if (!searchKeyword.value.trim()) {
    alert('장소를 입력하세요.');
    return;
  }
  loadKakaoMap(mapContainer.value);
}

const togglePlacesList = () => {
  showPlacesList.value = !showPlacesList.value;
}
onMounted(() => {
  loadKakaoMap(mapContainer.value);
})

</script>

<template>
  <div class="container">
    <div class="header">
      <input v-model="searchKeyword" type="text" placeholder="장소를 검색하세요">
      <button @click="searchPlaces" class="butt">검색</button>
    </div>

    <p class="discrip">※ 지역명과 은행명을 조합하여 검색하세요 ex)강남역 우리은행, 부산 국민은행</p>
    
    <div class="content">
      <div ref="mapContainer" class="mapContainer">

        <div class="search-list" >
          <button @click="togglePlacesList" class="toggle-button">검색 목록</button>
          <ul  class="placesList" v-show="showPlacesList"> <!--v-show="showPlacesList"-->
            <li v-for="(place, index) in places" :key="place.id">
              <strong>{{ index + 1 }}. {{ place.name }}</strong><br>
              <small>{{ place.address }}</small>
            </li>
          </ul>
        </div>  

      </div> 

    </div>

  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 90vh;
}

.header {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding: 20px;
  background-color: #ffffff;
}

.header input[type="text"] {
  width: 60%;
  max-width: 600px;
  padding: 12px 20px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 25px;
  outline: none;
  transition: box-shadow 0.3s ease-in-out;
}

.header input[type="text"]:focus {
  box-shadow: 0 0 8px rgba(0, 0, 0, 0.1);
}

.header button {
  padding: 12px 40px;
  font-size: 16px;
  border: none;
  border-radius: 25px;
  background-color: #EF4460;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

.header button:hover {
  background-color: #EF4460;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.discrip {
  margin: 0;
  font-size: 14px;
  padding: 10px;
}

.content {
  position: relative;
  width: 100%;
}

.mapContainer {
  position: relative;
  width: 100%;
  height: 70vh;
  background-color: rgba(255, 255, 255, 0.7);
  border-radius: 2%;
}

.search-list {
  position: absolute;
  top: 10px; /* 상단 여백 설정 */
  left: 10px; /* 왼쪽 여백 설정 */
  z-index: 10; /* 다른 요소 위에 표시되도록 설정 */
}



.placesList {
  list-style-type: none;
  padding: 10px;
  margin: 0;
  background-color: white;
  border: 0.1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 10px;
  max-height: calc(70vh - 60px);
  /* overflow-y: auto; */
}

.toggle-button {
  min-width: 120px;
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  border-radius: 25px;
  background-color: #EF4460;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
}

.toggle-button:hover {
  background-color: #FF6B82;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}
</style>