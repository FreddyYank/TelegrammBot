import requests as req
from bs4 import BeautifulSoup

response = req.get("https://api.github.com/users/Freddy").json()

print(response)
for i in response:
    print(i+":",response[f'{i}'])

# response = req.get('https://www.youtube.com/watch?v=rm7-P8zPDGk')
# soup = BeautifulSoup(response.text, "html.parser")
# print(response.status_code)
# comment = soup.find_all('span', class_='yt-core-attributed-string--link-inherit-color')
# print(comment)