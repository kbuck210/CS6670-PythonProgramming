## CS672 - Python Programming Hackathon
## Kevin C. Buckley
## 11/16/14

## Flask Web Services

from flask import Flask, jsonify, render_template
import googlechart
import sqlite3
from logging import FileHandler

app = Flask(__name__)

# base hello world
@app.route('/')
def hello_world():
    return 'Hello World!'

# CPU usage data chart
@app.route('/cpu')
def cpu_chart():
    # Create SQL connection to the database
    try:
        sql = sqlite3.connect("usage.sqlite")
        cursor = sql.cursor()
        # select all data from the table
        result = cursor.execute('select * from cpu_table')
        # fetch all the data, returning a tuple of tuples
        datalist = result.fetchall()
        sql.commit()
        sql.close()
        # the number of cores = # of columns -1
        nCores = len(datalist[0]) - 1
        
        formatted = googlechart.formatCpuData(datalist, nCores)
        return googlechart.getHTML(formatted, 'CPU Commit Charge:')
    
    except sqlite3.OperationalError:
        print("Failed to retrieve database information")
        return "Error reading database"

# Total memory percentage used chart
@app.route('/mem')
def mem_chart():
    # Create SQL connection to the database
    try:
        sql = sqlite3.connect("usage.sqlite")
        cursor = sql.cursor()
        result = cursor.execute('select percent from mem_table')
        datalist = result.fetchall()
        sql.commit()
        sql.close()

        formatted = googlechart.formatMemPercent(datalist)
        return googlechart.getHTML(formatted, 'Total Memory Used (%%)')
    except sqlite3.OperationalError:
        print("Failed to retrieve database information")
        return "Error reading database"

# Memory detailed information chart
@app.route('/mem/details')
def mem_detail_chart():
    try:
        sql = sqlite3.connect("usage.sqlite")
        cursor = sql.cursor()
        result = cursor.execute('select total, available, used, free from mem_table')
        datalist = result.fetchall()
        sql.commit()
        sql.close()

        formatted = googlechart.formatMemDetails(datalist)
        return googlechart.getHTML(formatted, 'Memory Usage Details (in MB)')
    except sqlite3.OperationalError:
        print("Failed to retrieve database information")
        return "Error reading database"

# Total Disk Used % chart
@app.route('/disk')
def dsk_chart():
    try:
        sql = sqlite3.connect("usage.sqlite")
        cursor = sql.cursor()
        result = cursor.execute('select percent from dsk_table')
        datalist = result.fetchall()
        sql.commit()
        sql.close()

        formatted = googlechart.formatDskPercent(datalist)
        return googlechart.getHTML(formatted, 'Total Disk Percent Used (%%)')
    except sqlite3.OperationalError:
        print("Failed to retrieve database information")
        return "Error reading database"

# Disk Detailed Information Chart
@app.route('/disk/details')
def dsk_detail_chart():
    try:
        sql = sqlite3.connect("usage.sqlite")
        cursor = sql.cursor()
        result = cursor.execute('select total, free, used from dsk_table')
        datalist = result.fetchall()
        sql.commit()
        sql.close()

        formatted = googlechart.formatDskDetails(datalist)
        return googlechart.getHTML(formatted, 'Disk Usage Details (in MB)')
    except sqlite3.OperationalError:
        print("Failed to retrieve database information")
        return "Error reading database"

# Network Packets Sent/Recieved chart
@app.route('/net_traffic')
def net_traffic_chart():
    try:
        sql = sqlite3.connect("usage.sqlite")
        cursor = sql.cursor()
        result = cursor.execute('select sent, received from net_table')
        datalist = result.fetchall()
        sql.commit()
        sql.close()

        formatted = googlechart.formatNetTraffic(datalist)
        return googlechart.getHTML(formatted, 'Packet Traffic')
    except sqlite3.OperationalError:
        print("Failed to retrieve database information")
        return "Error reading database"

# Network Dropped Packets chart
@app.route('/net_drops')
def net_drops_chart():
    try:
        sql = sqlite3.connect("usage.sqlite")
        cursor = sql.cursor()
        result = cursor.execute('select dropin, dropout from net_table')
        datalist = result.fetchall()
        sql.commit()
        sql.close()

        formatted = googlechart.formatNetDrops(datalist)
        return googlechart.getHTML(formatted, 'Dropped Packets')
    except sqlite3.OperationalError:
        print("Failed to retrieve database information")
        return "Error reading database"

# Process count chart
@app.route('/processes')
def process_chart():
    try:
        sql = sqlite3.connect("usage.sqlite")
        cursor = sql.cursor()
        result = cursor.execute('select count from prc_table')
        datalist = result.fetchall()
        sql.commit()
        sql.close()

        formatted = googlechart.formatProcessData(datalist)
        return googlechart.getHTML(formatted, 'Total Process Count')
    except sqlite3.OperationalError:
        print("Failed to retrieve database information")
        return "Error reading database"
    
app.run()
