from random import choice
from string import ascii_letters, ascii_lowercase, ascii_uppercase, printable

def Generate_Key(default_range = 26):
    user_key = ""
    for _ in range(default_range):
        user_key += choice(ascii_letters)
    return user_key

def Generate_User_Set():
    user_set = []
    for _ in range(6):
        user_set.append(Generate_Key())

    for _ in range(3):
        user_set.append(Generate_Key(38))
    
    return user_set

def Generate_Random_Lowercase_Alphabet():
    alphabet = ''
    while len(alphabet) != 26:
        generated_letter = choice(ascii_lowercase)
        if generated_letter not in alphabet:
            alphabet += generated_letter
    return alphabet

def Generate_Random_Uppercase_Alphabet():
    alphabet = ''
    while len(alphabet) != 26:
        generated_letter = choice(ascii_uppercase)
        if generated_letter not in alphabet:
            alphabet += generated_letter
    return alphabet

def Generate_Map(user_set):
    user_map = {}
    letter_counter = 0
    generated_lowercase_alphabet = Generate_Random_Lowercase_Alphabet()
    generated_uppercase_alphabet = Generate_Random_Uppercase_Alphabet()
    symbols = ["\n", ">"]

    for letter in generated_lowercase_alphabet:
        map_key = ""
        for character_count in range(3):
            map_key += user_set[character_count][letter_counter]
        letter_counter += 1
        user_map.update({map_key: letter})

    letter_counter = 0

    for letter in generated_uppercase_alphabet:
        map_key = ""
        for character_count in range(3):
            map_key += user_set[character_count+3][letter_counter]
        letter_counter += 1
        user_map.update({map_key: letter})
    
    letter_counter = 0

    for symbol in symbols:
        map_key = ""
        print(letter_counter)
        map_key += user_set[len(user_set) - 1][letter_counter]
        letter_counter += 1
        user_map.update({map_key: symbol})
    
    return user_map

def Write_User_Decrypt_Map(user_map):
    with open("decrypt_map.pspr", 'w+') as MapFile:
        for field in user_map:
            MapFile.write(str(field + ":" + user_map[field] + "\n"))
    return user_map

def Write_User_Encrypt_Map(user_map):
    with open("encrypt_map.pspr", 'w+') as MapFile:
        for field in user_map:
            MapFile.write(str(user_map[field] + ":" + field + "\n"))
    return user_map

def Read_User_Map(user_map_file_handle):
    loaded_user_map = {}
    with open(user_map_file_handle, 'r') as MapFile:
        for line in MapFile:
            loaded_user_map.update({line.split(":")[0]: line.split(":")[1].strip("\n")})
        
    return loaded_user_map

def Encrypt_File(file_handle, user_encrypt_map):
    ignored_characters = ["\n", " ", ", "]
    with open(file_handle, 'r') as DataFile:
        with open(file_handle + ".pspr.encrypted", "w+") as EncryptedDataFile:
            for line in DataFile:
                for character in line:
                    if character not in ignored_characters:
                        EncryptedDataFile.write(user_encrypt_map[character])
    return file_handle, user_encrypt_map

symbols = printable.split("Z")[1]

print(len(symbols))

user_generated_set = Generate_User_Set()
user_generated_map = Generate_Map(user_generated_set)

print(user_generated_set)
print(user_generated_map)

Write_User_Encrypt_Map(user_generated_map)
Write_User_Decrypt_Map(user_generated_map)
user_encrypt_map = Read_User_Map("encrypt_map.pspr")
user_decrypt_map = Read_User_Map("decrypt_map.pspr")

Encrypt_File("Lorem.txt", user_encrypt_map)
