import os
import sys
import re

def open_file(f):
    try:
        f_read = os.open(f, os.O_RDWR)
    except FileNotFoundError:
        sys.stdout.write('ERROR. File "{}" does not exist.\n'.format(f))
        exit(1)
    return f_read

def header(f):
    fd = os.read(f, 50).decode('utf-8', 'replace')
    regex = re.match(r'(P6|P3){1,}(\n){1,}(#\s*.*)*(\n)*(\d+){1}(\s){1,}(\d+){1}(\n){1,}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(\n)', fd)
    
    length_h = 0
    for i in regex.group():
        length_h += len(i.encode())
    return [regex.group().encode(), length_h]
