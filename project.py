from bs4 import BeautifulSoup
import requests

url = 'https://gitlab.com/'
login_url = 'https://gitlab.com/users/sign_in'

headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url)
response2 = requests.get(login_url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    h1_tags = soup.find_all('h1')  
    if h1_tags:
        print("H1 tags found on the page:")
        for h1_tag in h1_tags:
            print(h1_tag.text)
    else:
        print("No H1 tags found on the page.")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")


if response2.status_code == 200:
    soup = BeautifulSoup(response2.text, 'html.parser')
    label_tags = soup.find_all('label')  
    if label_tags:
        print("label tags found on the page:")
        for label_tag in label_tags:
            print(label_tag.text)
    else:
        print("No label tags found on the page.")
else:
    print(f"Failed to fetch the login page. Status code: {response.status_code}")