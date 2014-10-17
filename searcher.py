## CS672 - Python Programming
## Kevin C Buckley
## 9/29/14
##
## ----------------
##  Quotes Module
## ----------------

from datetime import datetime
import shelve

# Search function, using dictionary of indexed data as parameter 'd'
def search(shelved_file):
    # Get input from user:
    query=input("query:") 
    x = query.split()		    # split at whitespace
    tokens = set()		    # create set to store search tokens
    for tok in x:		    # loop over all of the entered tokens,
        tokens.add(tok.lower())    # adding them to the set

    # check if only OR boolean contained in query set, then get rid of logical tokens
    orFlag = False
    if "or" in tokens and "and" not in tokens:
        orFlag = True
        tokens.discard("or")
    else:
        tokens.discard("or")
        tokens.discard("and")
        
    if len(tokens) == 0:
        print("No valid keywords entered.")
        exit(None)
    elif len(tokens) > 1 and orFlag:
        print("Performing OR search for: " + str(tokens))
    elif len(tokens) > 1:
        print("Performing AND search for: " + str(tokens))
    else:
        print("Performing search for: " + str(tokens))

    # Open the shelved file for reading
    s = shelve.open(shelved_file, "r")

    ## find the token(s) within the data
    # get start time:
    time1 = datetime.now()

    # check if keyword is in shelved file keys
    # if in keys, get tuple of files in which they appear
    # if OR search, add all files to the set of files found
    # if AND search, add count the number of tokens found,
    # if the number of tokens found matches # of tokens,
    # write each's corresponding files form the shelved tuple to the set
    files = set()                   # Create emptyset

    tokensFound = 0
    for key in s.keys():
        if key in tokens and orFlag:
            files.update(s[key])
        elif key in tokens:
            tokensFound += 1
    if not orFlag and tokensFound == len(tokens):
        for tok in tokens:
            files.update(s[tok])

    if len(files) == 0:
        print("Could not find keywords in data.")
    else:
        for file in files:
            print("Found in {},\nLast Modified: {} \nFile Size: {}"
                  .format(file[0], file[2], file[3]))
        
    # get end time
    time2 = datetime.now()
    print("Search execution time (ms):", time2.microsecond-time1.microsecond)

    return None
