#include "cache.h"
#include <unordered_map>
#include <iostream>
#include <cstdio>

bool Cache::get(const std::string &url,webpage &wp)
{
	hashTable::const_iterator iter=table.find(url);
	if(iter!=table.end()){
	  wp = iter->second->wp;
		return true;
	}
	else
		return false;	
}

void Cache::put(const std::string &url,webpage &wp)
{
	if(wp.len == 0) return; /* in case the webpage has no content */
	Node *newNode=new Node;
	newNode->url=url;
	newNode->wp=wp;
	table.emplace(url,newNode);
	attach(newNode);
	totalSize+=wp.len;
	numEntry++;
	while(totalSize>MaxSize)
	{
		Node *last=tail->prev;
		detach(last);
		table.erase(last->url);
		numEntry--;
		totalSize-=(last->wp).len;
		if(last->prev!=NULL)
		{
			free((last->wp).data);
			delete last;
		}
	}	
}
