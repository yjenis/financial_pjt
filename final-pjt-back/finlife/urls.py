
from django.contrib import admin
from django.urls import path, include
from . import views

app_name='finlife'
urlpatterns = [
#예금---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('index1', views.index1, name='index1'),
    path('save-deposit-products/', views.save_deposit_products, name='save_deposit_products' ),
    path('deposit-products/', views.deposit_products, name='deposit-products'),
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_products_options, name='deposit_products_options'),
    #최고 금리 기준 높은 순으로 정렬
    path('deposit-products/sort_<int:term>/', views.deposit_products_sort, name='saving_products_sort'),

    #최저 금리 기준 낮은 순으로 정렬
    ###

#적금---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    path('index2', views.index2, name='index2'),
    path('save-saving-products/', views.save_saving_products, name='save_saving_products'),
    path('saving-products/', views.saving_products, name='saving_products'),
    path('saving-product-options/<str:fin_prdt_cd>/', views.saving_products_options, name='saving_products_options'),

    #최고 금리 기준 높은 순으로 정렬
    path('saving-products/sort_12/', views.saving_products_sort_12, name='saving_products_sort_12'),
    path('saving-products/sort_24/', views.saving_products_sort_24, name='saving_products_sort_24'),
    path('saving-products/sort_36/', views.saving_products_sort_36, name='saving_products_sort_36'),

    #최저 금리 기준 낮은 순으로 정렬
    ###

    path('recommend/', views.recommend),
    path('save_all_users_data/', views.save_all_users_data, name='save_all_users_data'),

]
