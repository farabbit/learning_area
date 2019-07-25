# Docker

## structure

C/S (Clienct/Server) structure, use remote API -> manage and create Docker container

Create container by using image

> 比较Docker与OOP
> Container ~ Object  
> Image ~ Class

| Docker          | Description                                                            |
| :-------------- | :--------------------------------------------------------------------- |
| 镜像 Image      | 用于创建Docker容器模板                                                 |
| 容器 Container  | 独立运行的应用                                                         |
| 客户端 Client   | 用命令行等工具通过**Docker API**与Docker守护进程 (Daemon Process) 通信 |
| 主机 Host       | 执行Docker守护进程与容器                                               |
| 仓库 Repository | 保存镜像 [Docker Hub](https://hub.docker.com)                          |
| Machine         | 简化Docker安装的命令行工具                                             |

## operations

```shell
docker run <Image>
docker stop <ContainerID> # 停止容器
docker start <>
docker restart <>
docker rm <> 移除容器

docker ps # 查看所有容器
docker logs <ContainerID> # 查看容器标准输出
# -f: ~ tail -f
docker port <ContainerID> # 查看端口映射
docker top <ContainerID> # 查看容器内部运行的进程
docker inspect <ContainerID> # 返回记录容器配置、状态的json

docker <command> --help
```

### Hello World

```shell
docker run ubentu:15.10 /bin/echo "Hello World !"
# run: 运行容器
# ubentu:15.10  要运行的镜像，若本地主机不存在，Docker从Docker Hub下载公共镜像
# bin/echo "Hello World !" 在容器里执行的命令
```

### interactive container 运行交互式容器

``` shell
docker run -i -t ubuntu:15.10 /bin/bash
# -i: 允许对容器内标准输入 STDIN进行交互
# -t: 在容器内指定终端、伪终端
# exit/CTRL+D 退出容器
```

### 后台模式

```shell
docker run -d ubuntu:15.10 /bin/sh -c "while true; do echo hello world; sleep 1; done"
# -d 后台运行
```

## 运行Web应用

```shell
docker pull training/webapp # 载入镜像
docker run -d -P training/webapp python app.py
# -P 容器内部使用的网络端口映射到我们使用的主机上
```

## 镜像使用

```shell
docker images # 查看本机镜像
docker pull <image> # 获取新镜像
docker search <keyword> # 查找镜像
```

### 创建镜像

1. 从已有容器中更新镜像，并提交

    ```shell
    docker commit -m="<message>" -a="<auther>" <ContainerID> <DestImageName>
    # commit: 提交容器副本
    docker images # 能看到创建的新镜像
    ```

2. 使用Dockerfile创建新镜像

    ```shell
    # 创建Dockerfile
    docker build
    ```
