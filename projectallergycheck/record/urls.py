from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views # . 은 '현재 디렉토리에서' 라는 의미

#record url.py
app_name = 'record'
urlpatterns = [
    #record url
    path('all_scan_list/', views.record_all_scan_list, name='record_all_scan_list'),
    path('latest_scan_list/', views.record_latest_scan_list, name='record_latest_scan_list'),
]