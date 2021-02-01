import requests

import json

import random

def jprint(obj):

    text = json.dumps(obj, sort_keys=True, indent=4)

    return text

def jload(obj):

    loaded_json = json.loads(formatted_json)

    return loaded_json


def get_random_word_json():

    response = requests.get("https://random-words-api.vercel.app/word")

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

for x in range (0, int(number_of_words), 1):

    random_word_json = get_random_word_json()

    formatted_json = jprint(random_word_json)

    loaded_json = jload(random_word_json)

    for key in loaded_json:

        wordsArray.append(key['word'])

for x in wordsArray:

    if (temp_counter == 0):

        text_full = text_full + x

        temp_counter = 1

    else:

        k = random.randint(0, 1)

        if (k == 0):

            text_full = text_full + ' ' + x.lower()

        else:

            text_full = text_full + '. ' + x

print (text_full)
