## CS672 - PythonProgramming Hackathon
## Kevin C. Buckley
## 11/14/14

## PSUtil Information

import datetime, psutil

# Gets the PSUtil CPU data, returns a tuple [0] = total [1] = per core list
def getCpuData():
    # Gets the total CPU usage percentage, over a 1/10s interval
    tot_usg_pct = psutil.cpu_percent(interval=0.1, percpu=False)
    # Gets the CPU usage percentage for each CPU core, over a 1/10s interval
    per_core = psutil.cpu_percent(interval=0.1, percpu=True)
    return (tot_usg_pct, per_core)

# Gets a named tuple containing the requisite memory statistics
def getMemData():
    return psutil.virtual_memory()

# Gets a subset of the named tuple of the relavent network data
# [0]=sent, [1]=recieved, [2]=dropped incoming, [3]=dropped outgoing
def getNetData():
    netDat = psutil.net_io_counters(pernic=False)
    return (netDat.packets_sent, netDat.packets_recv, netDat.dropin, netDat.dropout)

# Gets the first user in the list of connected users, returning a named tuple
def getUserInfo():
    return psutil.users()[0]

# Gest the named tuple containing disk usage data for the entire PC
## Can throw OSError if the path '/' does not exist
def getDiskData():
    try:
        dsk_data = psutil.disk_usage('/')
        return dsk_data
    except OSError:
        return None

# Gets the count of currently running processes
def getProcCount():
    return len(psutil.pids())
