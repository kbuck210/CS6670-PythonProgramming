import sqlite3

def insert_animal(animal):
    # connect to the database & get the cursor
    sql = sqlite3.connect("zoo.sqlite")
    cursor = sql.cursor()
    try:        
        result = cursor.execute("select * from animal_count")
    except sqlite3.OperationalError:
        # table doesn't exist, so create it 
        cursor.execute("create table animal_count (name text, count integer)")

    # 'animal' is a tuple with the animal's name & it's count from the web form
    name = animal[0]
    count = animal[1]

    # Add the animal to the sql database & commit changes
    cursor.execute("insert into animal_count(name, count) values(?,?)", (name, count))
    sql.commit()
    sql.close()


def print_animals():
    sql = sqlite3.connect("zoo.sqlite")
    cursor = sql.cursor()
    result = cursor.execute("select * from animal_count")

    for row in result:
        print(row)

