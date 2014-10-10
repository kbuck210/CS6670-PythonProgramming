## CS672 - Python Programming
## Homework 3
## Kevin C. Buckley
## 9/29/14
##
## ----------------------
##  Data Indexer Module
## ----------------------
import pickle
import shelve
import re

# data_list - the list of all of the quotes, is now the parameter to the
# indexer function, which in turn returns the indexed dictionary
def indexData(data_list):
    # Create a dictionary to store the data,
    # indexed by each word, mapped to quotes
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

    return d    # return the dictionary of indexed data

# Process Data function, same as above, only using pickled file,
# and mapping filepaths instead of list indecies
# ** Modified in step 6 to return the shelved file instead of the dictionary
def process_data(pickle_file):
    f = open(pickle_file, "rb")     # open the pickled file
    list_of_data = pickle.load(f)   # read the data
    f.close()                       # close the file

    s = shelve.open("fortunes_shelve")

    for tup in list_of_data:            # loop over the list of tuples
        for word in tup[1].split():     # loop over each word in the content
            word = word.lower()         # put the word in lower case for case insensitivity
            values = set()              # create an empty set
            if word in s:               # check if the keyword is in the shelve
                values = s[word]        # if so, set the set to the existing resulting set
            values.add(tup[0])          # add the filepath/webURL to the set of values in the shelve

            s[word] = values            # write the values to the shelve mapped by the keyword

    return "fortunes_shelve"            # return the name of the shelf file
    
    
