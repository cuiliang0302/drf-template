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