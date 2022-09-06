from random import choice
from string import ascii_letters, ascii_lowercase

def Generate_Key():
    user_key = ""
    for _ in range(26):
        user_key += choice(ascii_letters)
    return user_key

def Generate_User_Set():
    user_set = []
    for _ in range(3):
        user_set.append(Generate_Key())
    return user_set

def Generate_Random_Alphabet():
    alphabet = ''
    while len(alphabet) != 26:
        generated_letter = choice(ascii_lowercase)
        if generated_letter not in alphabet:
            alphabet += generated_letter
    return alphabet

def Generate_Map(user_set):
    user_map = {}
    letter_counter = 0
    generated_alphabet = Generate_Random_Alphabet()

    for letter in generated_alphabet:
        map_key = ""
        for character_count in range(3):
            map_key += user_set[character_count][letter_counter]
        letter_counter += 1
        user_map.update({map_key: letter})
    
    return user_map

print(Generate_Key(), "\n")

x = Generate_User_Set()

print(x, "\n")

print(Generate_Random_Alphabet(), "\n")

print((Generate_Map(x)), "\n")