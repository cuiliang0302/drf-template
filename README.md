## 项目概述
DRF初始化模板，实现开发生产环境区分，开发模式使用sqlite。生产模式使用mysql+redis

## 开发模式运行项目
`python manage.py runserver --settings=DRF.settings.product 0.0.0.0:8000`

## 生产模式运行项目

### MySQL部署

```bash
[root@aliyun opt]# mkdir -p /opt/docker/mysql
[root@aliyun opt]# cd /opt/docker/mysql/
[root@aliyun mysql]# docker run -p 3306:3306 --name mysql -v $PWD/conf:/etc/mysql/conf.d -v $PWD/logs:/logs -v $PWD/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=CuiLiang@0302 -d --restart=always mysql

# 创建数据库
mysql> CREATE DATABASE myblog_new DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
Query OK, 1 row affected, 2 warnings (0.01 sec)

mysql> show databases;
# 导入数据
mysql> use myblog;
Database changed
mysql> source /root/myblog.sql;
mysql> show tables;
```

### redis部署

```bash
[root@aliyun docker]# docker run --name redis -p 6379:6379 -d --restart=always redis --requirepass CuiLiang@0302
fe24cb38242ed2f1c8c7340fa1ce05f39c8fc351a7a96506c43dff41ca0774bb
[root@aliyun docker]# docker exec -it redis redis-cli
127.0.0.1:6379> auth CuiLiang@0302
OK
```

### 后端API部署
```bash
docker build -t drf:v1 . 
docker run -p 8000:8000 --name drf --restart always --link mysql --link redis -d drf:v1
```