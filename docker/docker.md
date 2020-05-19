

` helloworld` : sudo docker run hello-world

```shell
Hello from Docker!
```



`查看镜像` : docker images

```shell
root@server-ubuntu:/data# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              bf756fb1ae65        4 months ago        13.3kB
```



### 一. 常用命令

帮助:

```shell
docker version			#docker版本
docker info					#docker系统信息
docker 命令 --help	 #帮助
docker history 镜像id		#镜像操作历史
```

命令帮助文档:

https://docs.docker.com/reference/

==镜像==

#### docker image 查看镜像

```shell
root@server-ubuntu:/data# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
hello-world         latest              bf756fb1ae65        4 months ago        13.3kB

# 注释
REPOSITORY	仓库源
TAG					标签
IMAGE ID		ID
CREATED			创建时间
SIZE				大小

# 可选项:
  -a, --all             列出所有镜像(默认参数)
  -q, --quiet           只显示ID
```

#### docker search 搜索镜像

```shell
root@server-ubuntu:/etc/docker# docker search mysql                      
NAME                              DESCRIPTION                                     STARS               OFFICIAL            AUTOMATED
mysql                             MySQL is a widely used, open-source relation…   9504                [OK]                
mariadb                           MariaDB is a community-developed fork of MyS…   3446                [OK]                
mysql/mysql-server                Optimized MySQL Server Docker images. Create…   696                                     [OK]
centos/mysql-57-centos7           MySQL 5.7 SQL database server                   75                                      

# 可选项:
  -f, --filter 过滤,如搜索关注大于3000的镜像: docker search mysql --filter=STARS=3000
```

#### docker pull 下载镜像

```shell
root@server-ubuntu:/etc/docker# docker pull mysql #可以指定版本,如docker pull mysql:5.7
Using default tag: latest						#如果不写tag默认下载latest
latest: Pulling from library/mysql
afb6ec6fdc1c: Pull complete 				#联合文件系统 , 分层下载
0bdc5971ba40: Pull complete 
97ae94a2c729: Pull complete 
f777521d340e: Pull complete 
1393ff7fc871: Pull complete 
a499b89994d9: Pull complete 
7ebe8eefbafe: Pull complete 
597069368ef1: Pull complete 
ce39a5501878: Pull complete 
7d545bca14bf: Pull complete 
0f5f78cccacb: Pull complete 
623a5dae2b42: Pull complete 
Digest: sha256:beba993cc5720da07129078d13441745c02560a2a0181071143e599ad9c497fa		#签名
Status: Downloaded newer image for mysql:latest
docker.io/library/mysql:latest			#真实地址
```

#### docker rmi 删除镜像

```shell
docker rmi img_id 根据id删除镜像
docker rmi -f $(docker images -aq)	删除所有镜像
docker rmi -f img_id1 img_id2	删除多个镜像
```

==容器命令==

> 创建容器前必须有镜像

#### 新建容器并启动

docker run [可选参数] image 

```shell
# 参数
--name="Name"		容器名
-d							后台运行
-it							使用交互模式运行,进入容器查看内容  
-P							小写P 指定容器端口 -P 8080:8080
		-P 	主机端口:容器端口(常用)
		-P 	ip:主机端口:容器端口
		-P 	容器端口
-p							大写p 随机端口

例:
1.运行centos并用bash进入,进入后输入exit退出容器
docker run -it centos /bin/bash
2.后台启动 (如果内部没有操作会自动停止)
docker run -d centos
```

#### 退出容器

```shell
exit	退出并停止容器
ctrl+P+Q	退出不停止容器
```

#### 进入正在运行的容器

```shell
docker exec -it 容器id /bin/bash	#进入后开启新的终端

docker attach 容器id /bin/bash	#进入正在执行的终端
```

#### 查看所有运行的容器

docker ps

```shell
# 参数
-a 		列出运行中的容器+历史运行过的容器
-n=?	列出最近创建的容器
-q		只显示id

root@server-ubuntu:/data# docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

root@server-ubuntu:/data# docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES
b5f2496cdc04        centos              "/bin/bash"         4 minutes ago       Exited (0) 2 minutes ago                        reverent_mayer
ea124acc6057        bf756fb1ae65        "/hello"            58 minutes ago      Exited (0) 58 minutes ago                       elegant_hamilton
```

#### 删除容器

```shell
docker rm 容器id		#删除某容器
docker rm -f 容器id				#强制删除容器
docker rm -f $(docker ps -aq)		#删除所有容器
docker ps -a -q | xargs docker rm 	#删所有容器
```

#### 启动停止容器

```shell
docker start 容器id		#启动
docker restart 容器id	#重启
docker stop 容器id		#停止容器
docker kill 容器id		#强制停止容器
```

==进阶命令==

#### 日志

```shell
docker logs [参数] 容器id

#参数
-tf						#显示日志
--tail 条数		#显示几条
```

#### 容器内的进程信息

```shell
docker top 容器id
root@server-ubuntu:~# docker top d376c22d8eed
UID                 PID                 PPID                C                   STIME               TTY                 TIME                CMD
root                6853                6834                1                   03:07               ?                   00:00:00            /bin/bash -c while true;do date;sleep 1;done
root                6970                6853                0                   03:07               ?                   00:00:00            /usr/bin/coreutil
```

#### 查看镜像元数据

```shell
docker inspect		#容器信息
```

#### 从容器内复制文件到容器外

```shell
docker cp 容器id:容器内文件 容器外位置
例:
docker cp d376c22d8eed:/home/test.text ./
```

```
docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:tag
```

#### 查看docker内存情况

```shell
docker stats
```

#### 内存限制

```
# 安装ES 并限制 ES 内存
docker run -d --name elasticsearch02 -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" -e ES_JAVA_OPTS="-Xms64m -Xmx512m" elasticsearch
```

#### 可视化管理

```
docker run -d -p 9000:9000 -p 8000:8000 --name portainer --restart always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```



### 二. 提交容器

docker commit

```shell
# 提交容器
docker commit -m="描述信息" -a="坐着" 容器id
```



### 三. 容器数据卷

> 简述作用: 将容器内的文件存储到docker外的物理机上

#### 挂载数据卷

```shell
-v
docker run -it -v 主机目录:容器内目录 容器id /bin/bash
例子:
1. 把mysql的 配置文件 和 数据 挂载到容器外的磁盘上
docker run -d -p 3306:3306 -v /data/mysql/conf:/etc/mysql/conf.d -v /data/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 --name=mysql01 mysql:5.7

```

#### 具名和匿名挂载

```shell
# 匿名挂载 (没名字,随机名字)
-v 容器内路径
docker run -d -P --name nginx01 -v /etc/nginx nginx

# 具名挂载 (有名字)
-v 卷名:容器内路径
docker run -d -P --name nginx01 -v juming_nginx:/etc/nginx nginx

# 设置容器权限
ro	#readonly 只读, 只能通过宿主机操作,容器内无法操作
rw	#readwrite	可读可写
docker run -d -P --name nginx01 -v juming_nginx:/etc/nginx:ro nginx
docker run -d -P --name nginx01 -v juming_nginx:/etc/nginx:rw nginx

# 查看所有 volume
root@server-ubuntu:/data# docker volume ls
DRIVER              VOLUME NAME
local               140f5c069322becf2fe8bef79dc4ad2b2da255053e7197744ed1ce34d2a7b741
local               f6dac5f4a8e91817f42cd5bbd8038899311b39a7a381df6d69b27ee0435fb2cd
local               portainer_data
# 查看挂载情况 docker volume inspect 卷名
root@server-ubuntu:/data# docker volume inspect portainer_data
[
    {
        "CreatedAt": "2020-05-17T04:40:13+08:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/portainer_data/_data",
        "Name": "portainer_data",
        "Options": {},
        "Scope": "local"
    }
]
如果没有指定挂载路径,默认指向/var/lib/docker/volumes/xxx/_data
```

#### 容器间共享卷

> 容器间的文件共享, 共享后当某容器被删除后其他容器的共享文件不会被删除

```shell
--volumes-from		#类似java继承,docker02继承docker01的挂在卷
例子:
docker run -it --name docker02 --volumes-from docker01 centos
```



### 四. DockerFile

#### 构建步骤

1. 编辑Dockerfile
2. docker build 镜像
3. docker run 运行镜像
4. docker push 发布镜像

#### 构建指令

> 关键字必须是全大写字母

```shell
FROM					# 基础镜像, 大部分镜像都是从 scratch 开始
MAINTAINER		# 镜像作者信息, 姓名+邮箱
RUN						# 构建的时候需要运行的命令
ADD						# 步骤
WORKDIR				# 镜像工作目录
VOLUME				# 挂在卷
EXPOSE				# 指定暴露端口

CMD						# 容器启动时执行的命令, 只有最后一个会生效, 替代
ENTRYPOINT		# 容器启动时执行的命令, 追加命令

ONBUILD				# 当构建一个被继承的 dockerfile 时会执行 ONBUILD 指令
COPY					# 类似ADD, 京文件拷贝到镜像
ENV						# 构建的时候设置环境变量
```

例子

```shell
# 例子1, 自定义centos
FROM centos												#基于centos
MAINTAINER hxl<weibosteam@163.com>

ENV MYPATH /data
WORKDIR $MYPATH

RUN yum -y install vim						#安装vim
RUN yum -y install net-tools			#安装net-tools

EXPOSE 80

CMD echo $MYPATH
CMD echo "----final----"
CMD /bin/bash
```

```shell
# 例子2, tomcat镜像
FROM centos
MAINTAINER hxl<weibosteam@163.com>

COPY README.txt /data/readme.txt

ADD jdk-8u171-linux-x64.tar.gz /data/
ADD apache-tomcat-9.0.35.tar.gz /data/

RUN yum -y install vim

ENV MYPATH /data
WORKDIR $MYPATH

ENV JAVA_HOME /data/jdk1.8.0_171
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
ENV CATALINA_HOME /data/apache-tomcat-9.0.35
ENV CATALINA_BASH /data/apache-tomcat-9.0.35
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/lib:$CATALINA_HOME/bin

EXPOSE 8080

CMD /data/apache-tomcat-9.0.35/bin/startup.sh && tail -f /data/apache-tomcat-9.0.35/logs/catalina.out

#----------构建镜像
docker build -t mytomcattest001 .

#----------挂载webapps和logs
docker run -d -p 3344:8080 --name mytomcat001 -v /data/dockerfiles/docker_tomcat_test/webapps:/data/apache-tomcat-9.0.35/webapps/ -v /data/dockerfiles/docker_tomcat_test/tomcatlogs/:/data/apache-tomcat-9.0.35/logs/ mytomcattest001
```



### 五. 发布镜像

#### 发布至dockerhub

```shell
#1. 登录dockerhub
docker login -u 用户名

#2. 提交镜像
docker push 用户名/镜像名:tag #docker push webuserhu/testcentos:1.0

#3. 镜像重复的话可以改TAG
docker tag 镜像id TAG ##docker tag xxx webuserhu/testcentos:1.1

```

#### 发布至阿里云镜像

```shell
1.登录阿里云
2.进入容器镜像服务
3.创建命名空间
4.创建镜像仓库,选择本地仓库

1. 登录阿里云Docker Registry
$ sudo docker login --username=15510615638 registry.cn-beijing.aliyuncs.com
用于登录的用户名为阿里云账号全名，密码为开通服务时设置的密码。

您可以在访问凭证页面修改凭证密码。

2. 从Registry中拉取镜像
$ sudo docker pull registry.cn-beijing.aliyuncs.com/webuserhu/my_repo:[镜像版本号]
3. 将镜像推送到Registry
$ sudo docker login --username=15510615638 registry.cn-beijing.aliyuncs.com
$ sudo docker tag [ImageId] registry.cn-beijing.aliyuncs.com/webuserhu/my_repo:[镜像版本号]
$ sudo docker push registry.cn-beijing.aliyuncs.com/webuserhu/my_repo:[镜像版本号]
请根据实际镜像信息替换示例中的[ImageId]和[镜像版本号]参数。

4. 选择合适的镜像仓库地址
从ECS推送镜像时，可以选择使用镜像仓库内网地址。推送速度将得到提升并且将不会损耗您的公网流量。

如果您使用的机器位于VPC网络，请使用 registry-vpc.cn-beijing.aliyuncs.com 作为Registry的域名登录，并作为镜像命名空间前缀。
5. 示例
使用"docker tag"命令重命名镜像，并将它通过专有网络地址推送至Registry。

$ sudo docker images
REPOSITORY                                                         TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
registry.aliyuncs.com/acs/agent                                    0.7-dfb6816         37bb9c63c8b2        7 days ago          37.89 MB
$ sudo docker tag 37bb9c63c8b2 registry-vpc.cn-beijing.aliyuncs.com/acs/agent:0.7-dfb6816
使用"docker images"命令找到镜像，将该镜像名称中的域名部分变更为Registry专有网络地址。

$ sudo docker push registry-vpc.cn-beijing.aliyuncs.com/acs/agent:0.7-dfb6816
```

#### 镜像打包

```shell
1.将镜像打包为压缩包
docker save

2.从压缩包加载为镜像
docker load
```



### 六. Docker网络

```shell
docker network
#参数
	ls	展示所有网络
	inspect	查看信息
	rm	删除
	create 创建
	connect 连通容器到某网络
```

网络模式:

 	1. bridge:  桥接 (默认)
 	2. none: 不配置网络
 	3. host: 和宿主机共享网络
 	4. container: 容器网络

#### Docker0

```shell
root@server-ubuntu:/data/dockerfiles/docker_tomcat_test# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 00:16:3e:16:73:86 brd ff:ff:ff:ff:ff:ff
    inet 172.17.249.121/20 brd 172.17.255.255 scope global dynamic eth0
       valid_lft 315266685sec preferred_lft 315266685sec
    inet6 fe80::216:3eff:fe16:7386/64 scope link 
       valid_lft forever preferred_lft forever
3: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
    link/ether 02:42:60:63:8a:b5 brd ff:ff:ff:ff:ff:ff
    inet 172.18.0.1/16 brd 172.18.255.255 scope global docker0
       valid_lft forever preferred_lft forever
       
# lo: 本机回环地址
# eth0: 内网地址
# docker0: docker地址
```

#### 通过容器名称ping通

```shell
--link
# 通过名称t2可以ping通t1 , 但是t1不能ping通t2
docker run -d --name t2 --link t1 -p 8081:8080 tomcat01
# 原理,会在t2的hosts文件配置了t1的映射
172.18.0.3	t1	40748892eb11
```

#### 自定义网络

> 容器互联, 当我们通过自定义网络创建容器后, 就可以通过ip或容器名ping通了

```shell
docker network create --driver bridge --subnet 192.168.0.0/16 --gateway 192.168.0.1 mynet

# --driver bridge 桥接
# --subnet 192.168.0.0/16 子网
# --gateway 192.168.0.1 网关
```

![](https://tva1.sinaimg.cn/large/007S8ZIlly1gexqcj8ittj313m0o8djj.jpg)

```shell
# 根据上图 tomcat-01 ping 不通 tomcat-net-01及tomcat-net-02
# 我们通过用 docker network connect 来建立 mynet和tomcat-01和tomcat-02的网络关系
docker network connect mynet tomcat-01
# 这样tomcat-01就能ping通tomcat-net-01
```

==测试搭建redis集群==

![](https://tva1.sinaimg.cn/large/007S8ZIlly1gexqkyirf6j30xy0ks76k.jpg)



```shell
#1. 创建网卡
root@server-ubuntu:~# docker network create redisnet --subnet 172.38.0.0/16
85c14df394a85434105339325ac155f3d7657a93315895cbc0d63b57a0b472e5

root@server-ubuntu:~# docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
1f0ca4001458        bridge              bridge              local
0a74ca817b6b        host                host                local
8bedb49b3177        none                null                local
85c14df394a8        redisnet            bridge              local

#2. 通过脚本创建redis配置文件
for port in $(seq 1 6); \
do \
mkdir -p /data/redis/node-${port}/conf
touch /data/redis/node-${port}/conf/redis.conf
cat << EOF >/data/redis/node-${port}/conf/redis.conf
port 6379
bind 0.0.0.0
cluster-enabled yes
cluster-config-file nodes.conf
cluster-node-timeout 5000
cluster-announce-ip 172.38.0.1${port}
cluster-announce-port 6379
cluster-announce-bus-port 16379
appendonly yes
EOF
done

#3. 启动容器
for port in $(seq 1 6); \
do \
docker run -p 637${port}:6379 -p 1637${port}:16379 --name redis-${port} \
-v /data/redis/node-${port}/data:/data \
-v /data/redis/node-${port}/conf/redis.conf:/etc/redis/redis.conf \
-d --net redisnet --ip 172.38.0.1${port} redis:5.0.9-alpine3.11 redis-server /etc/redis/redis.conf
done

#4. 进入随便一个节点容器, redis镜像没有bash, 通过sh进入
docker exec -it redis-1 /bin/sh

#5.在节点容器内创建集群
redis-cli --cluster create 172.38.0.11:6379 172.38.0.12:6379 172.38.0.13:6379 172.38.0.14:6379 172.38.0.15:6379 172.38.0.16:6379 --cluster-replicas 1

#6. 测试连接
/data # redis-cli -c
127.0.0.1:6379> cluster info
cluster_state:ok
cluster_slots_assigned:16384
cluster_slots_ok:16384
cluster_slots_pfail:0
cluster_slots_fail:0
cluster_known_nodes:6
cluster_size:3
cluster_current_epoch:6
cluster_my_epoch:1
cluster_stats_messages_ping_sent:133
cluster_stats_messages_pong_sent:140
cluster_stats_messages_sent:273
cluster_stats_messages_ping_received:135
cluster_stats_messages_pong_received:133
cluster_stats_messages_meet_received:5
cluster_stats_messages_received:273

127.0.0.1:6379> cluster nodes
ee962ddf8c20ef2b1ed6ea97aea5e25dc5a2b232 172.38.0.15:6379@16379 slave 0b9ca7d74dd66d2921b91bf396fa282205c7cf98 0 1589872704357 5 connected
0b9ca7d74dd66d2921b91bf396fa282205c7cf98 172.38.0.11:6379@16379 myself,master - 0 1589872704000 1 connected 0-5460
c210cd2705c99b772a06c6573fc06932213ecc3c 172.38.0.13:6379@16379 master - 0 1589872705359 3 connected 10923-16383
0c6ee587a872c5f4943c62098c70d14026f2a778 172.38.0.12:6379@16379 master - 0 1589872705860 2 connected 5461-10922
7307f396bc0547bc06b474a94fd0bdda024a97d8 172.38.0.16:6379@16379 slave 0c6ee587a872c5f4943c62098c70d14026f2a778 0 1589872705000 6 connected
7efd0b6a2cccbc198672788f396e4059ddf75be6 172.38.0.14:6379@16379 slave c210cd2705c99b772a06c6573fc06932213ecc3c 0 1589872704000 4 connected
127.0.0.1:6379> 
```

#### 部署简单项目

创建springboot项目, 打包,jar包和Dockerfile上传至统一目录下,构建&启动

```
FROM java:8

COPY *.jar /app.jar

CMD ["--server.port=3344"]

EXPOSE 3344

ENTRYPOINT ["java","-jar","/app.jar"]
```

