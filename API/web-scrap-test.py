import requests
from bs4 import BeautifulSoup
''
url = 'https://pcpartpicker.com/'
query = 'products/cpu/#xcx=0'

page = requests.get(url=url+query)
soup = BeautifulSoup(page.content, "html.parser")
result = soup.find(id="category_content")
print(result.prettify())
