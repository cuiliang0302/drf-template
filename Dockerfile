# 项目dockerfile镜像文件
FROM rockylinux:8
RUN dnf install -y python38 sudo mysql-devel gcc python38-devel langpacks-zh_CN
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone
ADD . /opt/DRF/
RUN pip3.8 install -r /opt/DRF/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
WORKDIR /opt/DRF/
# 开发环境
#EXPOSE 8000
#CMD ["python3.8","manage.py","runserver","--settings=DRF.settings.develop","0.0.0.0:8000"]
# 测试环境
#EXPOSE 8000
# ENV DJANGO_SETTINGS_MODULE DRF.settings.develop
#CMD ["python3.8","manage.py","runserver","--settings=DRF.settings.product","0.0.0.0:8000"]
# 生产环境
EXPOSE 8888
ENV DJANGO_SETTINGS_MODULE DRF.settings.product
ENV LANG zh_CN.UTF-8
RUN pip3.8 install uwsgi -i https://pypi.tuna.tsinghua.edu.cn/simple
CMD ["uwsgi","--ini","/opt/DRF/uwsgi.ini"]