import os
import sys
import re


def rotate_header(f):
    bytes_list = f.split(b'\n')
    separator = b' '
    sep2 = b'\n'
    for i in bytes_list:
        r = i.decode('utf-8')
        regex = re.search(r'(\d+){1}(\s){1,}(\d+){1}', r)
        if regex:
            not_inverted = (regex.group().encode())
            inverted_list = list()
            l, w = not_inverted.split(b' ')
            l, w = w, l
            inverted_list.append(l)
            inverted_list.append(w)
            inverted = separator.join(inverted_list)
            for i in range(len(bytes_list)):
                if bytes_list[i] == not_inverted:
                    bytes_list[i] = inverted
    return [sep2.join(bytes_list), inverted_list, not_inverted.split(b' ')]


def dump(matrix, size, name):
    plain_ppm = os.open(f'left_{name}', os.O_RDWR | os.O_CREAT)
    os.write(plain_ppm, size)
    sep = b''
    for i in matrix:
        row = b''
        for x in i:
            row += sep.join(x)
        os.write(plain_ppm, row)

def open_file(f):
    try:
        f_read = os.open(f, os.O_RDWR | os.O_CREAT)
    except FileNotFoundError:
        sys.stdout.write('ERROR. File "{}" does not exist.\n'.format(f))
        exit()
    return f_read

def header(f):
    fd = os.read(f, 50).decode('utf-8', 'replace')
    regex = re.match(r'(P6|P3){1,}(\n){1,}(#\s*.*)*(\n)*(\d+){1}(\s){1,}(\d+){1}(\n){1,}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(\n)', fd)
    
    length_h = 0
    for i in regex.group():
        length_h += len(i.encode())
    return [regex.group().encode(), length_h]
