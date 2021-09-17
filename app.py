"""English dictionary applicaion."""
import json
import difflib
from difflib import get_close_matches

data = json.load(open('data.json'))

def output(meaning):
    num_meaning = len(meaning)
    print(f"It has {num_meaning} meanings.")
    for m in meaning:
        print(f"=> {m}")


def translate(word):
    word = word.lower()
    if word in data:
        meaning = data[word]
        output(meaning)
    elif len(get_close_matches(word,data.keys())) > 0:
        match = input(f"Did you mean {get_close_matches(word,data.keys())[0]} instead? (y/n) ")
        if match.lower() == "y" or match.lower() == "yes":
            meaning = data[get_close_matches(word,data.keys())[0]]
            #print(meaning)
            output(meaning)
    else:
        print(f'"{word}" is not found. Please double check.')
    
def init():
    word = input('Enter a word: ')
    translate(word)
    

if __name__ == '__main__':
    init()             