#!/usr/bin/python3
import os
import argparse
import sys
from multiprocessing import Process, Pipe
import re


def histo(color_list):
    profundidad = list()
    total = list()
    count = 0
    for i in range(256):
        profundidad.append(count)
        count += 1
    qt = 0
    for i in profundidad:
        for j in color_list:
            if i == j:
                qt += 1
        total.append(qt)
        qt = 0
    return total


def rgb_list(arr_rgb, k):
    arr = list()
    for i in range(len(arr_rgb)):
        arr.append(arr_rgb[k % len(arr_rgb)])
        k = k + 3
    return arr
    

def histogram(chunk, hijo, color):
    # fd = os.open('{}_{}.{}'.format(color, f, 'txt'), os.O_RDWR, os.O_CREAT)
    rgb = list()
    while True:
        if color == 'r':
            texto = hijo.recv()
            if texto == b"":
                # print(histo(r))
                # print(len(histo(r)))
                break
            for byte in texto:
                rgb.append(byte)
            r = (rgb_list(rgb, 0))

        if color == 'g':
            texto = hijo.recv()
            if texto == b"":
                
                break
            for byte in texto:
                rgb.append(byte)
            g = (rgb_list(rgb, 1))
            
        if color == 'b':
            texto = hijo.recv()
            if texto == b"":
                break
            for byte in texto:
                rgb.append(byte)
            b = (rgb_list(rgb, 2))
    hijo.close()       
    return

# lo que hace es determinar el largo del header através de regex
def header(f):
    while True:
        fd = os.read(f, 30)
        text = fd.decode('utf-8', 'replace')
        head_lenght = 0
        regex = re.compile(r"(P6|P3)")
        regex_comment = re.compile(r"\n(#\s*.*){1}")
        regex3 = re.compile(r'\n(600|5[0-9][0-9]|4[0-9][0-9]|3[0-9][0-9]|2[0-9][0-9]|1[0-9][0-9]|[1-9]?[0-9]){1}\s(500|4[0-9][0-9]|3[0-9][0-9]|2[0-9][0-9]|1[0-9][0-9]|[1-9]?[0-9]){1}')
        regex4 = re.compile(r'\n(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\n')
        h1 = regex.search(text)
        h2 = regex_comment.search(text)
        h3 = regex3.search(text)
        h4 = regex4.search(text)
        list_regex = [h1, h2, h3, h4]
        for i in list_regex:
            if i:
                head_lenght += len(i.group().encode())
        print(head_lenght)
        return int(head_lenght)
        
                
    ## lo que hace es leer de a chunks el archivo ppm.
    ## le que lee lo escribe en un txt pero escribe desde el byte posterior al heade
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='TP1 - procesa ppm')
    parser.add_argument('-s', '--size',action="store", metavar='SIZE', type=int,
                        required=True, help='Bloque de lectura')
    parser.add_argument('-f', '--file',action="store", metavar='FILE', type=str,
                        required=True, help='archivo a procesar')

    args = parser.parse_args()
    fd = args.file
    chunk = args.size

    parent_conn = list()
    hijos = list()
    colors = ['r', 'g', 'b']
    index = 0
    for i in range(3):
        p, h = Pipe()
        child = Process(target=histogram, args=(chunk, h, colors[index]))
        index += 1
        hijos.append(child)
        parent_conn.append(p)

    for i in hijos:
        i.start()
    
    fd_read = os.open(fd, os.O_RDWR)
    head_lenght = header(fd_read)
    os.lseek(fd_read, head_lenght, 0)
    while True:
        f_read = os.read(fd_read, chunk)
        parent_conn[0].send(f_read)
        parent_conn[1].send(f_read)
        parent_conn[2].send(f_read)

        if f_read == b"" and len(f_read) < chunk:
            break
    
    for i in parent_conn:
        i.close()
    
    os.close(fd_read)
    print('Exito')
