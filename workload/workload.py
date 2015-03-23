from random import choice

pages=["http://www.google.com","http://www.cnn.com","http://www.yahoo.com","http://www.github.com","http://www.gatech.edu","http://www.youtube.com","http://www.tutorialspoint.com","http://www.ebay.com","http://www.fox.com","http://www.facebook.com","http://www.paypal.com","http://www.bbc.com","http://www.walmart.com","http://www.bestbuy.com","http://www.newegg.com","http://www.emory.edu","http://www.mit.edu","http://www.espn.com","http://www.nature.com","http://www.time.com"]



# random work load			
with open("random_workload",'w') as file1:
	for i in range(110):
		file1.write(choice(pages)+"\n")

#repeated work load
repeated = []
for i in range(0, len(pages)-5, 2):
	for j in range(5):
		repeated.append(pages[i+j])
	if i % 2 == 0 :
	       	repeated.append(pages[0])
	if i % 3 == 0 :
	       	repeated.append(pages[1])
	if i % 4 == 0 :
		repeated.append(pages[2])
		
repeated += repeated[::-1]
with open("repeated_workload",'w') as file2:	
	for i in range(len(repeated)):
		file2.write(repeated[i]+"\n")

