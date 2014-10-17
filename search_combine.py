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

# Get the indexed data from the indexer
shelf_file = indexer.process_data(data_load.get_traversal_data())

# Perform the search on the shelved file
searcher.search(shelf_file)
