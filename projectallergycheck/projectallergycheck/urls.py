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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('list/', include('record.urls')),
    #path('pages/', include('pages.urls')),
    path('scan/', include('scan.urls')),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#static 폴더 url설정

#path(url,해당 요청을 다룰 view의 함수)
#root url은 " 라고 치면됨.
