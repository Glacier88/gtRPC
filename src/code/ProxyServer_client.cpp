#include "ProxyServer.h"
#include <thrift/transport/TSocket.h>
#include <thrift/transport/TBufferTransports.h>
#include <thrift/protocol/TBinaryProtocol.h>

#include <iostream>
#include <cstdio>
using namespace apache::thrift;
using namespace apache::thrift::protocol;
using namespace apache::thrift::transport;

using namespace ::RPC;
using namespace std;

int main(int argc, char **argv) {
  boost::shared_ptr<TSocket> socket(new TSocket("localhost", 9090));
  boost::shared_ptr<TTransport> transport(new TBufferedTransport(socket));
  boost::shared_ptr<TProtocol> protocol(new TBinaryProtocol(transport));

  ProxyServerClient client(protocol);
  transport->open();

  string url("https://www.yahoo.com/");
  sendData result;
  client.getPage(result, url);

  cout << result.webcontent << endl;;
  fprintf(stderr, "%d\n", result.doesSucceed);
  transport->close();

  return 0;
}
