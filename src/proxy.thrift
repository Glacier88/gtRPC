#!/usr/local/bin/thrift --gen cpp

namespace cpp RPC

struct sendData {
       1: bool doesSucceed,
       2: string webcontent,
}

service ProxyServer {
  // return the webpage content given the page address
  sendData getPage(1:string url)
}