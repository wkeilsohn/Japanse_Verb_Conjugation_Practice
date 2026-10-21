# William Keilsohn

# Import Packages
import os
import pandas as pd

## Import Custom Scripts
from Form_Scripts.te_form import *
from Form_Scripts.polite_form import *
from Form_Scripts.negative_form import *
from Form_Scripts.stem_form import *
from Form_Scripts.past_form import *

# Define Functions

def RUVerbProcedure(user_verb, verb_base):
    dict_form = user_verb
    stem_form = verb_base
    negative_form = conjugateRUNegative(verb_base=verb_base)
    past_negative_form = conjugatePastNegative(negative_v=negative_form)
    te_form = conjugateRUTEForm(verb_base=verb_base)
    past_form = conjugatePast(te_verb=te_form)
    polite_forms = conjugatePolite(verb_root=stem_form)
    conjugation_dict = {"Dictionary Form": dict_form, "Stem Form": stem_form, "Polite Form(s)": polite_forms, \
                        "Negative Form": negative_form, "Past Negative Form": past_negative_form, "Past Form": \
                            past_form, "Te Form": te_form}
    return conjugation_dict


def UVerbProcedure(user_verb, verb_base):
    dict_form = user_verb
    stem_form = conjugateUStem(user_verb=user_verb)
    negative_form = conjugateUNegative(user_verb=user_verb)
    past_negative_form = conjugatePastNegative(negative_v=negative_form)
    te_form = conjugateUTEForm(user_verb=user_verb, verb_type="U")
    past_form = conjugatePast(te_verb=te_form)
    polite_forms = conjugatePolite(verb_root=stem_form)
    conjugation_dict = {"Dictionary Form": dict_form, "Stem Form": stem_form, "Polite Form(s)": polite_forms, \
                        "Negative Form": negative_form, "Past Negative Form": past_negative_form, "Past Form": \
                            past_form, "Te Form": te_form}
    return conjugation_dict

def IRVerbProcedure(user_verb): # This only covers the two most common irregular verbs. As noted, I am just one person. 
    dict_form = user_verb
    if user_verb == "する":
        negative_form = "しない"
        te_form = conjugateUTEForm(user_verb=user_verb, verb_type="IR")
        stem_form = conjugateIIGStem(user_verb=user_verb)
    elif user_verb == "くる":
        negative_form = "こない"
        te_form = conjugateUTEForm(user_verb=user_verb, verb_type="IR")
        stem_form = conjugateIIGStem(user_verb=user_verb)
    else:
        stem_form = conjugateERStem(user_verb=user_verb)
        negative_form = "ない"
        te_form = conjugateUTEForm(user_verb=user_verb, verb_type="ER") # Exceptions
    polite_forms = conjugatePolite(verb_root=stem_form)
    past_form = conjugatePast(te_verb=te_form)
    past_negative_form = conjugatePastNegative(negative_v=negative_form)
    conjugation_dict = {"Dictionary Form": dict_form, "Stem Form": stem_form, "Polite Form(s)": polite_forms, \
                        "Negative Form": negative_form, "Past Negative Form": past_negative_form, "Past Form": \
                            past_form, "Te Form": te_form}
    return conjugation_dict