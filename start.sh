#! /bin/bash
mkdir logs
echo "正在启动后端API服务……"
nohup uwsgi --ini uwsgi.ini > logs/django.log 2>&1 &
sleep 3
echo "正在启动定时任务……"
nohup python manage.py crontab > logs/crontab.log 2>&1 &
sleep 3
echo "服务启动成功！"
tail -f logs/django.log