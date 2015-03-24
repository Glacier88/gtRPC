/* The LRU cache policy. Based on the cache class, we only need to
 * implement the get() and put() functions.
 */
#include "cache.h"
#include <unordered_map>
#include <iostream>
#include <cstdio>

bool Cache::get(const std::string &url, webpage &wp){
  hashTable::const_iterator got = table.find (url); // find hash entry
  if (got != table.end() ){ // found in cache
    detach(got->second); 
    attach(got->second); // move this entry to the head
    wp = got->second->wp; // copy the webpage to wp 
    return true;
  }
  else{ // not found
    return false;
  }
}

void Cache::put(const std::string &url, webpage &wp){
  if(wp.len == 0) return; /* in case the webpage has no content */
  Node *newnode = new Node;
  newnode->url = url; 
  newnode->wp = wp;  
  table.emplace(url, newnode); // inserted to the hash table
  attach(newnode); // put this new entry to the head
  totalSize += wp.len; 
  numEntry++; 
  while(totalSize > MaxSize){ // exclude some entries
    Node *old = tail->prev;
    totalSize -= (old->wp).len;
    numEntry--;
    table.erase(old->url);
    detach(old);
    if(old->prev != NULL){ // in case of the head node
      // we should free the memory of the webpage content here
      free((old->wp).data);
      delete old; // also delete this node
    }
  }
}
  
