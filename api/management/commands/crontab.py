from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from django.core.management.base import BaseCommand
from django_apscheduler import util
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django.conf import settings
from loguru import logger


def my_job():
    logger.info('开始执行my_job任务')


@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=IntervalTrigger(seconds=60, timezone=settings.TIME_ZONE),  # Every 10 seconds
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=5,
            replace_existing=True,
            misfire_grace_time=60
        )
        logger.info("添加my_job任务成功")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Midnight on Monday, before start of the next work week.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True
        )
        logger.info("添加delete_old_job_executions任务成功")

        try:
            logger.info("scheduler开始执行...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("scheduler停止执行...")
            scheduler.shutdown()
            logger.info("Scheduler成功停止!")
