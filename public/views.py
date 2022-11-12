import asyncio
from time import sleep

import httpx
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from public.models import UserDemo
from public.serializers import UserDemoSerializer, MyTokenObtainPairSerializer
from public.utils import MyPageNumber


def api_doc(request):
    """
    API 接口文档
    """
    return render(request, 'doc.html')


class MyTokenObtainPairView(TokenObtainPairView):
    """
    自定义jwt认证
    """
    serializer_class = MyTokenObtainPairSerializer


class UserDemoModelViewSet(viewsets.ModelViewSet):
    """
    用户测试增删改查
    """
    queryset = UserDemo.objects.all()
    serializer_class = UserDemoSerializer


# 异步任务
async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)


# 同步任务
def http_call_sync():
    for num in range(1, 6):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org/")
    print(r)


# 异步视图 - 调用异步任务
async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("异步视图 - 调用异步任务")


# 同步视图 - 调用普通同步任务
def sync_view(request):
    http_call_sync()
    return HttpResponse("同步视图 - 调用普通同步任务")
