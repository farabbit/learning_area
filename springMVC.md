# 详细架构

请求驱动 ~ 用MVC思想，将Web层解耦
事件驱动 - Tapestry, JSF

## tips

> ps:不需要程序员开发的，需要程序员自己做一下配置即可

1. DispatcherServlet 前端控制器（不需开发）
   - 接收请求，响应结果，相当于转发器，中央处理器。有了DispatcherServlet减少了其它组件之间的耦合度
2. HandlerMapping 处理器映射器（不需开发）
   - 根据请求的url查找Handler
3. HandlerAdapter 处理器适配器（不需开发）
   - 按照特定规则（HandlerAdapter要求的规则）去执行Handler。
4. Handler 处理器（需要开发）
   - 编写Handler时按照HandlerAdapter的要求去做，这样适配器才可以去正确执行Handler
5. ViewResolver 视图解析器（不需开发）
   - 进行视图解析，根据逻辑视图名解析成真正的视图（view）
6. View 视图（需要开发jsp）
   - View是一个接口，实现类支持不同的View类型（jsp. freemarker. pdf…）

## 前端控制器

> 接收请求，响应结果，相当于转发器，中央处理器。有了DispatcherServlet减少了其它组件之间的耦合度。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
     xmlns="http://java.sun.com/xml/ns/javaee"
     xsi:schemaLocation="http://java.sun.com/xml/ns/javaee
     http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd" id="WebApp_ID" version="3.0">
  <display-name>SpringMVC_01</display-name>

  <!-- 前端控制器DispatcherServlet -->
  <servlet>
    <servlet-name>springmvc</servlet-name>
    <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
    <init-param>
        <!--init时的参数，无则默认加载/WEB-INF/servlet名称-servlet.xml-->
        <param-name>contextConfigLocation</param-name>
        <!--springmvc.xml 自己创建的SpringMVC全局配置文件-->
        <param-value>classpath:springmvc.xml</param-value>
    </init-param>
  </servlet>

  <servlet-mapping>
    <servlet-name>springmvc</servlet-name>
    <!--配置1：*.do,还可以写*.action等等，表示以.do结尾的或者以.action结尾的URL都由前端控制器DispatcherServlet来解析
        配置2：/,所有访问的 URL 都由DispatcherServlet来解析，但是这里最好配置静态文件不由DispatcherServlet来解析
    -->
    <url-pattern>*.do</url-pattern>
  </servlet-mapping>
</web-app>
```

## 处理适配器

> 根据请求的url查找Handler  
> 在springmvc.xml中配置，约束Handler类


```xml
<!--配置1: 编写Handler时必须实现Controller-->
<bean class="org.springframework.web.servlet.mvc.SimpleControllerHandlerAdapter" />

<!--配置2: 编写Handler时必须实现 HttpRequestHandler-->
<bean class="org.springframework.web.servlet.mvc.HttpRequestHandlerAdapter" />
```

## Handler

> ~ Controller

### 方法1：实现Controller接口  

```java
package com.ys.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.Controller;

public class HelloController implements Controller{

    @Override
    public ModelAndView handleRequest(HttpServletRequest request,
            HttpServletResponse response) throws Exception {
        ModelAndView modelView = new ModelAndView();
        //类似于 request.setAttribute()
        modelView.addObject("name","张三");
        modelView.setViewName("/WEB-INF/view/index.jsp");
        return modelView;
    }

}
```

### 方法2：实现 HttpRequestHandler 接口  

```java
package com.ys.controller;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.HttpRequestHandler;

public class HelloController2 implements HttpRequestHandler{

    @Override
    public void handleRequest(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        request.setAttribute("name", "张三");
        request.getRequestDispatcher("/WEB-INF/view/index.jsp").forward(request, response);
    }

}
```