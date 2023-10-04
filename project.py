import requests
from bs4 import BeautifulSoup
import json

url = 'https://github.com/search?q=keyword&type=searchfor&p=page_no'

keyword = input("Enter keyword to search for : ")

while True:
    choice = input("Enter '1' for users or '2' for repositories: ")
    if choice == '1':
        searchfor = 'users'
        break
    elif choice == '2':
        searchfor = 'repositories'
        break
    else:
        print("Invalid input. Please enter '1' or '2'.")

new_url = url.replace("keyword", keyword).replace("searchfor", searchfor)

response = requests.get(new_url)

soup = BeautifulSoup(response.text, 'html.parser')

if response.status_code == 200:
    data = json.loads(response.text)
    
    if searchfor == 'users':
        page = 0
        pages = data['payload']['page_count']
    
        while page <= pages:
            base_url = new_url.replace("page_no", str(page)) 
            response = requests.get(base_url)
            data = response.json()
            results = data['payload']['results']
            
            for user in results:
                name = user.get('name', '')
                followers = user.get('followers', 0)
                repo = user.get('repos', 0)
                bio = user.get('profile_bio', '')
                print(f"Name: {name}\nFollowers: {followers}\nRepos: {repo}\nBio: {bio}\n\n")
            
            page += 1
    
    elif searchfor == 'repositories':
        page = 0
        pages = data['payload']['page_count']

        while page <= pages:
            base_url = new_url.replace("page_no", str(page)) 
            response = requests.get(base_url)
            data = response.json()
            results = data['payload']['results']
            
            for repo in results:
                name = repo['repo']['repository']['name']
                owner = repo['repo']['repository']['owner_login']
                stars = repo.get('followers', 0)
                forks = repo.get('forks', 0)
                description = repo.get('hl_trunc_description', '')
                print(f"Name: {name}\nOwner: {owner}\nStars: {stars}\nForks: {forks}\nDescription: {description}\n\n")
            
            page += 1

else:
    print("Failed to retrieve the page. Status code:", response.status_code)
