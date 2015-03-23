#include "ProxyServer.h"
#include <thrift/transport/TSocket.h>
#include <thrift/transport/TBufferTransports.h>
#include <thrift/protocol/TBinaryProtocol.h>

#include <iostream>
#include <cstdio>
#include <fstream>
#include <sys/time.h>
#include <string>
using namespace apache::thrift;
using namespace apache::thrift::protocol;
using namespace apache::thrift::transport;

using namespace ::RPC;
using namespace std;

typedef unsigned long long my_time_t;
my_time_t get_time()
{
	struct timeval time;
	gettimeofday(&time,NULL);
	return time.tv_usec+(my_time_t)time.tv_sec*1000000;
}
int main(int argc, char **argv) {
  const char* addr;
  const char* file;
  if(argc==3)
  {
	addr=argv[1];//not used yet
	file=argv[2];
  }
  boost::shared_ptr<TSocket> socket(new TSocket(addr, 9090));
  boost::shared_ptr<TTransport> transport(new TBufferedTransport(socket));
  boost::shared_ptr<TProtocol> protocol(new TBinaryProtocol(transport));

  ProxyServerClient client(protocol);
  
  //read the work load
  string line;
  ifstream inputfile(file);
  //test
  my_time_t total_time=0;
  size_t numPages = 1;
  if(inputfile.is_open())
  {
     while(getline(inputfile,line))
	 {
		  transport->open();
		  string url(line);
		  sendData result;
		  my_time_t start=get_time();
		  client.getPage(result, url);
                  my_time_t end=get_time();
                  total_time+=end-start;
		  cout << result.webcontent << endl;;
		  fprintf(stderr, "Succeed getting the %zd th webpage ? %d\n", 
			  numPages++, result.doesSucceed);
		  transport->close();
	  }
  }
  else
  {
	cout<<"Couldn`t open workload"<<endl;
	return 1;
  }
  fprintf(stderr, "Total time: %llu\n", total_time);
  return 0;
}
