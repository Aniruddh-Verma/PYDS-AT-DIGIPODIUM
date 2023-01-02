# parsing the data library used for parsing data is beautifulsoup
# a small link crawler 
from bs4 import BeautifulSoup
import requests

url = 'http://www.google.com/search?q=css'
response = requests.get(url)
if not response.status_code == 200:
      print('an error has occured.')
      exit()
else:
      print('success!')
      soup = BeautifulSoup(response.text,'html5lib')
      print(soup.prettify())

      # get all heading h1
      heading_3 = soup.find_all('h3')
      print("heading_3:")
      for i in heading_3:
            print(i.text)
      
      # get all links
      links = soup.find_all('a')
      print('links:')
      for i in links:
            print(f'{i.text} 🔗 {i.get("href")}')