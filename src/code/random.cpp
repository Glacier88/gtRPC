#include "cache.h"
#include <unordered_map>
#include <iostream>
#include <cstdio> 
#include <vector>
#include <iterator>


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
	totalSize+=wp.len;
	while(totalSize>MaxSize)
	{
		srand(time(0));
		int r=rand();
		int rand=r%numEntry--;
		totalSize-=(table.at(keys.at(rand))->wp).len;
		table.erase(keys.at(rand));
		keys.erase(keys.begin()+rand);
		
	}
	Node *newNode=new Node;
	newNode->url=url;
	newNode->wp=wp;
	numEntry++;
	keys.push_back(url);
	table.emplace(url,newNode);
}
