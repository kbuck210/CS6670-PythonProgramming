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
    f = open(pickle_file, "br")     # open the pickled file
    list_of_data = pickle.load(f)   # read the data
    f.close()                       # close the file

    s = shelve.open("fortunes_shelve")

    d = dict()
    for tup in list_of_data:            # loop over the list of tuples
        words = set()   
        for word in tup[1].split():     # for each word in the file contents
            words.add(word.lower())     # add to the set of unique words
        for word in words:              # looping over the unique words
            if word in d:               # if the dictionary contains the word
                d.get(word).add(tup[0]) # add the filepath from the tuple
            else:                       
                t = set({(tup[0], tup[2], tup[3])}) # otherwise create a new set with the filepath
                d[word] = t             # add the set to the dictionary

    for key in d:
        s[key] = tuple(d.get(key))      # make the mapped value a tuple to be hashable
    s.close()

    return "fortunes_shelve"
    
    
