

#Fetches quotes from list25 site and arranges for use in random quote generator
__author__ = "vignesh ramesh"
import requests,re
from bs4 import BeautifulSoup

outputFile = open('output.txt', 'w')
quotes = []
for i in range(1,6):
	res = requests.get("http://list25.com/25-inspirational-movie-quotes-that-could-change-your-life/"+ str(i)+ "/")
	print(res.raise_for_status())
	print("Request" + str(i))
	content =res.content #get html content
	soup = BeautifulSoup(content,'html.parser')
	list_items = soup.find("section",{"class":"list-items"}).findAll("div",{"class":"item-content"})
	
	for i in list_items:
		quote = {"text":"","name":""}
		quote["text"] = i.p.string
		quote["name"] = i.em.string
		quotes.append(quote)
	
outputFile.write(str(quotes))
outputFile.close()

	
