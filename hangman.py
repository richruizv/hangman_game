import os
import platform
import random as rd


def clear_os():
    if platform.system() == 'windows':
        os.system('cls')  
    else:
        os.system('clear')  
    
def read_intro():
    with open("./files/intro.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(line)

def get_random_word():
    words = []
    with open("./files/words.txt", "r", encoding="utf-8") as f:
        for word in f:
            words.append(word)
    words = list(map(lambda word : word.replace('\n','') , words))

    random_word = words[rd.randint(0,len(words)-1)]

    return random_word

def print_hidden_word(word,guessed_letter):
    mask_word = list(word) #we make a mask to print the hidden letters comparing the opposite

    for _guessed_letter in guessed_letter:
        mask_word[_guessed_letter] = '_'

    hidden_word = []
    for index,letter in enumerate(word):
        hidden_word.append('  ')
        if mask_word[index] == '_':
            hidden_word.append(letter)
        else:
            hidden_word.append('_')

    hidden_word = "                            "+"".join(hidden_word)+"\n"

    print(hidden_word)

# I create an iterative function to find more than one character in our random word
def iterative_find(word,letter,guessed_letter,needle): 
    f = word.find(letter)
    if f != -1:
        guessed_letter.append(f+needle)
        cut_word= word[f+1:len(word)]
        needle = needle + f + 1
        iterative_find(cut_word,letter,guessed_letter,needle)
        return True
    else:
        return False
    
def print_hangman(attemps_left):
    with open("./files/hangman1.txt", "r", encoding="utf-8") as f:
        for line in f:
            print("                 " + line)
    print("Attemps left: "+str(attemps_left))    
    
def hangman_attemp(word,guessed_letter,attemps_left):
    clear_os()
    read_intro()
    print_hangman(attemps_left)
    print_hidden_word(word,guessed_letter)

    letter = input('Guess the word letter by letter: ')
    
    needle = word
    attemp = iterative_find(needle,letter,guessed_letter,0)

    if attemp == False:
        attemps_left -= 1

    return attemps_left
    

def run():
    rand_word = get_random_word()
    guessed_letter = []
    attemps_left = len(rand_word)*2

    while 1:
        attemps_left = hangman_attemp(rand_word,guessed_letter,attemps_left)
     
if __name__ == '__main__':
    run()