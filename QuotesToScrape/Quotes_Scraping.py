__author__ = "Abdessamad Touzani"
'''
Ce projet utilise la bibliothèque Python BeautifulSoup pour extraire des citations depuis le site web "Quotes to Scrape". 
Les utilisateurs peuvent spécifier des thèmes ou des auteurs pour rechercher des citations pertinentes.

YouTube Katsky Studio: https://www.youtube.com/@katskystudio
Medium Abdessamad Touzani: https://medium.com/@abdessamadtouzani
Twitter (X) @at9kat: https://twitter.com/at9kat 
Instagram @t___abdessamad__: https://www.instagram.com/t___abdessamad__/
Website: https://katskydio.wordpress.com/ or directly links: https://lnk.bio/katskystudio
Github: https://www.github.com/AbdessamadTzn
'''
from bs4 import BeautifulSoup
import requests

url = "http://quotes.toscrape.com/"

data = requests.get(url).text

soup = BeautifulSoup(data, 'lxml')

quote = soup.find('span', class_='text').text
authorName = soup.find('small', class_='author').text
span_tag = soup.find('span', class_='author')
a_tag = span_tag.find('a')
authorInfos = a_tag.get(href)
print(f'{quote}\nby: {authorName} link {authorInfos}')


