#!/usr/local/bin/thrift --gen cpp

namespace cpp RPC

service ProxyServer {
  // return the webpage content given the page address
  string getPage(1:string url)
}