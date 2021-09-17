import json 
import difflib
from difflib import get_close_matches

data = json.load(open('data.json'))

                
def find_meaning(word):
    word = word.lower()
    with open('data.json') as f:
        data = json.load(f)
        output =''
    try:
        if word in data:
            output = data[word.lower()]  
        else:
            match = get_close_matches(word,data)
            if len(match) != 0:
                print(match)
            else:    
                print(f"{word} not found. Please double check")   
                output = ''   
    except Exception as e:
        print(f"Error is {e}")
    else:
        if output != '':
            print(f"{word} has {len(output)} meaning")
            print(f"{word} means: ")
            for o in output:
                print(f"=> {o}\n")    

#word = input('Enter a word: ')



def init():
    word = input('Enter a word: ')
    
    if word.lower() in data.keys():
        find_meaning(word)
    else:
        match = get_close_matches(word,data)
        if len(match) >0:
            print('did you mean:')
            for m in match:
                print(m)
            inp = input('\nEnter the correct word again: ')
            if inp.lower() in data:
                find_meaning(inp)
            else:
                print(f'"{inp}" is not found in dictionary.')    
        else:
            print(f"{word} not found")            



#init()
    
if __name__ == '__main__':
    init()    
    