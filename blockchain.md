# blockchain

## WEB客户端

项目的WEB客户端属于区块链的分节点，主要用于SUPBANK的用户使用和查询已有的区块和交易信息。用户可通过浏览器进入注册页面进行账号注册，注册完毕并登陆后将进入。WEB客户端端一共有四个页面，囊括了一个区块链登陆、交易、查询系统的所需的主要功能，包括注册页面Register.html, 用于登陆的Login.html页面, 主页Home.html, 以及查询区块详细信息的Detail.html页面。

## 文件结构

前端代码遵循了前端开发追求简洁清晰的要求，将HTML文件、CSS文件和JAVASCRPT文件分开存放，能够更清晰地表现出项目的体系结构。代码主要分为以下三部分：

PAGES文件夹主要用于存放静态的HTML文件，这些文件中的scripts, style标签对CSS与JS文件夹下的CSS文件具有依赖关系。CSS文件夹主要用于存放页面所需要的样式文件，将HTML文件和CSS分离的好处是能够更好地进行项目迭代，省去了诸多手动修改的繁琐操作。JS文件夹用于存放页面的JAVASCRIPT文件，这些文件的脚本使得页面的动态运作，其中包括与WEB服务器进行注册、登陆验证、传输BLOCK数据结构等功能。

## 技术介绍

### Bootstrap介绍

Bootstrap是推特推出的一个用于前端开发的开源工具包，在项目中用于快速开发Web应用程序，是项目中区块链网页客户端的前端框架。Bootstrap是基于HTML、CSS、JAVASCRIPT，具有良好浏览器支持、响应式设计和开源等诸多优点。在Bootstrap包中提供了带有网格系统、链接样式、背景的基本结构，Bootstrap CSS提供了全局的 CSS设置、定义基本的HTML元素样式和可扩展的class，包中还包含了若干可重用的组建和若干自定义的jQury插件

### AJAX

AJAX的缩写是异步JAVASCRIPT和XML的缩写，其不是一种新的编程语言或是技术，使用现有标准的新方法。其最大的优点是在不重新加载整个页面的情况下，可以与服务器交换数据并更新部分网页内容。在项目中使用了AJAX在需要获取服务器数据时主动与WEB服务器进行数据连接，并请求验证注册时输入格式和重名、验证登陆时的账号密码、和向后端获取BLOCK数据结构。




