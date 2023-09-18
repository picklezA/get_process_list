# version: 0.0.1
# author: Ben
# priority escalation :)

import psutil
import os
import time

pid = os.getpid()
cpu_process_count = psutil.cpu_count()

process = next((proc for proc in psutil.process_iter() if proc.pid == pid),None)
process.nice(psutil.REALTIME_PRIORITY_CLASS)
print(process.nice())