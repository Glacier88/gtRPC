#include <unordered_map>
#include <iostream>
#include <cstdio>

//const size_t MaxSize = 1 << 20; // 1M

//page Structure
typedef struct {
  char *data;
  size_t size; // allocated size
  size_t len;  // actual length of array
} webpage;

typedef struct _Node {
  std::string url; 		/* key */
  webpage wp;      		/* data */
  _Node *prev, *next;
} Node;

typedef std::unordered_map<std::string, Node*> hashTable;

class Cache {

 private:
  size_t MaxSize;
  size_t totalSize;
  size_t numEntry;
  hashTable table;
  Node *head, *tail;
  
  /* detach the node from the node list */
  void detach(Node *node){
    node->prev->next = node->next; 
    node->next->prev = node->prev;
  }

  /* insert the new node after the head of the list */
  void attach(Node *node){
    node->prev = head;
    node->next = head->next;
    head->next = node;
    node->next->prev = node;
  }
  
 public: 
  Cache(size_t size = 1 << 20){
    MaxSize = size;
    totalSize = 0;
    numEntry = 0;
    head = new Node;
    tail = new Node;
    
    head->prev = NULL;
    head->next = tail;
    tail->prev = head;
    tail->next = NULL;
  }
  
  ~Cache(){
    delete head;
    delete tail;
  }

  /* get the webpage corresponding to url */
  bool get(const std::string &url, webpage &wp){
    hashTable::const_iterator got = table.find (url);
    if (got != table.end() ){ // found in cache
      detach(got->second);
      attach(got->second);
      wp = got->second->wp;
      return true;
      }
    else{ // not found
      return false;
    }
  }
  
  /* insert new hash entry */
  void put(const std::string &url, webpage &wp){
    Node *newnode = new Node;
    newnode->url = url;
    newnode->wp = wp;
    table.emplace(url, newnode);
    attach(newnode);
    totalSize += wp.len;
    numEntry++;
    while(totalSize > MaxSize){
      Node *old = tail->prev;
      totalSize -= (old->wp).len;
      numEntry--;
      table.erase(old->url);
      detach(old);
      if(old->prev != NULL){ // in case of the head node
	free((old->wp).data);
	delete old;
      }
    }
  }

  void printCache(){
    printf("%zd %zd\n", totalSize, numEntry);
    for(auto& x: table)
      std::cout << x.first << std::endl;
  }
};
