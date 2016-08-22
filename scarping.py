import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.yellowpages.com/search?search_terms=coffe&geo_location_terms=Los+Angeles%2C+CA')

soup = BeautifulSoup(r.content, "html5lib")

g_data = soup.find_all('div', {"class":"info"})

for item in g_data:
	print(item.contents[0].find_all('a',{"class":"business-name"})[0].text)

	try:
		print(item.contents[1].find_all('span', {"itemprop":"streetAddress"})[0].text)
	except:
		pass

	try:
		print(item.contents[1].find_all('span', {"itemprop":"adressLocality"})[0].text.replace(",", ""))
	except:
		pass

	try:
		print(item.contents[1].find_all('span', {"itemprop":"adressRegion"})[0].text)
	except:
		pass

	try:
		print(item.contents[1].find_all('span', {"itemprop":"postalCode"})[0].text)
	except:
		pass

	try:
		print(item.contents[1].find_all('li', {"class":"primary"})[0].text)
	except:
		pass