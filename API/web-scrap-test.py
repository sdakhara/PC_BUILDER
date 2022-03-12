import requests
from bs4 import BeautifulSoup

url = 'https://pcpartpicker.com/'
query = 'products/cpu/#xcx=0'


page = requests.get(url=url+query)
soup = BeautifulSoup(page.content, "html5lib")
print(soup.prettify())
