# 项目dockerfile镜像文件
FROM python:3.11
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone && pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
ADD . /opt/DRF/
RUN pip install -r /opt/DRF/requirements.txt
WORKDIR /opt/DRF/
EXPOSE 8000
# 开发环境
#CMD ["python","manage.py","runserver","0.0.0.0:8000"]
# 测试环境
# ENV PROJECT_ENV prod
#CMD ["PROJECT_ENV=prod","python","manage.py","runserver","0.0.0.0:8000"]
# 生产环境(无定时任务)
#ENV PROJECT_ENV prod
#CMD ["gunicorn", "DRF.asgi:application", "-k", "uvicorn.workers.UvicornWorker","-c","gunicorn_conf.py"]
# 生产环境(启用定时任务)
ENV PROJECT_ENV prod
CMD ["sh","start.sh"]