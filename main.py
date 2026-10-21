# William Keilsohn
# June 10 2026

# Import Packages 
import os
import numpy as np
import pandas as pd
from random import randint

## Import Custom Packages
from text_converter import *
from con_main import *

# Define Global Variables
cwd = os.getcwd()
file_folder = os.path.join(cwd, 'files')
verb_file = os.path.join(file_folder, 'verbs.xlsx')

## Get Verb List
df = pd.read_excel(verb_file)
verb_ls = list(df['Furigana'])

total_possible_score = len(verb_ls)

## Polite Forms
p_forms = ['Present', 'Present Negative', 'Past', 'Past Negative']
n_forms = ['Present', 'Past']

# Define Function
def convertUserInput():
    user_input = input("Enter Your Answer: ")
    use_ans = textCon(user_input)
    return use_ans

def verbPicker():
    global verb_ls
    v = randint(0, len(verb_ls) - 1)
    v = verb_ls[v]
    return v
    
def pickCon(ran_verb):
    global p_forms
    global n_forms
    con_options = conVerb(ran_verb)
    c = randint(0, len(con_options) - 1)
    c_form = list(con_options.values())[c]
    m = list(con_options)[c]
    if isinstance(c_form, list):
        c = randint(0, len(c_form) - 1)
        if len(c_form) > 3:
            m = m + ' - ' + p_forms[c]
        else:
            m = m + ' - ' + n_forms[c]
        c_form = c_form[c]
    return (m, c_form)
    
def checkAnswer(machine_answer, user_answer):
    if user_answer == machine_answer:
        print('That is correct!')
        print(user_answer)
        return True
    else:
        print('That is incorrect.')
        print('Your answer was {}'.format(user_answer))
        print('The correct answer is {}'.format(machine_answer))
        return False

# Run Application
if __name__ == '__main__':
    print('Welcome to the Challange!')
    game_status = True
    check_val = True
    final_score = 0
    questions_answered = 0
    while game_status:
        vrb_in = 'The verb is: {} '
        con_in = 'Please conjugate in: {} '
        ran_verb = verbPicker()
        con_verb = pickCon(ran_verb)
        vrb_in = vrb_in.format(ran_verb)
        print(vrb_in)
        con_in = con_in.format(con_verb[0])
        print(con_in)
        user_answer = convertUserInput()
        check_val = checkAnswer(con_verb[1], user_answer)
        questions_answered = questions_answered + 1
        if check_val:
            final_score = final_score + 1
            verb_ls.remove(ran_verb)
        if final_score == total_possible_score:
            print('You Won The Game!')
            game_status = False
        print('Your current score is: {} out of {} questions asked.'.format(final_score, questions_answered))
    print('Your final score is: {} our of a possible {}'.format(final_score, total_possible_score))
    