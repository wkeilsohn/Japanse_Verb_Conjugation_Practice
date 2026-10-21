# William Keilsohn

# Import Packages
import pandas as pd
import os

cpath = os.getcwd() 
file_folder = os.path.join(cpath, 'files')
alphabet_file = os.path.join(file_folder, 'alphabet.xlsx')
chars_df = pd.read_excel(alphabet_file)
chars_df = chars_df.iloc[:, 1:]

present_ending = "ない"
past_ending = "かった"

# Declare Functions

def conjugateRUNegative(verb_base):
    global present_ending
    return verb_base + present_ending

def conjugatePastNegative(negative_v):
    global past_ending
    return negative_v[:-1] + past_ending

def conjugateUNegative(user_verb):
    global chars_df
    global present_ending
    new_verb = user_verb[:-1]
    if user_verb[-1] == "う":
        new_end_char = "わ"
    else:
        new_end_char = chars_df.loc[chars_df['U'] == user_verb[-1], 'A'].iloc[0]
    return new_verb + new_end_char + present_ending
