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
        center: new window.kakao.maps.LatLng(37.566826, 126.9786567), // 지도 중심 좌표
        level: 3, // 지도 확대 레벨
        maxLevel: 5, // 지도 축소 제한 레벨
      }

      const map = new window.kakao.maps.Map(container, options) // 지도 생성
      var infowindow = new kakao.maps.InfoWindow({zIndex:1});

        // 장소 검색 객체를 생성합니다
        var ps = new kakao.maps.services.Places(map); 

        // 카테고리로 은행을 검색합니다
        ps.categorySearch('BK9', placesSearchCB, {useMapBounds:true}); 

        // 키워드 검색 완료 시 호출되는 콜백함수 입니다
        function placesSearchCB (data, status, pagination) {
            if (status === kakao.maps.services.Status.OK) {
                for (var i=0; i<data.length; i++) {
                    displayMarker(data[i]);    
                }       
            }
        }

        // 지도에 마커를 표시하는 함수입니다
        function displayMarker(place) {
            // 마커를 생성하고 지도에 표시합니다
            var marker = new kakao.maps.Marker({
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
    })
  }
}
</script>

<template>
  <div>
  <!-- <input v-model="searchKeyword" type="text" placeholder="장소를 검색하세요">
  <button @click="searchPlaces">검색</button> -->
  <div ref="mapContainer" style="width: 100%; height: 70vh"></div>
  </div>
</template>

<style scoped>
</style>