from rest_framework import routers
from public import views
from django.urls import path
from public.views import MyTokenObtainPairView

app_name = "public"
urlpatterns = [
    # 用户登录
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 定时作业暂停/恢复
    path('job_pause/<str:job_id>/', views.JobPauseAPIView.as_view(), name='job_pause'),
    # 更改定时作业触发器
    path('job_triggers/<str:job_id>/', views.JobTriggersAPIView.as_view(), name='job_triggers'),
    # 立即执行一次定时作业
    path('job_run/<str:job_id>/', views.JobRunAPIView.as_view(), name='job_triggers')
]
router = routers.DefaultRouter()
# 用户测试信息增删改查
router.register('user', views.UserDemoModelViewSet, 'user')
# 获取定时任务执行历史记录
router.register('job_history', views.JobHistoryReadOnlyModelViewSet, 'job_history')
# 获取定时任务列表
router.register('job', views.JobModelViewSet, 'job')
urlpatterns += router.urls
