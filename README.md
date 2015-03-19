# gtRPC
project 3 of GT course CS6210 ---- RPC-Based Proxy Server

I may put the following words in the report.  

#### structure of the code
All code is contained in folder src  
* proxy.thrift : use thrift to generate proxy frame work  
* ProxyServer_client.cpp: the client code
* ProxyServer_server.cpp: the server code
* cache.h:  define the cache policy class
* lru.cpp:  implement functions in cache.h to obtain LRU cache policy

So we only to implement the Cache class defined in cache.h to get 
different cache policies. 

##work flow

####Xiong Ding: 
1. test the thrift "hello word" program
2. write the proxy server/client program
3. write the cache LRU policy
4. Next => write the report and wait Yuebin Zhou to finish his part

####Yuebin Zhou
1. write the other two policies
2. write the measurement metrics (calculate performance)
3. implement URL list for the client, implement different overload patterns.

after all is done, we do the experiments and finish the report.

##Useful links

http://wiki.apache.org/thrift/ThriftUsageC%2B%2B

http://www.thrift.pl/Thrift-tutorial-how-it-works.html

http://thrift-tutorial.readthedocs.org/en/latest/usage-example.html

* libcurl tutorial   
http://curl.haxx.se/libcurl/c/libcurl-tutorial.html    
a useful example  
http://curl.haxx.se/libcurl/c/getinmemory.html

* LRU Cache   (I followed the following link to implement LRU)
http://www.hawstein.com/posts/lru-cache-impl.html   

build thrift from source file (linux)
====================
I compile and install in my desktop. It requires boost library to support C++.
I installed boost-1.57 in my home directory. Also I need to make sure that
thrift can find the location of boost.

For example, my configure options:
```
./configure --prefix=/usr/local/home/xiong/apps/thrift 
JAVA_PREFIX=/usr/local/home/xiong/apps/thrift 
PY_PREFIX=/usr/local/home/xiong/apps/thrift 
PHP_PREFIX=/usr/local/home/xiong/apps/thrift 
--with-boost-libdir=/usr/local/home/xiong/apps/boost/lib 
--with-boost=/usr/local/home/xiong/apps/boost/

make

make install
```
After installation, add "thrift/include" folder to enviroment variable
"C_INCLUDE_PATH", add "thrift/lib" folder to enviroment variable 
"LD_LIBRARY_PATH" and "LIBRARY_PATH".
