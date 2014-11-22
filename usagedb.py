## CS672 - Python Programming Hackathon
## Kevin C. Buckley
## 11/15/14

## Database

# Need to store the following:

##
## CPU Data:
## 1. List[] Total CPU usage percentage
## 2. List[] List of percentages per CPU core

##
## Memory Data
## 1. List[] Total Mem usage percentage
## 2. List[] Total Mem usgage magnitude
## 3. List[] Available mem usage magnitude
## 4. List[] Used mem usage magnitude
## 5. List[] Free mem usage magnitude

##
## Net Data
## 1. List[] Sent packets
## 2. List[] Recieved packets
## 3. List[] Drops-incoming
## 4. List[] Drops-outgoing

##
## UserInfo - Dont store averages...database for each user?
## 1. Name
## 2. Terminal
## 3. Host
## 4. Started - running time since epoch

##
## Disk Data
## 1. List[] Total disk usage magnitude
## 2. List[] Free disk usage magnitude
## 3. List[] Used disk usage magnitude
## 4. List[] Disk percentage used

import sqlite3

class UsageDB():
    # Dictionary of descriptive names to SQL table names
    tableNames = {'CPU':'cpu_table', 'MEM':'mem_table', 'DSK':'dsk_table',
                  'NET':'net_table', 'USR':'usr_table'}

    def __init__(self, dbname):
        self.dbname = dbname
        # Connect to the usage database
        self.sql = sqlite3.connect(dbname)
        self.cursor = self.sql.cursor()

        ## Only create tables if they do not already exist in the database
        try:
            self.cursor.execute("select * from cpu_table")
        except sqlite3.OperationalError:
            self.cursor.execute("create table cpu_table (total real)")
        try:
            self.cursor.execute("select * from mem_table")
        except sqlite3.OperationalError:
            self.cursor.execute("create table mem_table (percent real, total real, available real, used real, free real)")
        try:
            self.cursor.execute("select * from dsk_table")
        except sqlite3.OperationalError:
            self.cursor.execute("create table dsk_table (total real, free real, used real, percent real)")
        try:
            self.cursor.execute("select * from net_table")
        except sqlite3.OperationalError:
            self.cursor.execute("create table net_table (sent integer, received integer, dropin integer, dropout integer)")
        try:
            self.cursor.execute("select * from usr_table")
        except sqlite3.OperationalError:
            self.cursor.execute("create table usr_table (name text, terminal text, host text, started real)")
        try:
            self.cursor.execute("select * from prc_table")
        except sqlite3.OperationalError:
            self.cursor.execute("create table prc_table (count integer)")
            
    # Add the columns to the CPU table based on the number of cores in the machine
    def updateCpuCols(self, nCores):
        try:
            for i in range(0, nCores):
                colName = ("core" + str(i+1),)
                self.cursor.execute('alter table "cpu_table" add column '+str(colName[0])+' real')
        except sqlite3.OperationalError:
            print("could not add columns to the cpu_table for each core...")

    # Get the rows for the specified table
    def getRows(self, table):
        if table in UsageDB.tableNames.keys():
            t = (table,)    # Do this for security
            try:
                result = cursor.execute("select * from ?", t)
                return result
            except sqlite3.OperationalError:
                return None

    # Insert rows to CPU Table
    def insertCpuData(self, data):
        # Data is list of tuples from last 10 iterations of psutildata calls
        for tup in data:
            t = [tup[0]]        # Flatten the list to write to the database
            for x in tup[1]:
                t.append(x)
            
            # insert total_usg_percent & per_core data to cpu_table
            try:
                self.cursor.execute('insert into "cpu_table" values(?,'+ ','.join("?" * len(tup[1])) + ')', tuple(t))
            except sqlite3.OperationalError:
                print("Failed to add cpu data to table")
                return
        # if no errors encountered, commit changes to the database
        self.sql.commit()
        

    # Insert rows to Mem Table
    def insertMemData(self, data):
        mb = 1000000
        # data is list of named tuples returned from psutil
        for entry in data:            
            t = [entry.percent, entry.total/mb, entry.available/mb,
                 entry.used/mb, entry.free/mb]
            try:
                self.cursor.execute('insert into "mem_table" values(?,?,?,?,?)',tuple(t))
            except sqlite3.OperationalError:
                print("Failed to add mem data to table")
                return
        # If no errors, commit to database
        self.sql.commit()

    # Insert rows to Disk Table
    def insertDskData(self, data):
        mb = 1000000
        # data is list of named tuples returned from psutil
        for entry in data:
            t = [entry.total/mb, entry.free/mb, entry.used/mb, entry.percent]
            try:
                self.cursor.execute('insert into "dsk_table" values(?,?,?,?)', tuple(t))
            except sqlite3.OperationalError:
                print("Failed to add disk data to table")
                return
        # If no errors, commit to database
        self.sql.commit()

    # Insert rows to Net Table
    def insertNetData(self, data):
        for entry in data:
            t = [entry[0], entry[1], entry[2], entry[3]]
            try:
                self.cursor.execute('insert into "net_table" values(?,?,?,?)',tuple(t))
            except sqlite3.OperationalError:
                print("Failed to add net data to table")
                return
        # If no errors encountered, commit to database
        self.sql.commit()

    # Insert rows to User Table
    def insertUsrData(self, data):
        # write only unique user data to DB
        pass

    # Insert rows to Process Count table
    def insertPrcData(self, data):
        for entry in data:
            t = [entry]
            try:
                self.cursor.execute('insert into "prc_table" values(?)',tuple(t))
            except sqlite3.OperationalError:
                print("Failed to add process data to table")
                return
        # if no errors, commit to database
        self.sql.commit()
                
    
            
