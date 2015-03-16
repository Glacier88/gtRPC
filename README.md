# gtRPC
project 3 of GT course CS6210 ---- RPC-Based Proxy Server

##Useful links

http://wiki.apache.org/thrift/ThriftUsageC%2B%2B

http://www.thrift.pl/Thrift-tutorial-how-it-works.html

http://thrift-tutorial.readthedocs.org/en/latest/usage-example.html

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
