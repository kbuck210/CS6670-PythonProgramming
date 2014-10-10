## CS672 - Python Programming
## Kevin C Buckley
## 9/29/14
##
## ----------------
##  Quotes Module
## ----------------

from datetime import datetime
import shelve
import weather

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

    # Get and display the current weather for the search terms (exact search)
    cur_weather = weather.get_weather(query)
    if cur_weather != "error":
        print("Current weather:", cur_weather)
    
    # Open the shelved file for reading
    s = shelve.open(shelved_file, "r")

    time1 = datetime.now()

    allFound = True
    results = set()

    for tok in tokens:
        if orFlag and tok in s:
            results.update(s[tok])
        elif not orFlag and tok not in s:
            allFound = False

    if not orFlag and allFound:
        count = 0
        for tok in tokens:
            if count > 0:
                results &= s[tok]   # intersection with s[tok] value and self
            else:
                results |= s[tok]   # union with s[tok] value and self

            count += 1
        
    if not results:
        print("Could not find search query in data.")
    else:
        for result in results:
            print("Found at:", result)
        
    # get end time
    time2 = datetime.now()
    print("Search execution time (ms):", time2.microsecond-time1.microsecond)

    return None
