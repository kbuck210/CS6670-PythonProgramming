## CS672 Python Programming - Final Exam
## Kevin C. Buckley
## 12-5-14

import sqlite3
from flask import Flask, render_template
from wsgiref.simple_server import make_server

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
        # Throw an exception if the form doesn't have defined parameters
        raise Exception("Form input fields incorrectly defined")
    elif not name or not exam_num:
        # Throw a different exception if the returned values are empty
        raise Exception("User input incomplete")
    else:
        sql = sqlite3.connect('final_exam-copy.sqlite')
        # Use with to handle closing database 
        with sql:
            cur = sql.cursor()
            try:
                cur.execute("UPDATE EXAM SET StudentName=? WHERE Number=?",(str(name), str(exam_num)))
                sql.commit()
            except sqlite3.Error as e:
                print("Failed to update table with message: {}".format(str(e)))
                raise Exception("Failed to update EXAM table with values {} and {}".format(name, exam_num))               
            else:
                print("Updated EXAM table with values {} and {}".format(name, exam_num))

# SQLite database method tests        
#updateExamData('Kevin','5')

##
##  WSGI Server
##
def defineServer(environ, start_response):
    message = ""
    status = '200 OK'
    headers = [('Content-type', 'html; charset=utf-8')]
    start_response(status, headers)
    if(environ['REQUEST_METHOD'] == 'POST'):
        request_body_size = int(environ['CONTENT_LENGTH'])
        request_body = environ['wsgi.input'].read(request_body_size)
        
        # Create variables to store name & exam_num, default to None
        exam_num = None
        name = None
        # Get the form values submitted by the user
        form_vals = get_form_vals(request_body)
        for item in form_vals.keys():
            # check the value of the key
            if item.lower() == "exam_num".lower():
                exam_num = form_vals[item]
            elif item.lower() == "name".lower():
                name = form_vals[item]
            else:
                pass
        
        # call the updateExamData Method to update the values, catching exceptions
        try:
            updateExamData(name, exam_num)
        except Exception as e:
            message += "<br>Submission not processed: {}<br/>".format(str(e))
        
    message += "<h1>FINAL EXAM</h1>"
    message += "<h2>Add Record:</h2>"
    message += "<form method='POST'><br>Exam Number:<input type=text name='exam_num'>"
    message += "<br><br>Student Name:<input type=text name='name'>"
    message += "<br><br><input type='submit' name='Submit' ></form>"

    # Call the method to read the table data and output to screen
    data = getExamData()
    # Data is list of tuples in order (exam_num, name)
    message += '<br><table width="25%">'
    message += '<tr><td>Exam Number:</td><td>Student Name:</td></tr>'
    for entry in data:
        message += '<tr><td>{number}</td><td>{student}</td></tr>'.format(number=entry[0], student=entry[1])
    message += '</table><br/>'
    
    return[bytes(message,'utf-8')]

def get_form_vals(post_str):
    form_vals = {item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")}
    return form_vals

httpd = make_server('', 8000, defineServer)
print("Serving on port 8000...")
httpd.serve_forever()

##
##  Flask Application for Visualization
##
