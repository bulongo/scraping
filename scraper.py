from bs4 import BeautifulSoup as bs
from requests.exceptions import MissingSchema
import requests
import lxml

site = input('Name of the site: ')
try:
    holder = requests.get(site)
except MissingSchema:
    holder = requests.get('http://' + site)
except MissingSchema:
    holder = requests.get('https://' + site)
soup = bs(holder.text,'lxml')

item = input('What type of file would you like to find?: ("a-for links and so on" ')

lst = soup.findAll(item)
for i in lst:
    print(i.text)
