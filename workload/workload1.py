from random import choice

pages=["http://www.google.com","http://www.cnn.com","http://www.yahoo.com","http://www.github.com","http://www.gatech.edu","http://www.youtube.com","http://www.tutorialspoint.com","http://www.stanford.edu","http://www.ebay.com","http://www.fox.com","http://www.facebook.com","http://www.harward.edu","http://www.careercup.com","http://www.netflix.com","http://www.bbc.com","http://www.walmart.com","http://www.instagram.com","http://www.bestbuy.com","http://www.newegg.com","http://www.baidu.com","http://www.emory.edu","http://www.mit.edu","http://www.princeton.edu","http://www.brown.edu","http://www.nutrition.gov","http://www.altmedicine.com","http://www.citysearch.com","http://www.monster.com","http://www.votesmart.org","http://www.sciam.com","http://www.espn.com","http://www.findlaw.com","http://www.nature.com","http://www.usatoday.com","http://www.allposters.com","http://www.time.com","http://www.mapquest.com","http://www.abebooks.com","http://www.allmusic.com","http://www.medlineplus.gov","http://www.dmoz.org","http://www.loc.gov","http://windowsmedia.msn.com","http://www.ucomics.com","http://www.infoplease.com","http://www.alexa.com","http://www.un.org","http://www.artforum.com","http://www.webmd.com","http://www.vlib.org","http://moneycentral.msn.com","http://www.classmates.com","http://groups.yahoo.com",
"http://www.nybooks.com","http://www.jokes.com","http://www.priceline.com","http://www.rottentomatoes.com","http://www.ipl.org","http://www.acefitness.com",
"http://www.quicken.com","http://lpi.oregonstate.edu","http://www.pcmag.com","http://www.iht.com","http://www.ebooks.com","http://www.gatech.edu",
"http://www.ibm.com","http://www.paypal.com","http://www.youtube.com","http://www.pogo.com","http://www.stackoverflow.com","http://www.bizrate.com","http://www.billboard.com",
"http://www.give.org","http://mathworld.wolfram.com","http://www.webring.org",
"http://www.careerbuilder.com","http://www.411.com","http://www.cisco.com","http://www.epinions.com","http://www.nolopress.com","http://www.classical.net","http://www.nytimes.com","http://www.earthcam.com"]

# random work load			
with open("random_workload",'w') as file1:
	for i in range(300):
		file1.write(choice(pages)+"\n")
#repeated work load
with open("repeated_workload",'w') as file2:
	for i in range(300):
			file2.write(choice(pages[0:40])+"\n");

