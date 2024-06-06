from django.urls import path
from . import views


urlpatterns = [
    path('articles/', views.article_list, name='articles'),
    path('articles/<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/comments/', views.comment_list),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_detail),
]
