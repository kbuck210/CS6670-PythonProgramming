## CS672 - Python Programming - Homework 6
## Kevin Buckley
## 11/4/14

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.request import urlopen
import psutil, datetime

# Create new HTTP Request Handler Subclass of BaseHTTPRequestHandler
class NewHTTPRequestHandler(BaseHTTPRequestHandler):
    # Override do_GET method to set request response
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        # Do psutil get for relevent server data
        boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
        cpu_util = psutil.cpu_percent(interval=1, percpu=True)
        mem = psutil.virtual_memory()
        dsk_usg = psutil.disk_usage('/')
        html = """<!DOCTYPE html>
                  <html><body>
                  <table style="width:50%">
                    <tr bgcolor="cyan">
                      <td>BOOT TIME</td>
                      <td colspan="2">{bt}</td>
                      </span>
                    </tr>
                    <tr>
                      <td rowspan="{cpus}">CPU UTILIZATION</td>
                      """.format(bt=boot_time, cpus=(len(cpu_util)+1))
        i = 1
        for cpu in cpu_util:
            if cpu < 50:
                cbg = "#00FF00"
            elif cpu < 75:
                cbg = "yellow"
            else:
                cbg = "red"
            html += "<tr><td>CPU {}</td><td bgcolor=\"{}\">{}</td></tr>".format(i, cbg, cpu)
            i += 1
        html += """<tr bgcolor="cyan">
                     <td>AVAILABLE MEMORY</td>
                     <td colspan="2">{am}</td>
                   </tr>""".format(am=mem.available)
        html += """<tr>
                     <td>USED MEMORY</td>
                     <td colspan="2">{um}</td>
                   </tr>""".format(um=mem.used)
        if mem.percent < 50:
            mbg = "green"
        elif mem.percent < 90:
            mbg = "yellow"
        else:
            mbg = "red"
        html += """<tr bgcolor="cyan">
                     <td>USED PERCENTAGE</td>
                     <td colspan="2" bgcolor="{bgcol}">{up}</td>
                   </tr>""".format(bgcol=mbg, up=mem.percent)
        html += """<tr>
                     <td>TOTAL DISK SPACE</td>
                     <td colspan="2">{tds}</td>
                   </tr>""".format(tds=dsk_usg.total)
        html += """<tr bgcolor="cyan">
                     <td>USED DISK SPACE</td>
                     <td colspan="2">{uds}</td>
                   </tr>""".format(uds=dsk_usg.used)
        html += """<tr>
                     <td>FREE DISK SPACE</td>
                     <td colspan="2">{fds}</td>
                   </tr>""".format(fds=dsk_usg.free)
        if dsk_usg.percent < 50:
            dbg = "green"
        elif dsk_usg.percent < 90:
            dbg = "yellow"
        else:
            dbg = "red"
        html += """<tr bgcolor="cyan">
                     <td>USED PERCENTAGE</td>
                     <td colspan="2" bgcolor="{bgcol}">{udp}</td>
                   </tr>
                 </table>
                 </body>
                 </html>""".format(bgcol=dbg, udp=dsk_usg.percent)
        
        self.wfile.write(bytes(html,'utf-8'))
        return

server = HTTPServer(("", 8000), NewHTTPRequestHandler)
server.serve_forever()
