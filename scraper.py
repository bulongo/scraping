from bs4 import BeautifulSoup as bs
import requests
import lxml

site = input('Name of the site: ')
holder = requests.get(site)
soup = bs(holder.text,'lxml')

item = input('What type of file would you like to find?: ("a-for links and so on" ')

lst = soup.findAll(item)
for i in lst:
    print(i.text)
