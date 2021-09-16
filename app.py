import json 
                
def find_meaning(word):
    with open('data.json') as f:
        data = json.load(f)
        output =''
    try:
        if word.lower() in data:
            output = data[word.lower()]  
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

word = input('Enter a word: ')

find_meaning(word)



        
    # for k,v in data.items():
    #     if word.lower() in k:
    #         print(f"{k} means: {v}")
            