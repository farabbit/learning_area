# python network programming

## demo

server

```python
import socket
# server
sk=socket.socket()
sk.bind(('127.0.0.1',8998)) # bind listening addr
sk.listen()
conn,addr = sk.accept()
ret = conn.recv(1024)
print(ret)
conn.send('HI'.encode())
conn.close()
sk.close()
```

client

```python
import socket
# client
sk = socket.socket()
sk.connect(('127.0.0.1',8898)) # 尝试连接
sk.send('hello!'.encode())
ret = sk.recv(1024) # 
print(ret)
sk.close()
```
