# William Keilsohn

# Define Functions

def conjugatePast(te_verb):
    raw_verb = te_verb[:-1]
    end_te = te_verb[-1]
    if end_te == "て":
        return raw_verb + "た"
    else:
        return raw_verb + "だ"