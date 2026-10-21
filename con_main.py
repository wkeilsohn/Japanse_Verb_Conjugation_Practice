# William Keilsohn

# Import Packages
import os
import numpy as np
import pandas as pd

## Import Custom Scripts
from procedures import *

# Delcare Global Variables
ru_verb_end_char = "る"
irreg_ls = ["する", "くる"]
exception_ls = ["ある", "いる"]

ru_u_common_exceptions = ["かえる", "しる", "しゃべる", "はいる", "帰る", "知る", "喋る", "入る"] # There are probably more but I am just one person.

# Define Functions
def exceptionVerbChecker(user_verb):
    global irreg_ls
    global exception_ls
    is_exception = False
    if user_verb in irreg_ls:
        is_exception = True
    elif user_verb in exception_ls:
        is_exception = True
    return is_exception

def ruVerbChecker(user_verb):
    global chars_df
    global ru_u_common_exceptions
    true_ru_chars = []
    if user_verb in ru_u_common_exceptions:
        return False
    second_end_char = user_verb[-2]
    true_chars_1 = chars_df["I"].to_list()
    true_chars_2 = chars_df["E"].to_list()
    true_ru_chars = true_chars_1 + true_chars_2
    if second_end_char in true_ru_chars:
        return True
    else:
        return False

def verbChecker(user_verb, end_char):
    ru_verb_status = False
    if end_char == ru_verb_end_char:
        ru_verb_status = ruVerbChecker(user_verb)
    return ru_verb_status
    
def conVerb(user_verb):
    ru_verb_status = False
    verb_base = user_verb[:-1]
    end_char = user_verb[-1]
    exception_status = exceptionVerbChecker(user_verb=user_verb)
    verb_forms = {}
    if exception_status:
        verb_forms = IRVerbProcedure(user_verb=user_verb)
    else:
        ru_verb_status = verbChecker(user_verb=user_verb, end_char=end_char)
        if ru_verb_status:            
            verb_forms = RUVerbProcedure(user_verb=user_verb, verb_base=verb_base)
        else:
            verb_forms = UVerbProcedure(user_verb=user_verb, verb_base=verb_base)
    return verb_forms
