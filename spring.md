### Questions
Java Bean?
J2EE?
面向切片编程?

## Concepts
* 非侵入式设计 无需继承框架提供的任何类
* JavaBean 特殊Java类，遵循JavaBean API规范
> 1. 提供默认*无参*构造函数
> 2. 实现Serilizable接口，可被序列化
> 3. 可能有一系列读写属性
> 4. 可能有getter, setter
* POJO: Plain Ordinary Java Objects
> 没有业务逻辑 ~ value object | Data transfer object ~ JavaBean  

**what can spring do**
> 根据配置文件, 创建、组装对象间依赖关系  
> 面向切片编程 -> 无耦合实现 日志记录，性能统计，安全控制  
> 管理数据库事务  
> 第三方数据访问框架 - Hibernate, JPA - 提供了JDBC访问模板  
> 无缝集成第三方Web框架 - 且提供了Spring MVC  
> 方便与Java EE整合  

### Structure
**Data Access/Integration层** -> JDBC, ORM, OXM, JMS, Transaction  
**Web层** -> Web, Web-Servlet, WebSocket, Web-Porlet  
**AOP层** -> 符合AOP联盟便准的面向切片编程实现  
**Core Container** -> Beans, Core, Context, SpEL
**Test模块** -> JUnit, TestNG  

# Spring IoC, DI
IoC = Inverse of Control 控制反转
> 一种设计思想：将原本手动创建对象的控制权交由Spring管理  
DI = Dependency Injection 依赖注入  
> 将对象依赖属性由配置设值给该对象 -> 从new转变为由IOC创建  
### 创建对象的方式
先创建测试类 -> testBean
1. **用默认构造方法**
/src -> applicationContext.xml => spring配置文件  
```
<bean id="testBean", class="classPath"></bean>
<alias name="testBean" alias="testAlias" />  
```
使用  
```
ApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml")
testBean test = (testBean) context.getBean("testBean")
test.display();
```
<br/>

2. **静态工厂**
创建静态工厂类 testBeanStaticFactory
> 实现 public static testBean getInstance(){ return new testBean; }  
applicationContext.xml
> <bean id="testBeanStaticFactory" factory-method="getInstance" class="FactoryClassPath"></bean>  
使用  
```
ApplicationContext context = new ClassPathXmlApplicationContex("applicationContext.xml");
testBean staticFactory = (testBean) context.getBean("testBeanStaticFactory");
staticFactory.display();
```
<br/>

3. **实例工厂**
创建实例工厂类 testBeanInstanceFactory  
> 实现 public testBean getInstance(){ return new testBean; }  
applicationContext.xml  
```
<bean id="instanceFactory" class="classPath+name"></bean>  
<bean id="instance" factory-bean="instanceFactory" factory-method="getInstance"></bean>
```
<br/>

### 创建对象的时机
*TODO*
<br/>

### bean中scope
singleton/prototype/request/session/global session  
*TODO*
<br/>

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
3. @Resource，按照名称装配
需要别的类作为属性时，需要加@Resource(name="xxx")
4. @Autowired，按照类型装配
*TODO*





# Spring AOP 面向切片编程
Aspect Oriented programming  
**思想**
解剖开封装对象的内部，将影响多个类的公共行封装到可重用模块，命名为Aspect=切面  
功能分为  
> 核心业务 登陆，增删改查  
> 周边功能 性能统计，日志，事务管理 = 切面  
两功能独立开发，切面+核心业务 = AOP  
**目的**
封装与业务无关。但为业务模块共同调用的逻辑、责任封装，去重减耦，增加扩展维护性
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
* > 实现类，实现接口
* > [事务类，实现before(), after() -> printSth]
* > 代理类，将实现类作为属性，实现接口调用实现类的函数->可前拦截、后拦截
缺点  
代理类要实现与目标对象一样的接口，代理类繁多、不易维护，接口增加方法时，对象和代理类都要维护
2. **JDK动态代理**
动态地在内存中构建代理对象（制定目标对象接口类型），利用JDK的API生成指定接口对象
代理类
```java
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;

import packagePath.myTransaction; // 事务类 -> 处理逻辑外事务，如output

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


总结：
依赖注入：松耦合，装配
AOP：将事务与目标类分离，配置切面

有需要用到的类，在xml中加一条就行了
有耦合关系，在xml中配置



模板
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
> @Component
3. 定义配置类CDPlayConfig并启用组建扫描
> @Configuration  
> @ComponentScan -> 类中未显式声明类时，扫描当前包  
或者通过XML启用  
```xml
<context:component-scan base-package="packageName"/>
```=
