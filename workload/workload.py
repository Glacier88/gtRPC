from random import choice

pages=["http://www.google.com","http://www.cnn.com","http://www.yahoo.com","http://www.github.com","http://www.gatech.edu","http://www.youtube.com","http://www.tutorialspoint.com","http://www.baidu.com","http://www.ebay.com","http://www.sina.com.cn"]

# random work load			
with open("random_workload",'w') as file1:
	for i in range(60):
		file1.write(choice(pages)+"\n")
# repeated work load
with open("repeated_workload",'w') as file2:
	for i in range(3):
		for j in pages:
			file2.write(j+"\n")
	for i in range(3):
		for j in reversed(pages):
			file2.write(j+"\n")
