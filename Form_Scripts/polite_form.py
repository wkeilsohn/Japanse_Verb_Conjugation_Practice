# William Keilsohn

# Declare Variables
polite_form = ["ます", "ません", "ました", "ませんでした"]

# Define Functions

def conjugatePolite(verb_root): # Just adds the polite stem to the end. 
    global polite_form
    polite_ls = []
    for i in polite_form:
        j = verb_root + i
        polite_ls.append(j)
    return polite_ls