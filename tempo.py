import requests
from bs4 import BeautifulSoup
import re

def getTerpopuler(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html5lib")
    result = {}
    data = soup.find_all('div', {"id":"tops-1"})
    terpopulers = data[0].find_all('h3')
    for terpopuler in terpopulers:
        result[terpopuler.text] = terpopuler.find_all('a')[0].get('href')
    return result

def getContent(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html5lib")
    data = soup.find_all('p')
    result = []
    if(len(data)>1):
        for dt in data[:-1]:
            result.append(dt.text)
        return result


def main():
    url = "https://www.tempo.co/"
    data = getTerpopuler(url)
    keys = list(data.keys())
    
    while True:       
        counter = 1
        for key in keys:
            print(counter,key)
            counter += 1
        
        pilih = int(input('Pilih no berita : '))
        
        if pilih == 0:
            break
        
        page = data[keys[pilih-1]]
        results = getContent(page)
        for result in results:
            print(re.sub('\s\s+','\n\n', result))
        #print(type(getContent(page)), len(getContent(page)))
        print()

if __name__ == '__main__':
    main()
