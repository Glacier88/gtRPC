#include "cache.h"
#include <unordered_map>
#include <iostream>
#include <cstdio>

bool Cache::get(const std::string &url,webpage &wp)
{
	hashTable::const_iterator iter=table.find(url);
	if(iter!=table.end())
		return true;
	else
		return false;	
}

void Cache::put(const std::string &url,webpage &wp)
{
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
