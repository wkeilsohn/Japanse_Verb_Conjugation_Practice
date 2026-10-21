# William Keilsohn

# Define Variables
te_irregulars = {"いく":"いって", "くる":"きて", "する":"して"}
te_u_regulars = {"く":"いて", "ぐ":"いで", "す":"して", "る":"って", "つ":"って", "う":"って", "む":"んで", "ぬ":"んで", "ぶ":"んで"} # There may be a better way to organize this later.
te_r_regulars = {"る":"て"}
polite_add_on = "い"

# Define Functions

def conjugateRUTEForm(verb_base): # This only makes the regular te_form. Not one of the polite derivatives. 
    te_verb = ""
    te_verb = te_verb + verb_base + "て"
    return te_verb

def conjugateUTEForm(user_verb, verb_type):
    global te_irregulars
    global te_u_regulars
    te_verb = ""
    if verb_type == "IR":
        te_verb = te_irregulars.get(user_verb)
    else:
        verb_base = user_verb[:-1]
        change_char = user_verb[-1]
        end_char = te_u_regulars.get(change_char)
        te_verb = te_verb + verb_base + end_char
    return te_verb
        
def add_polite_glue(te_form_verb):
    global polite_add_on
    return te_form_verb + polite_add_on