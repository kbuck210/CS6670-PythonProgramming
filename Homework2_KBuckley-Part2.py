## Homework 2 - CS672 Python Programming
## Kevin Buckley
## 9/19/14
##
from datetime import datetime
import Homework2_DataModule

# Get the data from the data module
data_list = Homework2_DataModule.getData()

# Part 2
# Improve performance by using a dictionary, mapping each word to a set of quotes
d = dict()
for i, quote in enumerate(data_list):
    words = set()
    for word in quote.split():      # tokenize each line on whitespace
        words.add(word.lower())     # add each token to the words set
    for word in words:              # loop over each unique word
        if word in d:               # if the dictionary has the word,
            d.get(word).add(i)      # add the line number to the word's set
        else:                       # if the dictionary doesn't have the word
            s = set({i})            # create a new set (init with line number)
            d[word] = s             # set value of new key to set

query=input("query:") 
x = query.split()				# split at whitespace
tokens = set()					# create set to store search tokens
for tok in x:					# loop over all of the entered tokens, adding them to the set
    tokens.add(tok.lower())

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

## find the token(s) within the data
# get start time:
time1 = datetime.now()

# check if keyword is in dictionary
# if in dictionary, get lines appearing
# if OR search, print all lines
# if AND search, add lines to set
# for each next token, get lines, take only similar lines in set
if orFlag:
    lines = set()   # Empty set for OR flag, add all found to set
else:
    lines = set(range(len(data_list))) # Full set for AND flag
    
for tok in tokens:
    if tok in d and orFlag:
        lines = lines | d.get(tok)  # for OR condition, add all lines
    elif tok in d:
        lines = lines & d.get(tok)  # for AND condition, add only similar lines
if len(lines) == 0:
    print("Could not find keywords in data.")
else:
    for line in lines:
        print("Found at", line, data_list[line])
    
# get end time
time2 = datetime.now()
print("Search execution time (ms):", time2.microsecond-time1.microsecond)
