from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views # . 은 '현재 디렉토리에서' 라는 의미

#accounts url.py
app_name = 'accounts'
urlpatterns = [
    #accounts url
    #path('accounts/signup', views.accounts_signup, name='accounts_signup'),
    
    path('badfood/', views.accounts_badfood, name='accounts_badfood'),
    path('bodyInfo/', views.accounts_bodyInfo, name='accounts_bodyInfo'),
    path('goodfood/', views.accounts_goodfood, name='accounts_goodfood'),
    path('mypage/', views.accounts_mypage, name='accounts_mypage'),
    path('nickname/', views.accounts_nickname, name='accounts_nickname'),
    path('warningfood/', views.accounts_warningfood, name='accounts_warningfood'),    
    
]