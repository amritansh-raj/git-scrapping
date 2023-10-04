import requests
from bs4 import BeautifulSoup
import json

url = 'https://github.com/search?q=keyword&type=searchfor'

keyword = input("Enter keyword to search for : ")

while True:
    searchfor = input(
        "Enter what you are searching for (users/repositories): ")
    if searchfor in ['users', 'repositories']:
        break
    else:
        print("Invalid input. Please enter 'users' or 'repositories'.")

new_url = url.replace("keyword", keyword).replace("searchfor", searchfor)

response = requests.get(new_url)

soup = BeautifulSoup(response.text, 'html.parser')

if response.status_code == 200:
    data = json.loads(response.text)
    users = data['payload']['results']
    # print(users)

    for user in users:
        name = user.get('name', '')
        followers = user.get('followers', 0)
        repo = user.get('repos', 0)
        print(f"Name: {name}\nFollowers: {followers}\nRepos: {repo}\n")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
