# 项目dockerfile镜像文件
FROM rockylinux:latest
RUN dnf install -y python38 sudo mysql-devel gcc python38-devel vim
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone
ADD . /opt/drf/
RUN pip3.8 install -r /opt/drf/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
WORKDIR /opt/drf/
# 开发环境
#EXPOSE 8000
#CMD ["python3.8","manage.py","runserver","--settings=DRF.settings.develop","0.0.0.0:8000"]
# 测试环境
EXPOSE 8000
CMD ["python3.8","manage.py","runserver","--settings=DRF.settings.product","0.0.0.0:8000"]
# 线上环境
#EXPOSE 8997
#RUN pip3.8 install uwsgi
#CMD ["uwsgi","--ini","/opt/drf/other/uwsgi.ini"]