from rest_framework import routers
from public import views
from django.urls import path
from public.views import MyTokenObtainPairView

app_name = "public"
urlpatterns = [
    # 用户登录
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
router = routers.DefaultRouter()
# 用户测试信息增删改查
router.register('user', views.UserDemoModelViewSet, 'user')
urlpatterns += router.urls
