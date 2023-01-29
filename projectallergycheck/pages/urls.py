from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views # . 은 '현재 디렉토리에서' 라는 의미

#pages url.py
app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    #about url
    path('about/qrCode/', views.about_qrcode, name='about_qrcode'),
    path('about/test/', views.about_test, name='about_test'),
    path('about/user/', views.about_user, name='about_user'),

    #recommend url
    path('recommend/qrCode/', views.recommend_all_recommend_list, name='recommend_all_recommend_list'),
    path('recommend/test/', views.recommend_nutrient_recommend, name='recommend_nutrient_recommend'),
    path('recommend/user/', views.recommend_user_recommend, name='recommend_user_recommend'),
]