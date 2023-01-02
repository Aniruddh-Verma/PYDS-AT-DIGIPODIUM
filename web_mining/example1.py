import requests
url = 'http://www.google.com'

response = requests.get(url)
if response.status_code == 200:    # statuscode 200 is success 404 is not found 
      print('success!')
      print(response.content)
else:
      print('an errror has occured')
