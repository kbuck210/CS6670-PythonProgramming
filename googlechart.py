## CS672 - Python Programming Hackathon
## Kevin C. Buckley
## 11/19/14

## Google Charts API HTML code

## "data" element passed in as follows:
##   x-div   dataset1  dataset2
##  ['Year', 'Sales', 'Expenses'],
##  ['2004',  1000,      400],
##  ['2005',  1170,      460],
##  ['2006',  660,       1120],
##  ['2007',  1030,      540]
import datetime

# Method to add seconds to the data lists (X-value for charts
def appendSeconds(data, result):
    rowid = 1  # the row id of data read from the database (in seconds)
    for row in data:
        l = [rowid]
        l.extend(row)
        result.append(l)
        rowid += 1

    return result

# Method to format the CPU data to Google Chart API Style
def formatCpuData(data, nCores):
    result = [['Seconds', 'Total CPU%']]
    # Add the dataset names for each core
    for i in range(0, nCores):
        result[0].append('Core ' + str(i+1))
    # Create the datalist
    result = appendSeconds(data, result)

    if len(result) > 1:
        return result
    else:
        return None
# Method to format the MEM Percentage data to the Google Charts
def formatMemPercent(data):
    result = [['Seconds', 'Memory Used %']]
    result = appendSeconds(data, result)
    if len(result) > 1:
        return result
    else:
        return None

# Method to format the Mem Table data to Google Charts
def formatMemDetails(data):
    result = [['Seconds', 'Total', 'Available', 'Used', 'Free']]
    result = appendSeconds(data, result)
    if len(result) > 1:
        return result
    else:
        return None

# Method to format the Dsk data to Total Percent used
def formatDskPercent(data):
    result = [['Seconds', 'Disk Space Used %']]
    result = appendSeconds(data, result)
    if len(result) > 1:
        return result
    else:
        return None

# Method to format the Dsk data details for Google Charts
def formatDskDetails(data):
    result = [['Seconds', 'Total', 'Free', 'Used']]
    result = appendSeconds(data, result)
    if len(result) > 1:
        return result
    else:
        return None

# Method to format the net sent/recieved data for Google Charts
def formatNetTraffic(data):
    result = [['Seconds', 'Sent', 'Received']]
    result = appendSeconds(data, result)
    if len(result) > 1:
        return result
    else:
        return None

# Method to format the net Dropped data for Google Charts
def formatNetDrops(data):
    result = [['Seconds', 'Dropped - Incoming', 'Dropped - Outgoing']]
    result = appendSeconds(data, result)
    if len(result) > 1:
        return result
    else:
        return None

# Method to format the process count data for Google Charts
def formatProcessData(data):
    result = [['Seconds', 'Processes']]
    result = appendSeconds(data, result)
    if len(result) > 1:
        return result
    else:
        return None

# Method to format the HTML in the Google Charts API format
def getHTML(data, title):
    cur_time = datetime.datetime.now().strftime("%I:%M%p on %B %d, %y")
    
    chartHTML = """
    <html>
      <head>
        <script type="text/javascript" src="https://www.google.com/jsapi"></script>
        <script type="text/javascript">
          google.load("visualization", "1", {packages:["corechart"]});
          google.setOnLoadCallback(drawChart);
          function drawChart() {
            var data = google.visualization.arrayToDataTable(
              """ + str(data) + """
            );

            var options = {
              title: '""" + title + """'
            };

            var chart = new google.visualization.LineChart(document.getElementById('chart_div'));

            chart.draw(data, options);
          }
        </script>
      </head>
      <body>
        <h4>Data as of: """ + str(cur_time) + """</h4>
        <div id="chart_div" style="width: 900px; height: 500px;"></div>
      </body>
    </html>
    """
    return chartHTML
