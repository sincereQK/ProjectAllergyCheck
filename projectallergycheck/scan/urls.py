from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from . import views # . 은 '현재 디렉토리에서' 라는 의미

#scan url.py
app_name = 'scan'
urlpatterns = [
    #scan url
    #path('scan_list/', views.scan_scan_list, name='scan_scan_list'),

]