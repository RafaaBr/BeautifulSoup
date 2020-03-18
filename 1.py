from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://www.python.org/'

html = urlopen(url)

bs = BeautifulSoup(html, 'lxml')

print(bs.title)
#teste