from rest_framework import routers
from api import views
from django.urls import path
from api.views import MyTokenObtainPairView, async_view, sync_view

app_name = "api"
urlpatterns = [
    # 用户登录
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("async/", async_view),  # 异步视图 - 调用异步任务
    path("sync/", sync_view),  # 同步视图 - 调用普通同步任务
    # 只读视图集
    path('users/', views.UserDemoReadOnlyModelViewSet.as_view({'get': 'list'})),
    path('users/<int:pk>/', views.UserDemoReadOnlyModelViewSet.as_view({'get': 'retrieve'}))
]
router = routers.DefaultRouter()
# 用户测试信息增删改查
router.register('user', views.UserDemoModelViewSet, 'user')
urlpatterns += router.urls
