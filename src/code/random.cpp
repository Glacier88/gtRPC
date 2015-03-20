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
	totalSize+=wp.len;
	while(totalSize>MaxSize)
	{
		srand(time(0));
		int r=rand();
		int rand=r%numEntry--;
		Node *node=head;
		int i=0;
		for(i=0;i<=rand;i++)
			node=node->next;
		detach(node);
		table.erase(node->url);
		totalSize-=(node->wp).len;
		if(node->prev!=NULL)
		{
			free((node->wp).data);
			delete node;
		}
	}
	Node *newNode=new Node;
	newNode->url=url;
	newNode->wp=wp;
	table.emplace(url,newNode);
	attach(newNode);
	numEntry++;
}
