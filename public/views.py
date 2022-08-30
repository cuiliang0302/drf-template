from django.shortcuts import render
from django_apscheduler.models import DjangoJobExecution, DjangoJob
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from public.models import UserDemo
from public.serializers import UserDemoSerializer, MyTokenObtainPairSerializer, DjangoJobExecutionSerializer, \
    DjangoJobSerializer
from public.utils import MyPageNumber
from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.job import Job as AppSchedulerJob
from django_apscheduler.jobstores import DjangoJobStore, DjangoMemoryJobStore

django_job_store = DjangoJobStore()


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


class JobHistoryReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """
    定时作业执行历史
    """
    queryset = DjangoJobExecution.objects.all()
    serializer_class = DjangoJobExecutionSerializer
    pagination_class = MyPageNumber


class JobModelViewSet(viewsets.ModelViewSet):
    """
    定时作业列表
    """
    queryset = DjangoJob.objects.all()
    serializer_class = DjangoJobSerializer

    # 重写删除方法
    def perform_destroy(self, instance):
        django_job_store.remove_job(instance.id)


class JobPauseAPIView(APIView):
    """
    定时作业暂停/恢复
    """

    @staticmethod
    def post(request, job_id):
        action = request.data.get('action')
        job: AppSchedulerJob = django_job_store.lookup_job(job_id)
        if action == 'pause':
            job.next_run_time = None
            django_job_store.update_job(job)
            result = {'id': job_id, 'message': '任务暂停成功!'}
        else:
            job_state = job.__getstate__()
            del job_state['next_run_time']
            scheduler = BackgroundScheduler()
            scheduler.add_jobstore(django_job_store)
            scheduler.add_job(replace_existing=True, **job_state)
            scheduler.start()
            result = {'id': job_id, 'message': '任务恢复成功!'}
        return Response(result, status=status.HTTP_200_OK)


class JobTriggersAPIView(APIView):
    """
    更改定时作业触发器
    """

    @staticmethod
    def post(request, job_id):
        crontab_exp = request.data.get('crontab_exp')
        job: AppSchedulerJob = django_job_store.lookup_job(job_id)
        job.trigger = CronTrigger.from_crontab(crontab_exp)
        django_job_store.update_job(job)
        result = {'id': job_id, 'message': '修改定时任务触发器成功!'}
        return Response(result, status=status.HTTP_200_OK)


class JobRunAPIView(APIView):
    """
    立即手动执行一次定时作业
    """

    @staticmethod
    def post(request, job_id):
        scheduler = BackgroundScheduler()
        scheduler.add_jobstore(DjangoMemoryJobStore())
        scheduler.start()
        job: AppSchedulerJob = django_job_store.lookup_job(job_id)
        job_state = job.__getstate__()
        del job_state['next_run_time']
        del job_state['version']
        del job_state['executor']
        job_state['trigger'] = None
        scheduler.add_job(replace_existing=True, **job_state)
        result = {'id': job_id, 'message': '定时任务手动执行成功!'}
        return Response(result, status=status.HTTP_200_OK)
