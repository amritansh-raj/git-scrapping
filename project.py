import requests
from bs4 import BeautifulSoup

url = 'https://github.com/search?q=keyword&type=searchfor'

keyword = input("Enter keyword to search for : ")

while True:
    searchfor = input("Enter what you are searching for (users/repositories): ")
    if searchfor in ['users', 'repositories']:
        break
    else:
        print("Invalid input. Please enter 'users' or 'repositories'.")

new_url = url.replace("keyword", keyword).replace("searchfor", searchfor)

response = requests.get(new_url)

soup = BeautifulSoup(response.text, 'html.parser')

divs = soup.find_all('div', class_='Box-sc-g0xbh4-0 bBwPjs search-title')

for div in divs:
    spans = div.find_all('span')
    for span in spans:
        print(span.text)