#!/usr/bin/python3

import os
import argparse
import concurrent.futures
import re
from filtro import filtro 
from manager import open_file, header


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



    rotated_content_header, inverted_sz, o_size = rotate_header(head)

    

    print(filtro(file, length, rotated_content_header, inverted_sz, o_size, chunk))
    
    # filtro('k', file, 1965906, rotate_header(head), length)

