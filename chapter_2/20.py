import json

try:
    with open('jawiki-country.json', 'r') as f:
        for item in list(f):
            json_item = json.loads(item)
            if json_item['title'] == 'イギリス':
                print(json_item['text'])
except json.JSONDecodeError as e:
    print('Error: ', e)
