#!/usr/bin/env python3
# Author: Juan Medina
# Email: jmedina@collin.edu

import uuid
import subprocess
import shelve 
import sys 
import datetime
import os 

os.system('clear')
Version='2'

class color:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

if len(sys.argv) != 2:
    print('Err1: Provide the Path to the answers DB')
    exit()

if not os.path.exists(sys.argv[1]):
    print(f'Err2: file {sys.argv[1]} not found')
    exit()

def grading(test):
    c = shelve.open(test)['key']
    cc = 0
    for task in c:
        s = ''
        tc = len(c)
        if 'Task' in task:
            o = str(subprocess.check_output(c[task]['vc'], shell=True).decode('utf-8')).rstrip()
            if c[task]['p'] == 'eq':
                if c[task]['r'] == float(o):
                    s='PASS'
                    cc += 1 
                else:
                    s='FAIL'
            elif c[task]['p'] == 'ne':
                if c[task]['r'] != float(o):
                    s='PASS'
                    cc += 1
                else:
                    s='FAIL'
            elif c[task]['p'] == 'lt':
                if c[task]['r'] > float(o):
                    s='PASS'
                    cc += 1
                else:
                    s='FAIL'
            elif c[task]['p'] == 'gt':
                if c[task]['r'] < float(o):
                    s='PASS'
                    cc += 1
                else:
                    s='FAIL'
            elif c[task]['p'] == 'let':
                if c[task]['r'] >= float(o):
                    s='PASS'
                    cc += 1
                else:
                    s='FAIL'
            elif c[task]['p'] == 'get':
                if c[task]['r'] <= float(o):
                    s='PASS'
                    cc += 1
                else:
                    s='FAIL'
            if s == 'PASS':
                print(color.ENDC + '\t' + c[task]['d'] + ' ' + color.GREEN + str(s))
            else:
                print(color.ENDC + '\t' + c[task]['d'] + ' ' + color.RED + str(s))
    grade = (100.0 / float(tc)) * float(cc)
    return grade

print('Collin Test Checker - Version: ' + Version)
print(f'Running verification for: {sys.argv[1]}')
uid = input(color.GREEN + "Student ID: " + color.BLUE)
u = [uid[i:i+3] for i in range(0, len(uid), 3)]
c=str(uuid.UUID(str(subprocess.check_output(['grep', 'UUID', '/etc/fstab'])).replace('=', ' ').split(' ')[1])).split('-')
t=datetime.datetime.now()
print(color.GREEN + 'Start Time: ' + color.YELLOW + str(t) + color.ENDC)
print(color.BLUE + 'Results:' + color.ENDC)
g = grading(sys.argv[1])
print(color.GREEN + 'Final Grade: ' + color.YELLOW + str(g) + color.GREEN + ' %' + color.ENDC)
ts = str(t.strftime('%Y%m%d'))
r = c + u + [ts[i:i+2] for i in range(0, len(ts), 2)]
r.append(int(g))
print(color.GREEN + 'End Time: ' + color.YELLOW + str(datetime.datetime.now()) + color.ENDC)
print(color.RED + ''.join(map(str, r[::-1])) + color.ENDC)
