import requests
from bs4 import BeautifulSoup
import re

def getBreakingNews(url):
	headers = {
		"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:44.0) Gecko/20100101 Firefox/44.0"
	}
	values = {}
	r =  requests.get(url)
	soup = BeautifulSoup(r.content, "html5lib")
	datas = soup.find_all('div', {"class":"td-trending-now-display-area"})
	for data in datas:
		breakingNews = data.find_all('a')
		for breakingNew in breakingNews:
			try:
				values[breakingNew.text] = breakingNew.get('href')
			except:
				pass

	return values

def getContent(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.content, "html5lib")
	datas = soup.find_all('div', {"class":"td-post-content"})
	for data in datas:
		contents = [tmp.text for tmp in data.find_all('p')]

	return contents
		

def main():
	url = 'http://waktuku.com/'
	data = getBreakingNews(url)
	keys = list(data.keys())
	
	while True:
		counter = 1
		for key in keys:
			print(counter,key)
			counter += 1

		pilih = int(input('Pilih no artikel : '))

		if pilih == 0:
			break

		page = data[keys[pilih-1]]
		results = getContent(page)
		print("\n",results,"\n")
	

if __name__ == '__main__':
	main()