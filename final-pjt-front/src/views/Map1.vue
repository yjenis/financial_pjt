<script setup>
import { ref, onMounted } from 'vue'
const { VITE_MAP_API_KEY } = import.meta.env;

const mapContainer = ref(null)

onMounted(() => {
  loadKakaoMap(mapContainer.value)
})

const loadKakaoMap = (container) => {
  const script = document.createElement('script')
  script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=${VITE_MAP_API_KEY}&libraries=services,clusterer,drawing&autoload=false`;
  document.head.appendChild(script)

  script.onload = () => {
    window.kakao.maps.load(() => {
      const options = {
        center: new window.kakao.maps.LatLng(33.450701, 126.570667), // 지도 중심 좌표
        level: 3, // 지도 확대 레벨
        maxLevel: 5, // 지도 축소 제한 레벨
      }

      const mapInstance = new window.kakao.maps.Map(container, options) // 지도 생성

      // 장소 검색 객체를 생성합니다
      const ps = new window.kakao.maps.services.Places(); 

      const placesSearchCB = (data, status, pagination) => {
          if (status === kakao.maps.services.Status.OK) {

              // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
              // LatLngBounds 객체에 좌표를 추가합니다
              var bounds = new kakao.maps.LatLngBounds();

              for (var i=0; i<data.length; i++) {
                  displayMarker(data[i]);    
                  bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
              }       

              // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
              mapInstance.setBounds(bounds);
          } 
      }

      // 지도에 마커를 표시하는 함수입니다
      function displayMarker(place) {
          
          // 마커를 생성하고 지도에 표시합니다
          var marker = new kakao.maps.Marker({
              map: mapInstance,
              position: new kakao.maps.LatLng(place.y, place.x) 
          });

          // 마커에 클릭이벤트를 등록합니다
          kakao.maps.event.addListener(marker, 'click', function() {
              // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
              infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
              infowindow.open(map, marker);
          });
      }

      ps.keywordSearch('이태원 맛집', placesSearchCB); 

      // // 마커가 표시될 위치
      // const markerPosition = new kakao.maps.LatLng(33.450701, 126.570667)

      // // 마커를 생성
      // const marker = new kakao.maps.Marker({
      //   position: markerPosition,
      // })

      // marker.setMap(mapInstance) // 마커 표시
      //marker.setMap(null) // 마커 제거
    })
  }
}
</script>

<template>
  <div class="whole">
    <input v-model="searchKeyword" type="text" placeholder="장소를 검색하세요">
    <button @click="searchPlaces">검색</button>
    <div ref="mapContainer" style="width: 100%; height: 70vh"></div>
  </div>
</template>

<style scoped>
.whole {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  gap: 20px;
}

input, button {
  width: 200px;
  padding: 10px;
  margin: 5px 0;
}

.map-container {
  width: 80%;
  height: 70vh;
}
</style>