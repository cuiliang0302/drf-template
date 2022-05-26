"""DRF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.static import serve
from public import views
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    # admin管理页
    re_path('static/(?P<path>.*)', serve, {'document_root': settings.STATIC_ROOT}, name='static_url'),
    # 静态资源文件
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # API接口调试认证
    path('', views.apiDoc, name='apiDoc'),
    # API文档
    path('v1/public/', include('public.urls', namespace='public')),
    # 公共API
]
