# William Keilsohn

# Import Packages
import os
import pandas as pd

# Declare Variables

cpath = os.getcwd() 
file_folder = os.path.join(cpath, 'files')
alphabet_file = os.path.join(file_folder, 'alphabet.xlsx')
chars_df = pd.read_excel(alphabet_file)
chars_df = chars_df.iloc[:, 1:]

# Define Functions

def conjugateRUStem(verb_base): # This is a useless endeavore for RU verbs.
    return verb_base 

def conjugateUStem(user_verb):
    global chars_df
    new_verb = user_verb[:-1]
    swap_char = user_verb[-1]
    new_end_char = chars_df.loc[chars_df['U'] == swap_char, 'I'].iloc[0]
    return new_verb + new_end_char

def conjugateIRStem(user_verb):
    global chars_df
    swap_char = user_verb[0]
    new_char = chars_df.loc[chars_df['U'] == swap_char, 'I'].iloc[0]
    return new_char

def conjugateERStem(user_verb):
    global chars_df
    new_verb = user_verb[:-1]
    swap_char = user_verb[-1]
    new_char = chars_df.loc[chars_df['U'] == swap_char, 'I'].iloc[0]
    return new_verb + new_char
    
def conjugateIIGStem(user_verb):
    global chars_df
    swap_char = user_verb[0]
    new_char = chars_df.loc[chars_df['U'] == swap_char, 'I'].iloc[0]
    return new_char