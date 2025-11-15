import asyncio
from time import sleep

import httpx
from django.http import HttpResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from api.filter import UserDemoFilter
from api.models import UserDemo
from api.serializers import UserDemoSerializer, MyTokenObtainPairSerializer
from api.utils import MyPageNumber


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
    模型视图集(用户测试增删改查)
    """
    queryset = UserDemo.objects.all()
    serializer_class = UserDemoSerializer

    # 重写queryset方法
    # def get_queryset(self):
    #     return UserDemo.objects.order_by('-time')

    # 重写序列化器方法
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return ArticleListSerializer
    #     else:
    #         return ArticleRetrieveSerializer

    # 重写get方法
    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

    # 重写更新方法
    # def perform_update(self, serializer):
    #     serializer.save()

    # 重写更新的response
    # def update(self, request, *args, **kwargs):
    #     return Response({'msg': '点赞失败'}, status=status.HTTP_200_OK)

    # 重写删除方法
    # def perform_destroy(self, instance):
    #     instance.is_delete = True
    #     instance.save()

    # 也可以重写删除的response
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    # 重写create方法
    # def perform_create(self, serializer):
    #     Goods.objects.create(**serializer.data)

    # 重写create和response
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDemoReadOnlyModelViewSet(viewsets.ModelViewSet):
    """
    只读视图集(用户测试信息只读)
    """
    queryset = UserDemo.objects.all()
    serializer_class = UserDemoSerializer
    # 使用分页
    pagination_class = MyPageNumber
    # 模型指定字段过滤
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ('name')
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    # 指定自定义的过滤器
    filterset_class = UserDemoFilter
    # 自定义排序字段
    ordering_fields = ['age']


# 一级视图（异步任务）
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
