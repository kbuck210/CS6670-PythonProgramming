## CS672 Python Programming - Final Exam
## Kevin C. Buckley
## 12-5-14

import sqlite3
from flask import Flask, render_template

##
##  Sqlite connection Methods (Retrieve & Update EXAM table)
##
def getExamData():
    try:
        sql = sqlite3.connect('final_exam-copy.sqlite')
        cur = sql.cursor()
        result = cur.execute('select Number,StudentName from EXAM WHERE StudentName is not null')
        data = result.fetchall()
        sql.commit()
        sql.close()
        return data
    except sqlite3.Error:
        print("Failed to retreive information from database")
        return None

def updateExamData(name, exam_num):
    # Check that both the student name and the exam number have been provided
    if name == None or exam_num == None:
        # Throw an exception if they have not been defined
        raise Exception("Input Parameters not Fully Defined")
    else:
        sql = sqlite3.connect('final_exam-copy.sqlite')
        # Use with to handle closing database 
        with sql:
            cur = sql.cursor()
            try:
                cur.execute("UPDATE EXAM SET StudentName=? WHERE Number=?",(str(name), str(exam_num)))
                sql.commit()
            except sqlite3.Error as e:
                print("Failed to update EXAM table with values {} and {}".format(name, exam_num))               
                print(e)
            else:
                print("Updated EXAM table with values {} and {}".format(name, exam_num))
        

updateExamData('Kevin','5')
