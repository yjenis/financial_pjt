from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from collections import Counter
import json

from django.db.models import Max
from rest_framework.response import Response
import requests
from django.conf import settings
from .serializers import DepositProductsSerializer,DepositOptionsSerializer,SavingProductsSerializer,SavingOptionsSerializer
from .models import DepositProducts,DepositOptions,SavingProducts,SavingOptions
from rest_framework.decorators import api_view

from accounts.models import User
import requests
from .serializers import *
from .models import *
from accounts.serializers import *

# Create your views here.
#예금---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def index1(request):
    API_KEY = settings.FINLIFE_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    return JsonResponse(response['result'])

@api_view(['GET'])
def save_deposit_products(request):
    API_KEY = settings.FINLIFE_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    # return JsonResponse(response)
    for lists in response['result']['baseList']:
        if DepositProducts.objects.filter(fin_prdt_cd=lists['fin_prdt_cd']).exists():
            continue

        # 예금 상품 저장
        save_datas = {
            'fin_prdt_cd':lists['fin_prdt_cd'],
            'kor_co_nm':lists['kor_co_nm'],
            'fin_prdt_nm':lists['fin_prdt_nm'],
            'etc_note':lists['etc_note'],
            'join_deny':lists['join_deny'],
            'join_member':lists['join_member'],
            'join_way':lists['join_way'],
            'spcl_cnd':lists['spcl_cnd'],
            'mtrt_int':lists['mtrt_int'],
            'max_limit':lists['max_limit'],
        }
        product_serializers = DepositProductsSerializer(data=save_datas)
        if product_serializers.is_valid(raise_exception=True):    
            product_serializers.save()

    for lists in response['result']['optionList']:
        fin_prdt_cd = lists['fin_prdt_cd']
        depositproducts = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        if depositproducts:
            save_datas = {
                'fin_prdt_cd': lists['fin_prdt_cd'],
                'intr_rate_type_nm':lists['intr_rate_type_nm'],
                'intr_rate':lists['intr_rate'],
                'intr_rate2':lists['intr_rate2'],
                'save_trm':lists['save_trm']
            }
            if DepositOptions.objects.filter(**save_datas).exists():
                continue
            else:
                option_serializers = DepositOptionsSerializer(data=save_datas)
                if option_serializers.is_valid(raise_exception=True):
                    option_serializers.save(product=depositproducts)
    return Response({'result':'OK'})

# B. 전체 데이터 조회, 수정
@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        depositproducts = DepositProducts.objects.all()
        serializers = DepositProductsSerializer(depositproducts, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Created
        return Response(serializer.errors, status=400)  # Bad Request

# C. 특정 상품의 옵션 리스트 출력
# 주소에 은행 코드 넣으면 기간별로 나옴
@api_view(['GET'])
def deposit_products_options(request, fin_prdt_cd):
    if request.method == 'GET':
        # 상품 코드에 해당하는 옵션 리스트 가져오기
        options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
        # 옵션 리스트를 시리얼라이즈
        serializer = DepositOptionsSerializer(options, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def deposit_products_sort(request, term):
    if request.method == 'GET':
        # 요청된 저축 기간에 맞는 DepositOptions 항목을 찾고 intr_rate2로 내림차순 정렬
        options_months = DepositOptions.objects.filter(save_trm=term).order_by('-intr_rate2')
        
        # DepositProducts를 포함하는 JSON 파일 생성
        response_data = []
        for option in options_months:
            product = DepositProducts.objects.get(fin_prdt_cd=option.fin_prdt_cd)
            product_serializer = DepositProductsSerializer(product)
            option_serializer = DepositOptionsSerializer(option)
            response_data.append({
                'product': product_serializer.data,
                'option': option_serializer.data
            })
        return Response(response_data)

#적금---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def index2(request):
    API_KEY = settings.FINLIFE_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    return JsonResponse(response['result'])

@api_view(['GET'])
def save_saving_products(request):
    API_KEY = settings.FINLIFE_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    # return JsonResponse(response)
    for lists in response['result']['baseList']:
        if SavingProducts.objects.filter(fin_prdt_cd=lists['fin_prdt_cd']).exists():
            continue

        # 예금 상품 저장
        save_datas = {
            'fin_prdt_cd':lists['fin_prdt_cd'],
            'kor_co_nm':lists['kor_co_nm'],
            'fin_prdt_nm':lists['fin_prdt_nm'],
            'etc_note':lists['etc_note'],
            'join_deny':lists['join_deny'],
            'join_member':lists['join_member'],
            'join_way':lists['join_way'],
            'spcl_cnd':lists['spcl_cnd'],
            'mtrt_int':lists['mtrt_int'],
            'max_limit':lists['max_limit'],
        }
        product_serializers = SavingProductsSerializer(data=save_datas)
        if product_serializers.is_valid(raise_exception=True):    
            product_serializers.save()

    for lists in response['result']['optionList']:
        fin_prdt_cd = lists['fin_prdt_cd']
        savingproducts = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        if savingproducts:
            save_datas = {
                'fin_prdt_cd': lists['fin_prdt_cd'],
                'intr_rate_type_nm':lists['intr_rate_type_nm'],
                'intr_rate':lists['intr_rate'],
                'intr_rate2':lists['intr_rate2'],
                'save_trm':lists['save_trm'],
                'rsrv_type_nm':lists['rsrv_type_nm'],
                'rsrv_type':lists['rsrv_type'],
            }
            if SavingOptions.objects.filter(**save_datas).exists():
                continue
            else:
                option_serializers = SavingOptionsSerializer(data=save_datas)
                if option_serializers.is_valid(raise_exception=True):
                    option_serializers.save(product=savingproducts)
    return Response({'result':'OK'})

# B. 전체 데이터 조회, 수정
@api_view(['GET', 'POST'])
def saving_products(request):
    if request.method == 'GET':
        savingproducts = SavingProducts.objects.all()
        serializers = SavingProductsSerializer(savingproducts, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializer = SavingProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)  # Created
        return Response(serializer.errors, status=400)  # Bad Request

# C. 특정 상품의 옵션 리스트 출력
# 주소에 은행 코드 넣으면 기간별로 나옴
@api_view(['GET'])
def saving_products_options(request, fin_prdt_cd):
    if request.method == 'GET':
        # 상품 코드에 해당하는 옵션 리스트 가져오기
        options = SavingOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
        # 옵션 리스트를 시리얼라이즈
        serializer = SavingOptionsSerializer(options, many=True)
        return Response(serializer.data)

# E. 12sort
@api_view(['GET'])
def saving_products_sort_12(request):
    if request.method == 'GET':
        # save_trm이 12개월인 SavingOptions 항목을 찾고 intr_rate2로 내림차순 정렬
        options_months = SavingOptions.objects.filter(save_trm=12).order_by('-intr_rate2')
        
        # SavingProducts를 포함하는 JSON 파일 생성
        response_data = []
        for option in options_months:
            product = SavingProducts.objects.get(fin_prdt_cd=option.fin_prdt_cd)
            product_serializer = SavingProductsSerializer(product)
            option_serializer = SavingOptionsSerializer(option)
            response_data.append({
                'product': product_serializer.data,
                'option': option_serializer.data
            })
        return Response(response_data)

# E. 24sort
@api_view(['GET'])
def saving_products_sort_24(request):
    if request.method == 'GET':
        # save_trm이 24개월인 SavingOptions 항목을 찾고 intr_rate2로 내림차순 정렬
        options_months = SavingOptions.objects.filter(save_trm=24).order_by('-intr_rate2')
        
        # SavingProducts를 포함하는 JSON 파일 생성
        response_data = []
        for option in options_months:
            product = SavingProducts.objects.get(fin_prdt_cd=option.fin_prdt_cd)
            product_serializer = SavingProductsSerializer(product)
            option_serializer = SavingOptionsSerializer(option)
            response_data.append({
                'product': product_serializer.data,
                'option': option_serializer.data
            })
        return Response(response_data)

# E. 36sort
@api_view(['GET'])
def saving_products_sort_36(request):
    if request.method == 'GET':
        # save_trm이 36개월인 SavingOptions 항목을 찾고 intr_rate2로 내림차순 정렬
        options_months = SavingOptions.objects.filter(save_trm=36).order_by('-intr_rate2')
        
        # SavingProducts를 포함하는 JSON 파일 생성
        response_data = []
        for option in options_months:
            product = SavingProducts.objects.get(fin_prdt_cd=option.fin_prdt_cd)
            product_serializer = SavingProductsSerializer(product)
            option_serializer = SavingOptionsSerializer(option)
            response_data.append({
                'product': product_serializer.data,
                'option': option_serializer.data
            })
        return Response(response_data)
    
@api_view(['GET'])
def recommend(request):
    # 모든 사용자의 나이와 가입한 상품명 가져오기
    user_data = User.objects.order_by('age').values('age', 'financial_products')
        
    # 나이를 10 단위로 끊어서 그룹화
    age_groups = {}
    for data in user_data:
        age = data['age']
        age_group = age - (age % 10)
        if age_group not in age_groups:
            age_groups[age_group] = []
        age_groups[age_group].extend(data['financial_products'].split(','))

    # 각 나이 그룹에서 가장 많이 가입된 상품 10개 찾기
    top_products_per_age_group = {}
    for age_group, products in age_groups.items():
        counter = Counter(products)
        top_products = counter.most_common(10)
        top_products_per_age_group[age_group] = top_products

    # JSON 응답 반환
    return Response({'user_data': top_products_per_age_group})

@api_view(['GET'])
def save_all_users_data(request):
    # 모든 사용자의 데이터 가져오기
    users = User.objects.all()

    # 필요한 필드만 선택하여 직렬화
    users_data = []
    for user in users:
        user_data = {
            'age': user.age,
            'money': user.money,
            'salary': user.salary,
            'fin_product': user.financial_products,
        }
        users_data.append(user_data)

    # 홀수 번째 사용자 데이터만 선택
    odd_users_data = users_data[::3]  # 0부터 시작하므로 리스트의 0, 2, 4, ... 번째 요소 선택

    return JsonResponse({'user': odd_users_data})
