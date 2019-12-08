import json
import difflib

data = json.load(open('data.json'))

def dict(keyUsr):
    key = keyUsr.lower()
    if key in data: 
        return data[key]
    elif key.title() in data:
        return data[key.title()]
    elif len(difflib.get_close_matches(key, data.keys())) > 0:
        close_key = difflib.get_close_matches(key, data.keys())
        ask = input(f'do you mean "{close_key[0]}"?, Enter Y if Yes, Enter N if No: ')
        if ask == 'Y':
            return data[close_key[0]]
        elif ask == 'N':
            return 'The word you entered does not exist'
        else:
            return 'We didn\'t understand your entry.'
    else:
        return 'The word you entered does not exist'

keyUsr = input('Enter the word: ')
result = dict(keyUsr)

if type(result) == list:
    num = list(range(1, len(result)+1))
    for item, number in zip(result, num):
        print(f'{number}. {item}')
else:
    print(result)