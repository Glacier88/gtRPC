GEN_SRC := ProxyServer.cpp proxy_constants.cpp proxy_types.cpp
GEN_OBJ := $(patsubst %.cpp,%.o, $(GEN_SRC))

SERVER=ProxyServer_server
CLIENT=ProxyServer_client

.PHONY: all clean

all: $(SERVER) $(CLIENT)

%.o: %.cpp
	$(CXX) -Wall -std=c++11 -DHAVE_INTTYPES_H -DHAVE_NETINET_IN_H  -c $< -o $@

$(SERVER): $(SERVER:=.o) $(GEN_OBJ)
	$(CXX) $^ -o $@  -lthrift -lcurl

$(CLIENT): $(CLIENT:=.o) $(GEN_OBJ)
	$(CXX) $^ -o $@  -lthrift 

clean:
	$(RM) *.o $(CLIENT) $(SERVER)