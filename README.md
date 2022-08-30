## 项目概述

本项目为DRF初始化模板，具体实现了以下功能

* 完整的序列化器、视图、路由示例。
* 集成Apscheduler定时任务模块与接口
* 实现开发生产环境区分，密钥与代码拆分。
* 开发模式使用sqlite。生产模式使用mysql+redis。
* 使用docker实现自动打包与发布。

## 接口文档

* 部署后查看：

    [接口文档](http://127.0.0.1:8000)

* 文件查看：

    [接口文档](./templates/doc.html)

* 在线查看

    链接: https://www.apifox.cn/apidoc/shared-34bb4a27-bf7b-432d-9d51-0a767a259e6e  访问密码 : 4UoQc75S 

## 开发模式运行项目

```bash
pip install -r requirements.txt
python manage.py runserver
```

## 生产模式运行项目

### MySQL部署

```bash
[root@aliyun opt]# mkdir -p /opt/docker/mysql
[root@aliyun opt]# cd /opt/docker/mysql/
[root@aliyun mysql]# docker run --name mysql -p 3306:3306 -v $PWD/conf:/etc/mysql/conf.d -v $PWD/logs:/logs -v $PWD/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123.com -d --restart=always mysql

# 创建数据库
mysql> CREATE DATABASE drf DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
Query OK, 1 row affected, 2 warnings (0.01 sec)

mysql> show databases;
```

### redis部署(可选)

如果使用redis缓存，envs/.env.prod配置如下
`#CACHE_URL=rediscache://redis:6379/0?client_class=django_redis.client.DefaultClient&password=123.com`

```bash
[root@aliyun docker]# docker run --name redis -p 6379:6379 -d --restart=always redis --requirepass 123.com
fe24cb38242ed2f1c8c7340fa1ce05f39c8fc351a7a96506c43dff41ca0774bb
[root@aliyun docker]# docker exec -it redis redis-cli
127.0.0.1:6379> auth CuiLiang@0302
OK
```

### 后端API部署

```bash
docker build -t drf:v1 . 
docker run --name drf -d -p 8888:8888 --restart always --link mysql --link redis drf:v1
```

### nginx配置

```bash
user root;
worker_processes auto;
error_log /var/log/nginx/error.log;
pid /run/nginx.pid;
# Load dynamic modules. See /usr/share/doc/nginx/README.dynamic.
include /usr/share/nginx/modules/*.conf;
events {
    worker_connections 1024;
}
http {
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';
    access_log  /var/log/nginx/access.log  main;
    sendfile            on;
    tcp_nopush          on;
    tcp_nodelay         on;
    keepalive_timeout   65;
    types_hash_max_size 2048;
    include             /etc/nginx/mime.types;
    default_type        application/octet-stream;
    include /etc/nginx/conf.d/*.conf;
    server {
        listen       80;
        server_name  ~^.*$;
        location / {
              include uwsgi_params;
              uwsgi_pass drf:8888;
              uwsgi_ignore_client_abort on;
        }
    }
}
```

### nginx部署

```bash
docker run --name nginx -d -p 80:80 -v $PWD/nginx.conf:/etc/nginx/nginx.conf --restart always --link drf nginx
```

## 注意事项

### 执行数据库迁移

```bash
docker exec -it drf bash
python manage.py makemigrations
python manage.py migrate
```

### 收集admin静态资源文件

```bash
docker exec -it drf bash
python manage.py collectstatic
```

### 默认用户名/密码

用户名`admin`
密码`123.com`
