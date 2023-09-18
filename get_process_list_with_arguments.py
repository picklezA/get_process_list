# author: picklez
# version: 0.0.3.b
# Fork b of get_process_list.py (forked at 0.0.2)

import argparse
parser = argparse.ArgumentParser(description="Valid Arguments for Process list getting", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-ls","--get_PIDs",action="store_true",help="Just returns ProcessID list")
parser.add_argument("-pyls","--get_py_PIDs",action="store_true",help="Just returns ProcessID list for all instances of Python")
parser.add_argument("-npyls","--get_nopy_PIDs",action="store_true",help="Just returns ProcessID list for all processes that are not Python")
parser.add_argument("-p","--print",action="store_true",help="Will print the arguments asked for")
args = parser.parse_args()
config = vars(args)

def get_processID_list():
    import os
    hold = os.popen('wmic process get description, processid').read()
    hold.replace("\n\n\n\n", "\n")
    hold.replace("\n\n\n", "\n")
    hold.replace("\n\n", "\n")
    process_list_hold = hold.split("\n")
    process_list = []
    for x in range(len(process_list_hold)):
        line = process_list_hold[x]
        hold2 = line.split(".exe")
        if len(hold2) == 1:
            if hold2[0] == '':
                continue
            else:
                hold3 = str(hold2[0]).split("  ")
                hold4 = []
                for element in hold3:
                    if element != '' and element != ' ':
                        hold4.append(element)
                hold2 = hold4
        hold2[1] = str(hold2[1]).replace(" ","")
        if hold2[0] != '':
            process_list.append(hold2)
    return process_list
    
def get_python_processesID():
    hold = get_processID_list()
    py_process_list = []
    for item in hold:
        if item[0] == "python" or item[0] == "py" or item[0] == "Python":
            py_process_list.append(item[1])
    return py_process_list
    
def get_not_python_processesID():
    hold = get_processID_list()
    not_py_process_list = []
    for item in hold:
        if item[0] != "python" or item[0] != "py" or item[0] != "Python":
            not_py_process_list.append(item[1])
    if not_py_process_list[0] == "ProcessId":
        not_py_process_list.pop(0)
    return not_py_process_list

# operations based on command line arguments
if config['print'] == True:
    if config['get_PIDs'] == True:
        print("\nEntire ProcessID list:\n"+str(get_processID_list()))
    if config['get_py_PIDs'] == True:
        print("\nProcessID list for just PythonIDs:\n"+str(get_python_processesID()))
    if config['get_nopy_PIDs'] == True:
        print("\nProcessID list w/ PythonIDs:\n"+str(get_not_python_processesID()))