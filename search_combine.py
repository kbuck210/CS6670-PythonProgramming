## CS672 - Python Programming
## Kevin C. Buckley
## 9/29/14
##
## -------------------------
##  Search Combine Module
## -------------------------

import searcher
import data_load
import indexer
import web_crawler

# Traverse the file structure to initialize the pickle
#pickle_file = data_load.get_traversal_data()

# Update pickle with web crawler data
#web_crawler.visit_url("http://www.newhaven.edu/", "www.newhaven.edu", pickle_file)


# Get the indexed data from the indexer for file traverser
#shelf_file = indexer.process_data("raw_data.pickle")

# Perform the search on the shelved file
searcher.search("fortunes_shelve")
