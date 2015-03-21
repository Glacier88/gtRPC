#ifndef CACHE_H
#define CACHE_H

#include <unordered_map>
#include <iostream>
#include <cstdio>
#include <vector>

//const size_t MaxSize = 1 << 20; // 1M

//page Structure
typedef struct {
  char *data;  // pointer to the webpage content
  size_t size; // allocated size
  size_t len;  // actual length of array
} webpage;

/* node structure used in the hash table */
typedef struct _Node {
  std::string url; 		/* key */
  webpage wp;      		/* data */
  _Node *prev, *next;
} Node;

typedef std::unordered_map<std::string, Node*> hashTable;


class Cache {

 private:
  size_t MaxSize; 		/* maximal cache size */
  size_t totalSize;		/* current total cache size */
  size_t numEntry;		/* number of cache entries */
  hashTable table;		/* the hash table */
  Node *head, *tail;		/* head and tail of the linked list */
  std::vector<std::string> keys;
  
  /* detach the node that is just before the tail */
  void detach(Node *node){
    node->prev->next = node->next; 
    node->next->prev = node->prev;
  }

  /* insert the new node after the head */
  void attach(Node *node){
    node->prev = head; 
    node->next = head->next; 
    head->next = node; 
    node->next->prev = node;
  }
  
 public:
  /* construction function */
  Cache(size_t size = 1 << 20){
    MaxSize = size; 		/* max cache size is default 2^20 */
    totalSize = 0;		
    numEntry = 0;
    head = new Node;
    tail = new Node;
    
    head->prev = NULL;		/* initialize head and tail */
    head->next = tail;
    tail->prev = head;
    tail->next = NULL;
  }
  
  /* destructor */
  ~Cache(){
    delete head;		/* delete head */
    delete tail;		/* delete tail */
  }

  /** @brief obtain the webpage corresponding to url
   *
   * @param[in] url  the url address
   * @param[out] wp  the webpage structure
   * @return         hash table hit or miss
   */
  bool get(const std::string &url, webpage &wp);
  
  /** @brief insert new hash entry
   *
   * When there is a hash table miss, we need to insert the
   * pair <ulr, node*> into the hash table. At the same time,
   * if the cache size exceeds the maximal size, we need to
   * throw out some hash entries.
   *
   * @param[in] url the url address
   * @param[in] wp  the webpage structure
   */
  void put(const std::string &url, webpage &wp);
  
  
  /* print the hash table just for debug purpose */
  void printCache(){
    printf("%zd %zd\n", totalSize, numEntry);
    for(auto& x: table)
      std::cout << x.first << std::endl;
  }
};

#endif	/* CACHE_H */
