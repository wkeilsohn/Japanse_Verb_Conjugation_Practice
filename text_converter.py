# William Keilsohn
# June 9th 2026

# Import Packages
import os
import numpy as np
import pandas as pd
import re

# Define Variables
cwd = os.getcwd()
file_folder = os.path.join(cwd, 'files')
alphabet_file = os.path.join(file_folder, 'alphabet.xlsx')

## Get Alphabet DF
df = pd.read_excel(alphabet_file)
df = df.set_index(df.columns[0])

### Get Letter Lists
vowels = list(df.columns)
consts = ['H','M','Y','R','W','G','D','B','P','N','Z']
trips = ['S','J','C']
iregs = ['K','T']
#### Japanese Special Letters
tiny_dic = {1:'っ', 2:'ゃ', 3:'ょ'}
NN = 'ん'

## Create Objects
char_ls = []
hira_ls = []

# Define Functions
def inputParser(user_input): # This should really be broken up into smaller functions.
    global vowels
    global char_ls
    global consts
    global trips
    global iregs
    user_input = user_input.upper().replace('F', 'H')
    first_char = user_input[0]
    letter_tup = ()
    tiny_tsu_tup = None
    tiny_ya_yo = None
    if first_char in vowels:
        letter_tup = ('X', first_char)
        user_input = user_input[1:]
    elif first_char in consts:
        char_pair = user_input[:2]
        letter_tup = (char_pair[0], char_pair[1])
        user_input = user_input[2:]
    elif first_char in trips:
        if user_input[1] == 'H':
            letter_tup = (user_input[0].replace('C', 'T'), 'I')
            user_input = user_input[3:]
        elif user_input[1] == 'Y':
            letter_tup = (user_input[0].replace('J', 'Z'), 'I')
            if user_input[2] == 'A':
                tiny_ya_yo = ('2', 2)
            else:
                tiny_ya_yo = ('3', 3)
            user_input = user_input[3:]
        else:
            char_pair = user_input[:2]
            letter_tup = (char_pair[0].replace('J', 'Z'), char_pair[1])
            user_input = user_input[2:]
    elif first_char in iregs:
        if user_input[0] == user_input[1]:
            tiny_tsu_tup = ('1', 1)
            letter_tup = (user_input[1], user_input[2])
            user_input = user_input[3:]
        elif user_input[1] == 'S' and user_input[0] == 'T':
            letter_tup = (user_input[0], user_input[2])
            user_input = user_input[3:]
        elif user_input[1] == 'Z' and user_input[0] == 'T':
            letter_tup = ('D', user_input[2])
            user_input = user_input[3:]
        else:
            char_pair = user_input[:2]
            letter_tup = (char_pair[0], char_pair[1])
            user_input = user_input[2:]
    else:
        user_input = user_input[1:] # Assumes single typo
    if tiny_tsu_tup:
        char_ls.append(tiny_tsu_tup)
    char_ls.append(letter_tup)
    if tiny_ya_yo:
        char_ls.append(tiny_ya_yo)
    if len(user_input) > 0:
        inputParser(user_input)
        
def charCoverter():
    global char_ls
    global hira_ls
    global df
    global tiny_dic
    global NN
    for i in char_ls:
        j = i[0]
        k = i[1]
        if j.isnumeric():
            hira_ls.append(tiny_dic[k])
        elif j == k:
            hira_ls.append(NN)
        else:
            hira_ls.append(df.at[j, k])

def textCon(user_input): # Function for calling in a larger Script.
    global char_ls
    global hira_ls
    char_ls = []
    hira_ls = []
    inputParser(user_input=user_input)
    # print(char_ls)
    charCoverter()
    # print(hira_ls)
    return "".join(hira_ls)

# # Run Application
# if __name__ == '__main__': # Standard Notation to Call Script on it's own. 
    # user_input = input('Enter Text Here: ')
    # hiragana_text = textCon(user_input)
    # print(hiragana_text)