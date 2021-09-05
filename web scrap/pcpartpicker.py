import bs4
import requests
page = requests.get(url='https://pcpartpicker.com/products/cpu/#xcx=0').text
# print(page.content) #done
# print(page.status_code()) # not working 
soup = bs4.BeautifulSoup(page, "html.parser")
soup.prettify()
print(soup.find_all('tbody'))
print('gi')
# done till now

