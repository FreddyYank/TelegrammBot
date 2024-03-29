import pprint
import requests

token = "5992942897:AAFgfBhPoldn36g8_lGSasRSNE6ReXs8P94"
main_url = f"https://api.telegram.org/bot{token}"

url = f'{main_url}/getUpdates'

result = requests.get(url)
pprint.pprint(result.json())

message = result.json()['result']
for message in message:
    chat_id = message['message']['chat']['id']
    url = f'{main_url}/sendMessage'
    params = {
        'chat_id':chat_id,
        'text': 'Привет друг!'
    }
    result = requests.post(url, params=params)
