import requests

import json

import random

def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)

    return text

def jload(obj):

    loaded_json = json.loads(formatted_json)

    return loaded_json


def get_random_word_json(word):

    response = requests.get("https://random-word-api.herokuapp.com//word?number="+word)

    if (response.status_code == 200):

        return response.json()

    else :

        print ("Unsuccessful Request with error code :",response.status_code)

        return None

def validate_input(input_value):

    if (input_value.isnumeric() == True):

        if (int(input_value)>0):

            return True

        else:

            print ("Please enter a valid input.")

            return False

    else:

        print ("Please enter a valid input.")

        return False

    
while True:

    number_of_words = input ("Please enter the number of words: ")

    validation = validate_input(number_of_words)

    if (validation == True):

        break

wordsArray = []

temp_counter = 0

text_full = ''

random_word_json = get_random_word_json(number_of_words)

formatted_json = jprint(random_word_json)

loaded_json = jload(random_word_json)

for key in loaded_json:

    wordsArray.append(key)

for x in wordsArray:

    if (temp_counter == 0):

        text_full = text_full + x.capitalize()

        temp_counter = 1

    else:

        k = random.randint(0, 3)

        if (k != 0):

            text_full = text_full + ' ' + x

        else:

            text_full = text_full + '. ' + x.capitalize()

print (text_full)
