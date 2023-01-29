"""projectallergycheck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),

    #about url
    path('about/edit', views.about_edit, name='about_edit'),
    path('about/home', views.about_home, name='about_home'),
    path('about/list', views.about_list, name='about_list'),
    path('about/qrCode', views.about_qrcode, name='about_qrcode'),
    path('about/test', views.about_test, name='about_test'),
    path('about/user', views.about_user, name='about_user'),

    #login url
    #path('login/index', views.login_index, name='login_index'),

    #mypage url
    path('mypage/badfood', views.mypage_badfood, name='mypage_badfood'),
    path('mypage/bodyInfo', views.mypage_bodyInfo, name='mypage_bodyInfo'),
    path('mypage/goodfood', views.mypage_goodfood, name='mypage_goodfood'),
    path('mypage/mypage', views.mypage_mypage, name='mypage_mypage'),
    path('mypage/nickname', views.mypage_nickname, name='mypage_nickname'),
    path('mypage/warningfood', views.mypage_warningfood, name='mypage_warningfood'),

    #recommend url
    path('recommend/all_recommend_list', views.recommend_all_recommend_list, name='recommend_all_recommend_list'),
    path('recommend/nutrient_recommend', views.recommend_nutrient_recommend, name='recommend_nutrient_recommend'),
    path('recommend/user_recommend', views.recommend_user_recommend, name='recommend_user_recommend'),

    #scan url
    #path('scan/all_scan_list', views.scan_all_scan_list, name='scan_all_scan_list'),
    #path('scan/latest_scan_list', views.scan_latest_scan_list, name='scan_latest_scan_list'),
    #path('scan/scan_list', views.scan_scan_list, name='scan_scan_list'),


]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#static 폴더 url설정

#path(url,해당 요청을 다룰 view의 함수)
#root url은 " 라고 치면됨.
