#!/usr/bin/python3

import os
import argparse
import concurrent.futures
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
    fd = os.read(f, 40).decode('utf-8', 'replace')
    regex = re.match(r'(P6|P3){1,}(\n){1,}(#\s*.*)*(\n)*(600|5[0-9][0-9]|4[0-9][0-9]|3[0-9][0-9]|2[0-9][0-9]|1[0-9][0-9]|[1-9]?[0-9]){1}(\s){1,}(500|4[0-9][0-9]|3[0-9][0-9]|2[0-9][0-9]|1[0-9][0-9]|[1-9]?[0-9]){1}(\n){1,}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])(\n)', fd)
    length_h = 0
    for i in regex.group():
        length_h += len(i.encode())
    return [regex.group().encode(), length_h]


def dump(fd, chunk):
    text = os.read(fd, chunk)
    new_ppm = os.open('new_dog.ppm', os.O_RDWR | os.O_CREAT)
    os.write(new_ppm, fd)


def rotate_header(f):
    # print(f.split(b'\n'))
    bytes_list = f.split(b'\n')
    separator = b' '
    sep2 = b'\n'
    # print(bytes_list)
    for i in bytes_list:
        r = i.decode('utf-8')
        regex = re.search(r'(600|5[0-9][0-9]|4[0-9][0-9]|3[0-9][0-9]|2[0-9][0-9]|1[0-9][0-9]|[1-9]?[0-9]){1}(\s){1,}(500|4[0-9][0-9]|3[0-9][0-9]|2[0-9][0-9]|1[0-9][0-9]|[1-9]?[0-9]){1}', r)
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

    return sep2.join(bytes_list)



def filtro(color, f, chunk, head, length):
    os.lseek(f, int(length), 0)
    text = os.read(f, chunk)
    files = list()

    for i in range(3):
        new_ppm = os.open(f'{color}.ppm', os.O_RDWR | os.O_CREAT)
        os.write(new_ppm, head)
        files.append(new_ppm)

    bytes_list= list()
    for i in text:
        bytes_list.append(bytes([i]))
    
    zero = list()
    for i in range(len(bytes_list)):
        zero.append(b'\x00')

    # print(zero)
    if color == 'r':
        ct = 0
        for i in range(int(len(zero)/3)):
            zero[ct] = bytes_list[ct]
            ct += 3
        for i in zero:
            os.write(files[0], i)

    elif color == 'g':
        ct = 1
        for i in range(int(len(zero)/3)):
            zero[ct] = bytes_list[ct]
            ct += 3
        for i in zero:
            os.write(files[1], i)

    elif color == 'b':
        ct = 2
        for i in range(int(len(zero)/3)):
            zero[ct] = bytes_list[ct]
            ct += 3
        for i in zero:
            os.write(files[2], i)

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='TP1 - procesa ppm')
    parser.add_argument('-s', '--size', action="store", metavar='SIZE', type=int,
                        required=True, help='Bloque de lectura')
    parser.add_argument('-f', '--file', action="store", metavar='FILE', type=str,
                        required=True, help='archivo a procesar')
    
    args = parser.parse_args()
    fd = args.file
    chunk = args.size
    rgb = ['r', 'g', 'b']
    file = open_file(fd)
    head, length = header(file) 
    for i in rgb:
        filtro(i, file, 1965906, rotate_header(head), length)
    # print(rotate_header(head))
