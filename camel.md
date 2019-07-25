# camel

Routing-engine builder

## Getting started

### CamelContext

represents the **Camel Runtime System**, typically have one **Camel Context** object in an application

Typical application executes the following steps

1. Create **Camel Context** obejct
2. Add **Endpoites**, and possibly Components
3. Add **routes** to CamelContext obj to connect the endpoints
4. Invoke **start()** on CamelContext obj -> starts Camel-internal threads used to process sending, receiving, processing of message.
5. Invoke **stop()** on CamelContext obj

* start()会逐个打开所有线程后再returns
* stop()会等所有线程结束后再return

### Endpoint

CORBA
= Common Object Request Broker Architecture 公共请求代理体系结构
= 面向对象应用程序体系规范
= 面向对象的远程过程调用中间件标准
= 解决分布式处理环境中，硬件软件互联的解决方案

IOR = Logical address in CORBA

* Physical address (host:port)
* logical address (host:port + id)

### URI

* URN = Unique Resource Name = urn:scheme-name:unique=identifier

### Component

~ Endpoint Factory

### Message, Exchange

**Message**:  Provides abstraction for single message
Concrete classes: eg: JmsMessage provides JMS-specific implementation of that interface

### Processor

### ROUTE

A step-by-step movement of a Message from an input queue through decision making to a destination queue

XML
JAVA DSL

## example

```java
package com.yinwenjie.test.cameltest.helloworld;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import org.apache.camel.Exchange;
import org.apache.camel.ExchangePattern;
import org.apache.camel.Message;
import org.apache.camel.Processor;
import org.apache.camel.builder.RouteBuilder;
import org.apache.camel.component.http.HttpMessage;
import org.apache.camel.impl.DefaultCamelContext;
import org.apache.camel.model.ModelCamelContext;
/**
* 郑重其事的写下 helloworld for Apache Camel
* @author yinwenjie
*/
public class HelloWorld extends RouteBuilder {
    public static void main(String[] args) throws Exception {
        // camel上下文对象，驱动整个路由
        ModelCamelContext camelContext = new DefaultCamelContext();
        // 启动route
        camelContext.start();
        // 将我们编排的完整消息路由过程，加入到上下文中
        camelContext.addRoutes(new HelloWorld()); // HelloWorld IS A RouteBuilder
        /*
        * ==========================
        * 为什么我们先启动一个Camel服务
        * 再使用addRoutes添加编排好的路由呢？
        * 这是为了告诉各位读者，Apache Camel支持动态加载/卸载编排的路由
        * 这很重要，因为后续设计的Broker需要依赖这种能力
        * ==========================
        * */
        // 通用没有具体业务意义的代码，只是为了保证主线程不退出
        synchronized (HelloWorld.class) {
            HelloWorld.class.wait();
        }
    }
    @Override
    public void configure() throws Exception {
        // 在本代码段之下随后的说明中，会详细说明这个构造的含义
        from("jetty:http://0.0.0.0:8282/doHelloWorld")
        .process(new HttpProcessor())
        .to("log:helloworld?showExchangeId=true");
    }
    /**
    * 这个处理器用来完成输入的json格式的转换
    * @author yinwenjie
    */
    public class HttpProcessor implements Processor {
        /* (non-Javadoc)
        * @see org.apache.camel.Processor#process(org.apache.camel.Exchange)
        */
        @Override
        public void process(Exchange exchange) throws Exception {
            // 因为很明确消息格式是http的，所以才使用这个类
            // 否则还是建议使用org.apache.camel.Message这个抽象接口
            HttpMessage message = (HttpMessage)exchange.getIn();
            InputStream bodyStream = (InputStream)message.getBody();
            String inputContext = this.analysisMessage(bodyStream);
            bodyStream.close();
            // 存入到exchange的out区域
            if(exchange.getPattern() == ExchangePattern.InOut) {
                Message outMessage = exchange.getOut();
                outMessage.setBody(inputContext + " || out");
            }
        }
        /**
        * 从stream中分析字符串内容
        * @param bodyStream
        * @return
        */
        private String analysisMessage(InputStream bodyStream) throws IOException {
            ByteArrayOutputStream outStream = new ByteArrayOutputStream();
            byte[] contextBytes = new byte[4096];
            int realLen;
            while((realLen = bodyStream.read(contextBytes , 0 ,4096)) != -1) {
                outStream.write(contextBytes, 0, realLen);
            }
            // 返回从Stream中读取的字串
            try {
                return new String(outStream.toByteArray() , "UTF-8");
            } finally {
                outStream.close();
            }
        }
    }
}
```

### example 2

```java
package com.yinwenjie.test.cameltest.helloworld;
import org.apache.camel.builder.RouteBuilder;
import org.apache.camel.impl.DefaultCamelContext;
import org.apache.camel.model.ModelCamelContext;

/**
* 测试两个路由的连接
* @author yinwenjie
*/
public class DirectCamel {

    public static void main(String[] args) throws Exception {
        // 这是camel上下文对象，整个路由的驱动全靠它了。
        ModelCamelContext camelContext = new DefaultCamelContext();
        // 启动route
        camelContext.start();
        // 首先将两个完整有效的路由注册到Camel服务中
        camelContext.addRoutes((new DirectCamel()).new DirectRouteA());
        camelContext.addRoutes((new DirectCamel()).new DirectRouteB());

        // 通用没有具体业务意义的代码，只是为了保证主线程不退出
        synchronized (DirectCamel.class) {
            DirectCamel.class.wait();
        }
    }

    /**
    * DirectRouteA 其中使用direct 连接到 DirectRouteB
    * @author yinwenjie
    */
    public class DirectRouteA extends RouteBuilder {

        /* (non-Javadoc)
        * @see org.apache.camel.builder.RouteBuilder#configure()
        */
        @Override
        public void configure() throws Exception {
        from("jetty:http://0.0.0.0:8282/directCamel")
            // 连接路由：DirectRouteB
            .to("direct:directRouteB")
            .to("log:DirectRouteA?showExchangeId=true");
        }
    }

    /**
    * @author yinwenjie
    */
    public class DirectRouteB extends RouteBuilder {
        /* (non-Javadoc)
        * @see org.apache.camel.builder.RouteBuilder#configure()
        */
        @Override
        public void configure() throws Exception {
            from("direct:directRouteB")
            .to("log:DirectRouteB?showExchangeId=true");
        }
    }
}
```

### example 3

```java
package com.yinwenjie.test.cameltest.helloworld;
......
/**
* 使用条件选择进行路由编排
* @author yinwenjie
*/
public class ChoiceCamel extends RouteBuilder {

    public static void main(String[] args) throws Exception {
        // 这是camel上下文对象，整个路由的驱动全靠它了。
        ModelCamelContext camelContext = new DefaultCamelContext();
        // 启动route
        camelContext.start();
        // 将我们编排的一个完整消息路由过程，加入到上下文中
        camelContext.addRoutes(new ChoiceCamel());

        // 通用没有具体业务意义的代码，只是为了保证主线程不退出
        synchronized (ChoiceCamel.class) {
            ChoiceCamel.class.wait();
        }
    }

    @Override
    public void configure() throws Exception {
        // 这是一个JsonPath表达式，用于从http携带的json信息中，提取orgId属性的值
        jsonPathExpression = new JsonPathExpression("$.data.orgId");
        jsonPathExpression.setResultType(String.class);

        // 通用使用http协议接受消息
        from("jetty:http://0.0.0.0:8282/choiceCamel")
        // 首先送入HttpProcessor，
        // 负责将exchange in Message Body之中的stream转成字符串
        // 当然，不转的话，下面主要的choice操作也可以运行
        // HttpProcessor中的实现和上文代码片段中的一致，这里就不再重复贴出
        .process(new HttpProcessor())
        // 将orgId属性的值存储 exchange in Message的header中，以便后续进行判断
        .setHeader("orgId", jsonPathExpression)
        .choice()
        // 当orgId == yuanbao，执行OtherProcessor
        // 当orgId == yinwenjie，执行OtherProcessor2
        // 其它情况执行OtherProcessor3
        .when(header("orgId").isEqualTo("yuanbao"))
        .process(new OtherProcessor())
        .when(header("orgId").isEqualTo("yinwenjie"))
        .process(new OtherProcessor2())
        .otherwise()
        .process(new OtherProcessor3())
        // 结束
        .endChoice();
    }

    /**
    * 这个处理器用来完成输入的json格式的转换
    * 和上一篇文章出现的HttpProcessor 内容基本一致。就不再贴出了
    * @author yinwenjie
    */
    public class HttpProcessor implements Processor {
        ......
    }

    /**
    * 另一个处理器OtherProcessor
    * @author yinwenjie
    */
    public class OtherProcessor implements Processor {

        @Override
        public void process(Exchange exchange) throws Exception {
            Message message = exchange.getIn();
            String body = message.getBody().toString();

            // 存入到exchange的out区域
            if(exchange.getPattern() == ExchangePattern.InOut) {
                Message outMessage = exchange.getOut();
                outMessage.setBody(body + " || 被OtherProcessor处理");
            }
        }
    }

    /**
    * 很简单的处理器OtherProcessor2
    * 和OtherProcessor基本相同，就不再重复贴出
    * @author yinwenjie
    */
    public class OtherProcessor2 implements Processor {
        ......
        outMessage.setBody(body + " || 被OtherProcessor2处理");
    }

    /**
    * 很简单的处理器OtherProcessor3
    * 和OtherProcessor基本相同，就不再重复贴出
    * @author yinwenjie
    */
    public class OtherProcessor3 implements Processor {
        ......
        outMessage.setBody(body + " || 被OtherProcessor3处理");
    }
}
```