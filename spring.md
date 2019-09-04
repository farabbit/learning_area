# spring

Java Bean?  
J2EE?  
面向切片编程?

## w3school

### framework

![Spring Framework](https://7n.w3cschool.cn/attachments/image/wk/wkspring/arch1.png)

* Core container
  1. spring-core => 框架基础, 包括IoC和DI
  2. spring-beans => 提供BeanFactory, 移除编码式单例, 把配置和依赖从实际编码逻辑中解耦
  3. spring-context => 建立在core与beans上, 提供类似JNDI注册方式访问对象, 继承Bean
      > ApplicationContext是Context的焦点
  4. spring-context-support => 提供第三方继承库到spring context的支持
  5. spring-expression
* Data Access/Integration
  1. JDBC
  2. ORM => 提供对流行对象关系映射API的集成
      > 如JPA, JDO, Hibernate, 可与spring其他功能整合
  3. OXM => 提供对OXM实现的支持
      > 如JAXB, Castor, XML Beans, JiBX, XStream
  4. JMS => 包含生产（produce）和消费（consume）消息的功能
  5. Transactions事务 => 为实现特殊接口类及POJO支持编程式和声明式事务管理
      > * 声明式：通过注解或配置由spring自动配置
      > * 编程式：自己写beginTransaction(), commit(), rollback()等, 粒度更细
* Web
  1. Web => 提供面向web的基本功能和面向web的应用上下文
      > multipart文件上传、用Servlet监听器初始化IoC容器, 以及HTTP客户端和Spring远程调用中web部分.
  2. Web-MVC => 模块为web应用提供MVC和REST服务的实现
      > Spring MVC可完全分离领域模型代码和web表单, 且可与Spring框架的其它所有功能集成.
  3. Web-Socket => 为WebSocket-based提供了支持, 而且在web应用中提供C/S间通信的两种方式.
  4. Web-Portlet => 提供用于Portlet环境的MVC实现, 反映了spring-web-mvc的功能
* 其他
  1. AOP => 提供面向方面的实现
      > 允许定义方法拦截器、切入点对代码解耦
  2. Aspects => 提供与AspetJ的集成
  3. Instrumentation
  4. Messaging

### IoC容器

---

IoC控制反转：将new交由Spring容器

容器创建、连接、配置、管理对象. Spring容器用DI来管理组成应用程序的组建：Spring Beans.

* BeanFacotory容器
  > 由org.springframework.beans.factory.BeanFactory接口定义.   
  > BeanFactory或相关接口, 如BeanFactoryAware, InitializingBean, DisposableBean在Spring中仍然存在具大量与 Spring 整合的第三方框架反向兼容性的目的.
* ApplicationContext容器
  > 由org.springframework.context.ApplicationContext定义  
  > 包括BeanFactory所有功能

#### BeanFactory

对BeanFactory接口的实现：XmlBeanFactory
资源宝贵的设备中一般用BeanFacotry, 否则一般用ApplicationContext

#### ApplicationContext

BeanFacotry的子接口

常用ApplicationContext接口实现

* FileSystemXmlApplicationContext：从XML中加载bean. 需要提供给构造器 XML 文件的完整路径.
* ClassPathXmlApplicationContext：从XML. . 中加载bean. 不需要提供XML完整路径, 只需配置 CLASSPATH环境变量, 容器会从CLASSPATH中搜索bean配置文件.
* WebXmlApplicationContext：容器会在web应用程序范围内加载在XML中已被定义的bean

### Bean

bean = 被实例化, 组装, 并通过Spring IoC容器所管理的对象
由配置元数据(Meta-data)创建

| property                 | description                                                                    |
| :----------------------- | :----------------------------------------------------------------------------- |
| class                    | 强制性的, 指定用来创建bean的bean类                                             |
| name                     | 指定唯一bean标识符. 在基于XML的配置元数据中, 可用ID和/或name属性指定bean标识符 |
| scope                    | 指定由特定bean定义创建对象的作用域                                             |
| lazy-initialization mode | 延迟初始化的bean, 告诉IoC容器在它第一次被请求时, 而非启动时创建bean实例        |
| initialization (method)  | 在 bean 的所有必需的属性被容器设置之后, 调用回调方法                           |
| destruction (method)     | 当包含该 bean 的容器被销毁时, 使用回调方法                                     |
| constructor-arg          | 用来注入依赖关系                                                               |
| properties               | 用来注入依赖关系                                                               |
| autowiring mode          | 用来注入依赖关系                                                               |

配置元数据

* XML
* Anotation
* Java

#### Bean作用域

| scope          | description                                                                                  |
| :------------- | :------------------------------------------------------------------------------------------- |
| singleton      | Bean以单例方式存在                                                                           |
| prototype      | 每次从容器调用Bean时, 都返回新实例, 即每次调用getBean()时, 相当于执行newXxxBean()            |
| request        | 每次HTTP请求都会创建新Bean, 该作用域仅适用于WebApplicationContext环境                        |
| session        | 同一个HTTP Session共享一个Bean, 不同Session使用不同的Bean, 仅适用于WebApplicationContext环境 |
| global-session | 一般用于Portlet应用环境, 该域仅适用于WebApplicationContext环境                               |

#### 生命周期

* init
  * JAVA: 实现org.springframework.beans.factory.InitializingBean并实现afterPropertiesSet()
  * XML: init-method="method_name"
* destroy
  * JAVA: 实现org.springframework.beans.factory.DisposableBean并实现destroy()
  * XML: destroy-method="method_name"

#### 继承

* parent="parent_name"

### DI

---

* Constructor based

    ```xml
    <!--引用：ref-->
    <constructor-arg ref="spellChecker"/>
    <!--值：value-->
    <constructor-arg type="java.lang.String" value="Zara"/>
    ```

* Setter based

    ```xml
    <!--in java: setter is needed-->
    <property name="spellChecker" ref="spellChecker"/>
    <!--传递null值-->
    <property name="email"><null/></property>
    ```

* Inner beans 内部bean类

    ```xml
    <property name="spellChecker">
      <bean id="spellChecker" class="com.tutorialspoint.SpellChecker"/>
    </property>
    ```

* Collection 集合

    ```xml
    <!--in java: setters of List, Set, Map, Properties are needed-->
    <!--list-->
    <property name="addressList">
      <list>
        <value>INDIA</value>
        <value>Pakistan</value>
      </list>
    </property>
    <!--set-->
    <property name="addressSet">
      <set>
        <value>INDIA</value>
        <value>Pakistan</value>
      </set>
    </property>
    <!--map-->
    <property name="addressMap">
      <map>
        <entry key="1" value="INDIA"/>
        <entry key="2" value="Pakistan"/>
      </map>
    </property>
    <!--props-->
    <property name="addressProp">
      <props>
        <prop key="one">INDIA</prop>
        <prop key="two">Pakistan</prop>
      </props>
    </property>
    ```

### 自动装配

减少编写XML, 使用bean的autowire定义自动装配模式
| autowire    | description                                                                    |
| :---------- | :----------------------------------------------------------------------------- |
| no          | 无自动装配                                                                     |
| byName      | 由属性名装配                                                                   |
| byType      | 由属性数据类型配                                                               |
| constructor | 类似byType, 但适用构造函数参数类型. 若容器中无构造函数参数类型的bean, 则会报错 |
| autodetect  | 先尝试constructor自动装配, 若不执行则尝试通过byType装配                        |

```xml
<bean id="textEditor" class="com.tutorialspoint.TextEditor" 
      autowire="byName">
      <property name="name" value="Generic Text Editor" />
</bean>
```

* byName / byType / byConstructor

由属性名/属性类型/构造函数参数列表指定自动装配

```xml
<bean id="textEditor" class="com.tutorialspoint.TextEditor" autowire="byName"><!--or byType--><!--or byConstrucor-->
    <!--property spellCheck will be automaticly be wired-->
    <property name="name" value="Generic Text Editor" />
</bean>
<bean id="spellChecker" class="com.tutorialspoint.SpellChecker" />
```

### Annotation

---

config file

```xml
<?xml version="1.0" encoding="UTF-8"?>

<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:context="http://www.springframework.org/schema/context"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans-3.0.xsd
    http://www.springframework.org/schema/context
    http://www.springframework.org/schema/context/spring-context-3.0.xsd">

   <context:annotation-config/>
   <!-- bean definitions go here -->

</beans>
```

#### @Required

bean必须设置此属性

#### @Autowired

可注释setter方法或属性

#### @Quolifier

创建多个相同类型的bean自动装配时可能会引起歧义, 使用@Qualifier可消除混乱

```java
@Autowired
@Qualifier("student1")
Private Student student;
```

```xml
<bean id="student1" class="Student">
```

#### Spring JSR-250注释

##### @PostConstruct, @PreDestroy

```java
   @PostConstruct
   public void init(){ System.out.println("Bean is going through init."); }
   @PreDestroy
   public void destroy(){ System.out.println("Bean will destroy now."); }
```

```xml
<bean id="helloWorld" 
    class="com.tutorialspoint.HelloWorld"
    init-method="init" destroy-method="destroy">
    <property name="message" value="Hello World!"/>
</bean>
```

##### @Resource

~ byName

```java
@Resource(name="spellChecker")
public void setSpellChecker( SpellChecker spellChecker ){ this.spellChecker = spellChecker; }
```

#### 基于Java的配置

##### @Configuration / @Bean

```java
@Configuration
public class HelloWorldConfig {
    @Bean
    public HelloWorld helloworld(){
        return new HelloWorld();
    }
}
```

等同于如下配置

```xml
<beans>
    <bean id="helloWorld" class="com.tutorialspoint.HelloWorld" />
</beans>
```

可以使用AnnotationConfigApplicationContext

```java
public static void main(String[] args) {
   ApplicationContext ctx = new AnnotationConfigApplicationContext(HelloWorldConfig.class);
   HelloWorld helloWorld = ctx.getBean(HelloWorld.class);
   helloWorld.setMessage("Hello World!");
   helloWorld.getMessage();
}
```

##### @Import

从另一个配置类中加载

```java
@Configuration
public class ConfigA {
   @Bean
   public A a() {
      return new A(); 
   }
}

@Configuration
@Import(ConfigA.class)
public class ConfigB {
   @Bean
   public B a() {
      return new A(); 
   }
}
```

##### 生命周期回调

```java
public class Foo {
   public void init() {
      // initialization logic
   }
   public void cleanup() {
      // destruction logic
   }
}

@Configuration
public class AppConfig {
   @Bean(initMethod = "init", destroyMethod = "cleanup" )
   public Foo foo() {
      return new Foo();
   }
}
```

#### Spring事件处理

| Spring内置事件        | 描述                                                                                                                                                          |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ContextRefreshedEvent | ApplicationContext初始化或刷新时, 该事件发布. 也可在ConfigurableApplicationContext接口中用refresh()方法手动发生                                               |
| ContextStartedEvent   | 当用ConfigurableApplicationContext接口中start()启动ApplicationContext时, 该事件发布. 你可以调查你的数据库, 或者你可以在接受到这个事件后重启任何停止的应用程序 |
| ContextStoppedEvent   | 当用ConfigurableApplicationContext接口中stop()停止ApplicationContext时, 该事件发布. 可在接受到此事件后做清理工作                                              |
| ContextClosedEvent    | 当用ConfigurableApplicationContext接口中close()关闭ApplicationContext时, 该事件发布. 一个已关闭的上下文到达生命周期末端；它不能被刷新或重启                   |
| RequestHandledEvent   | web-specific事件, 告诉所有bean HTTP请求已被服务                                                                                                               |

Spring事件处理是单线程的, 除非所有接收者得到该消息, 否则进程被阻塞, 流程不会继续

#### 自定义事件

*TODO*
extends ApplicationEvent

### AOP Aspect Orientied Programming 面向切面编程

---

把程序逻辑分解成关注点, 提供**拦截器**在执行方法前后添加额外功能

术语

| nouns         | description                                                                                                   |
| :------------ | :------------------------------------------------------------------------------------------------------------ |
| Aspect        | 一个模块具有一组提供横切需求的APIs. 如日志模块为了记录日志将被 AOP aspect调用, 程序可以拥有任意数量的aspect   |
| Join point    | 在应用程序中代表一个点, 可在插件AOP方面. 你也能说, 它是在实际的应用程序中, 其中一个操作将使用 Spring AOP 框架 |
| Advice        | 实际行动前后执行的方法. 是在程序执行期间通过Spring AOP框架实际被调用的代码                                    |
| Pointcut      | 一组一个或多个连接点, 通知应该被执行. 可使用表达式或模式指定切入点                                            |
| Introduction  | 引用: 允许添加新方法或属性到现有类中                                                                          |
| Target object | 被一或多个aspect所通知的对象, 此对象永远是被代理对象, 也称为被通知对象                                        |
| Weaving       | Weaving 把aspect连接到其它的应用程序类型或对象, 并创建被通知的对象. 可在编译时, 类加载时, 运行时完成          |

通知类型

| 通知           | 描述                                             |
| :------------- | :----------------------------------------------- |
| 前置通知       | 在方法执行前, 执行通知                           |
| 后置通知       | 在方法执行后, 不考虑其结果, 执行通知             |
| 返回后通知     | 在方法执行后, 只方法成功完成后, 才执行通知       |
| 抛出异常后通知 | 在方法执行后, 只在方法退出抛出异常后, 才执行通知 |
| 环绕通知       | 在建议方法调用前后, 执行通知                     |

自定义aspect

* @AspectJ
* XML Schema based


config file

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:aop="http://www.springframework.org/schema/aop"
    xsi:schemaLocation="http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans-3.0.xsd 
    http://www.springframework.org/schema/aop 
    http://www.springframework.org/schema/aop/spring-aop-3.0.xsd ">

   <!-- bean definition & AOP specific configuration -->

</beans>
```

#### AOP based xml framework

```xml
<aop:config>
   <aop:aspect id="myAspect" ref="aBean">
   ...
   </aop:aspect>
</aop:config>
<bean id="aBean" class="...">
...
</bean>
```



## before

### Concepts

* 非侵入式设计 无需继承框架提供的任何类  
  
* JavaBean 特殊Java类, 遵循JavaBean API规范  
    > 1. 提供默认*无参*构造函数  
    > 2. 实现Serilizable接口, 可被序列化  
    > 3. 可能有一系列读写属性  
    > 4. 可能有getter, setter

* POJO: Plain Ordinary Java Objects  
    > 没有业务逻辑 ~ value object | Data transfer object ~ JavaBean

#### what can spring do

> 根据配置文件, 创建、组装对象间依赖关系  
> 面向切片编程 -> 无耦合实现 日志记录, 性能统计, 安全控制  
> 管理数据库事务  
> 第三方数据访问框架 - Hibernate, JPA - 提供了JDBC访问模板  
> 无缝集成第三方Web框架 - 且提供了Spring MVC  
> 方便与Java EE整合  

#### Structure

* Data Access/Integration层 -> JDBC, ORM, OXM, JMS, Transaction  
* Web层 -> Web, Web-Servlet, WebSocket, Web-Porlet  
* AOP层 -> 符合AOP联盟便准的面向切片编程实现  
* Core Container -> Beans, Core, Context, SpEL  
* Test模块 -> JUnit, TestNG  

# Spring IoC, DI

* IoC = Inverse of Control 控制反转  
  * 一种设计思想：将原本手动创建对象的控制权交由Spring管理
* DI = Dependency Injection 依赖注入  
  * 将对象依赖属性由配置设值给该对象 -> 从new转变为由IOC创建  

### 创建对象的方式

先创建测试类 -> testBean  
1. **用默认构造方法**  

/src -> applicationContext.xml => spring配置文件  

```xml
<bean id="testBean", class="classPath"></bean>  
<alias name="testBean" alias="testAlias" />  
```  

使用  

```java  
ApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml")  
testBean test = (testBean) context.getBean("testBean")  
test.display();  
```
  
1. **静态工厂**  

创建静态工厂类 testBeanStaticFactory
> 实现 public static testBean getInstance(){ return new testBean; } 

applicationContext.xml

```xml  
<bean id="testBeanStaticFactory" factory-method="getInstance" class="FactoryClassPath"></bean>  
```

使用

```java
ApplicationContext context = new ClassPathXmlApplicationContex("applicationContext.xml");  
testBean staticFactory = (testBean) context.getBean("testBeanStaticFactory");  
staticFactory.display();  
```  

1. **实例工厂**  

创建实例工厂类 testBeanInstanceFactory  
> 实现 public testBean getInstance(){ return new testBean; }  
applicationContext.xml  

```xml
<bean id="instanceFactory" class="classPath+name"></bean>  
<bean id="instance" factory-bean="instanceFactory" factory-method="getInstance"></bean>  
```  

### 创建对象的时机  
*TODO*  

### bean中scope  

singleton/prototype/request/session/global session  
*TODO*  

### 生命周期  
applicationContext.xml  
```xml  
<bean id="springLifeCycle" init-method="init" destroy-method="destroy" class="com.ys.ioc.SpringLifeCycle"></bean>  
```  
**life cycle**  
1. 创建对象  
2. init  
3. 自己的方法  
4. destroy (可以是关闭Application Context的时候)  
<br/>  


# Spring DI 依赖注入  
Dependency Injection = 通过反射实现依赖注入（给属性赋值）  
1. **利用set方法赋值**  
创建实体类Person -> 有Student类的属性  
> 若干属性  
> private Properties properties  
>> properties getter/setter  
在applicationContext.xml中赋值

```xml  
<bean id="person" class="classPath+Name">  
  <property name="pid" value="1"></property>  
  <property name="students">  
    <ref bean="student"/>  
  </property>  
  <property name="lists">  
    <list>  
      <value>1</value>  
      <ref bean="student"/>  
      <value>vae</value>  
    </list>  
  </property>  
</bean>  
```  

测试  

```java  
ApplicationContext contxt = ...  
Person person = (Person) context.getBean("person);  
System.out(person.getName());  
```  

2. **利用构造函数赋值**  

创建实体类Person, 带参构造函数

```xml  
<bean id="person_con" class="com.ys.di.Person">  
  <constructor-arg index="0" type="java.lang.Long" value="1"></constructor-arg>  
  <constructor-arg index="1" type="com.ys.di.Student" ref="student_con"></constructor-arg>  
</bean>  
<bean id="student_con" class="com.ys.di.Student"></bean>  
```  
测试  
```java  
ApplicationContext context = ...  
Person person = (Person) context.getBean("person_con");  
System.out.println(person.getPid());  
```  

# Annotation  
> applicationContextt.xml中引入命名空间  
> applicationContext.xml中引入注解扫描器  
```xml  
<context:component-scan base-package="com.ys.annotation"></context:component-scan>  
```  
> Person 类中添加注解@Component  
1. @Component  
2. @Repository, @Service, @Controller  
> * @Repository -> dao层  
> * @Servic -> service层  
> * @Controller -> web层  
3. @Resource, 按照名称装配  
需要别的类作为属性时, 需要加@Resource(name="xxx")  
4. @Autowired, 按照类型装配  
*TODO*  





# Spring AOP 面向切片编程  
Aspect Oriented programming  
**思想**  
解剖开封装对象的内部, 将影响多个类的公共行封装到可重用模块, 命名为Aspect=切面  
功能分为  
> 核心业务 登陆, 增删改查  
> 周边功能 性能统计, 日志, 事务管理 = 切面  

两功能独立开发, 切面+核心业务 = AOP  
**目的**   
封装与业务无关. 但为业务模块共同调用的逻辑、责任封装, 去重减耦, 增加扩展维护性  

**Concepts**  
> target 需被代理的类  
> Joinpoint 连接点 -> 可能被拦截到的方法  
> PointCut 切入点 -> 被增强的  
> advice 通知/增强代码 -> after, before等  
> Weaving 织入 -> 把增强advice应用到  
> proxy 代理类 -> pointcut+advice  
> aspect 切面 = pointcut+advice  

### 代理模式  
提供对目标对象的间接访问方式  
> 便于扩展目标对象功能  
> 便于为多人所用  

```mermaid  
graph LR;  
C[客户]-->|访问目标|P[代理对象]-->|访问目标|O[目标对象];  
C[客户]|代理对象|<--P[代理对象]|返回结果|<--O[目标对象];  
```  

1. **静态代理**  
* > 接口  
* > 实现类, 实现接口  
* > [事务类, 实现before(), after() -> printSth]  
* > 代理类, 将实现类作为属性, 实现接口调用实现类的函数->可前拦截、后拦截  
缺点  
代理类要实现与目标对象一样的接口, 代理类繁多、不易维护, 接口增加方法时, 对象和代理类都要维护  
1. **JDK动态代理**  
动态地在内存中构建代理对象（制定目标对象接口类型）, 利用JDK的API生成指定接口对象  
代理类  
```java  
import java.lang.reflect.InvocationHandler;  
import java.lang.reflect.Method;  
import java.lang.reflect.Proxy;  

import packagePath.myTransaction; // 事务类 -> 处理逻辑外事务, 如output  

public class ObjectInterceptor implements InvocationHandler{  
    private Object target; //目标类  
    private myTransaction transaction; //切面类（事务类)  

    public ObjectInterceptor(Object target, myTransaction transaction){ // 通过构造类赋值  
        this .target = target;  
        this.transaction = transaction;  
    }  

    @Override // 传入  
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable{  
        this.transaction.before(); // 开启事务  
        method.invoke(this.target, args);  
        this.transaction.after(); // 提交事务  
        return null;  
    }  
}  
```  

## 使用Sping AOP 面向切面编程  

applicationContext.xml  

```xml  
<bean id="userService" class="packagePath+Name"></bean> <!--目标类-->  
<bean id="transaction" class="packagePath+Name"></bean> <!--切面类-->  

<!--开始装配-->  
<aop:config><!--配置-->  
    <!--切入点表达式： 选择方法(返回值 包 类名.方法名(参数)) AspectJ语法-->  
    <aop:aspect ref="transaction">  
        <aop:pointcut expression="execution(* com.ys.aop.*.*(..))" id="myPointCut"/><!--定义切点-->  
        <aop:befor method="before" pointcut-ref="myPointCut"></aop:before>  
        <aop:after-running method="after" pointcut-ref="myPointCut"></aop:after-running>  
    </aop:aspect>  
</aop:config>  
```  
测试  
```java  
public void testAop(){  
        ApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml");  
        UserService useService = (UserService) context.getBean("userService");  
        useService.addUser(null);  
    }  
```  

* 总结：  
依赖注入：松耦合, 装配  
AOP：将事务与目标类分离, 配置切面  

有需要用到的类, 在xml中加一条就行了  
有耦合关系, 在xml中配置  


* 模板  
exp: JdbcTemplate  

### 应用上下文  
spring自带多个容器实现  
> Bean工厂=BeanFactory -> 太初级了 一般不用  
> 应用上下文  
* AnnotationConfigApplicationContext 从Java配置类中加载Spring A.C.  
* ClassPathXmlApplicationContext 从Java配置类中加载Spring Web A.C.  
* FileSystemXmlApplicationContext 从类路径下XML加载A.C.  
* AnnotationConfigWebApplicationContext 从文件系统下XML加载A.C.  
* XmlWebApplicationContext 从Web应用下XML加载A.C.  

### Bean生命周期  
* 实例化  
* 填充属性  
* BeanNameAware -> setBeanName() 【实现BeanNameAware接口时调用】传递Bean ID给setBeanName方法  
* BeanFactoryAware -> setBeanFactory() 【实现BeanFactoryAware接口时调用】传入BeanFactory容器实例  
* ApplicationContextAware -> ApplicationContext() 【实现ApplicationContextAware接口时调用】传入Bean所在应用上下文引用  
* BeanPostProcessor的预初始化方法 *TODO*  
* InitializingBean -> afterPropertiesSet()  
* 自定义初始化方法  
* BeanPostProcessor初始化后方法  
--------------------------------------------------------  
* Bean可使用  
--------------------------------------------------------  
* 容器关闭  
* DisposableBean -> destory()  
* 自定义销毁方法  


Spring模块  
1. 核心容器  
*TODO*  


# 自动化装配  
* 显式XML配置  
* 显式Java配置 -> JavaConfig  
* 隐式Bean发现机制+自动化装配 -> 建议  

## 自动化装配  
* Component scanning 组件扫描 -> 自动发现A.C.中的Bean  
* Autowiring 自动装配 -> 自动满足Bean间依赖  
1. 定义接口CompactDisc  
> @Component  
2. 定义实现类SgtPeppers implements CompactDisc  
3. 定义配置类CDPlayConfig并启用组建扫描  
> @Configuration  
> @ComponentScan -> 类中未显式声明类时, 扫描当前包  
或者通过XML启用  
```xml  
<context:component-scan base-package="packageName"/>  
```  
### Bean注解  

* @Autowired 自动寻找匹配, 可以对应函数或属性  
*TODO*  

## 利用Java代码装配

### +@Configuration
在JavaConfig中声明Bean

```java
@Bean
public CompactDisc sgtPeppers(){ return new SgtPeppers(); }
```

@Bean表示会返回一个对象

注入

```java
@Bean
public CDPlayer cdPlayer(){ return new CDPlayer(SgtPeppers()); }
```

# Spring高级装配

## 环境、Profile

### profile bean

将在不同环境运行的bean整理入profile中 -> 使用@Profile注解指定bean输入哪一个profile
