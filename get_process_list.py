# author: picklez
# version: 0.0.2
# purpose: to parse the windows api process list into a form for python!

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

# comment out anything under this if you would like to just access the classes    
print(get_processID_list())
print()
print(get_python_processesID())
print()
print(get_not_python_processesID())