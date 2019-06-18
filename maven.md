# maven

## Core concept

-------------------

### Maven

* Project build & manage tool that provides manage builds, documents, reports, dependencies, scms, release, dispatch
* 好处：将项目过程规范化、自动化、高效化，可扩展性
* 还可实现获得代码检查报告、单元测试覆盖率，实现持续集成

### core concept

#### pom

Project Object Model

#### Artifact

大致等于项目要产生的文件 -> jar, 源文件, 二进制等  
由groupId:artifactId:version组成唯一识别  

#### Repositories

存储Artifact  
项目需要使用工具时，在中声明，代码能根据dependency下载工具
mvn install能将项目放到仓库中

#### Build Lifecycle

项目build过程，maven中分三种build lifecycle

* default = 处理项目部署
* clean = 处理项目清理
* site = 处理项目文档生成

phases - 是build lifecycle的一步，build lifecycle由phase组成  
> 执行phase时，mvn会把该phase之前的phase都执行一遍
部分phase (有序)

* validate
* compile
* test
* package
* integration-test
* verify
* install
* deploy

#### Goal = 特定任务

#### Archetype = 原型/模板

archetype = 实现goal的plugin  
plugin = a cikkectuib if goals with a geberak common purpose
(archetype:generate = goal)

## 文件结构

-------------------

* TOP
   1. pom.xml
   2. src -> all sourse material for building
      1. main
         1. java -> Application/library sources code
         2. resources -> application/library resources
         3. filters -> resource filter files
      2. test -> for unit test code/resources
         1. java
         2. resources
         3. filters
      3. it -> integration test
      4. assembly -> assembly descriptors
      5. site
   3. target -> all output of the build

## pom.xml

-------------------

maven项目级别的核心配置文件，包含了build项目所需的绝大部分信息
描述项目的:

> 1. maven坐标
> 2. 依赖关系
> 3. 开发者须遵循的规则
> 4. 缺陷管理系统
> 5. 其他所有项目相关因素

### tags

1. project = 顶级元素
2. modelVersion = 模型版本
3. groupId = 公司、组织唯一id
4. artifactId = 项目唯一id
5. version = 项目所处版本号
6. packaging
   > 打包的机制, eg: pom, jar, maven-lugin, ejb, rar等，默认jar
7. classifier = 帮助定义构建输出的附属构建
8. dependencies = 项目依赖关系
   * dependecy = 每个denpendency对应一个jar包
9. properties = 为pom定义的常量
10. build = build配置
11. parent = 父pom

### build tag 构建配置

tags

1. finalName = 构建文件名，默认"${artifactId}-${version}"
2. directory = 构建产生文件存放目录，默认"${basedir}/target"
3. defaultGoal = 未规定目标时的默认值，须能与phase或命令行参数对应
4. filters 过滤器属性文件列表???
5. resources = 项目所有资源路径列表
    > 如配置文件、属性文件
6. testResources = 单元测试所有资源路径
7. sourceDirectory = 项目源码目录
8. scriptSourceDirectory = 项目脚本源码目录
    > 一般会被拷贝到输出目录
9. outputDirectory = 被编译过的class
10. testOutputDirectory = 测试
11. extensions -> 可用maven插件完成部署时等打包等繁琐指令
    > 可使用wagon-maven-pugin, wagon-ftp等等
12. plugins = 使用的插件列表
13. pluginManagement = 本地配置

## Maven 日用三板斧

* mvn archetype:generate 创建maven项目
* mvn package 打包，上面已经介绍过了
* mvn package -Prelease打包，并生成部署用的包，比如deploy/*.tgz
* mvn install 打包并安装到本地库
* mvn eclipse:eclipse 生成eclipse项目文件
* mvn eclipse:clean 清除eclipse项目文件
* mvn site 生成项目相关信息的网站


## maven training

### settings
镜像路径

update project -> 更新包依赖