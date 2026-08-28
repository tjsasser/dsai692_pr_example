"""initials tool.""" 
 
 
def initials(text): 
    """Return the initials of each word in TEXT.""" 
    return "".join(w[0].upper() for w in text.split() if w)
