### Questions
Java Bean?
J2EE?
面向切片编程?

### Concepts
* 非侵入式设计 无需继承框架提供的任何类
* JavaBean 特殊Java类，遵循JavaBean API规范
> 1. 提供默认*无参*构造函数
> 2. 实现Serilizable接口，可被序列化
> 3. 可能有一系列读写属性
> 4. 可能有getter, setter
* POJO: Plain Ordinary Java Objects
> 没有业务逻辑 ~ value object | Data transfer object ~ JavaBean

**what can spring do**
> 根据配置文件 创建、组装对象间依赖关系  
> 面向切片编程  
>> 无耦合实现 日志记录，性能统计，安全控制
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

### Spring IoC, DI
IoC = Inverse of Control 控制反转
> 一种设计思想：将原本手动创建对象的控制权交由Spring管理  
DI = Dependency Injection 依赖注入  
> 将对象依赖属性由配置设值给该对象 -> 从new转变为由IOC创建
#### 创建对象的方式
先创建测试类 -> testBean
1. **用默认构造方法**
/src -> applicationContext.xml => spring配置文件
> <bean id="testBean", class="classPath"></bean>
> <alias name="testBean" alias="testAlias" />
使用
```
ApplicationContext context = new ClassPathXmlApplicationContext("applicationContext.xml")
testBean test = (testBean) context.getBean("testBean")
test.display();
```
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
3. **实例工厂**
创建实例工厂类 testBeanInstanceFactory
> 实现 public testBean getInstance(){ return new testBean; }
applicationContext.xml
```
<bean id="instanceFactory" class="classPath+name"></bean>  
<bean id="instance" factory-bean="instanceFactory" factory-method="getInstance"></bean>
```

#### Spring AOP 面向切片编程
Aspect Oriented programming
**思想**
功能分为
> 核心业务 登陆，增删改查  
> 周边功能 性能统计，日志，事务管理 = 切面
两功能独立开发，切面+核心业务 = AOP
**目的**
封装与业务无关。但为业务模块共同调用的逻辑、责任封装，去重减耦，增加扩展维护性