#!/usr/bin/python3
import os
import argparse
import concurrent.futures
import re
from filtro import plain_matrix, bytes_matrix
from manager import open_file, header, dump, rotate_header


def rotate(chunk, j):
    global constant
    global index
    global empty
    chunk_list = chunk
    rows = len(empty)
    for i in chunk_list:
        empty[index[0]][index[1]][j] = i[j]
        index[0] -= 1

        if index[0] == -1 and index[1] == rows+1:
            empty[index[0]][index[1]][j] = i[j]
       
        if index[0] == -1:
            index[1] += 1
            index[0] = rows - 1
    

def rotate_g(chunk, j):

    global constant
    global index2
    global empty
    
    chunk_list = chunk
    rows = len(empty)

    for i in chunk_list:
        empty[index2[0]][index2[1]][j] = i[j]
        index2[0] -= 1
        if index2[0] == -1 and index2[1] == rows+1:
            empty[index2[0]][index2[1]][j] = i[j]
        if index2[0] == -1:
            index2[1] += 1
            index2[0] = rows - 1


def rotate_b(chunk, j):
    global constant
    global index3
    global empty
    
    chunk_list = chunk
    rows = len(empty)

    for i in chunk_list:
        empty[index3[0]][index3[1]][j] = i[j]
        index3[0] -= 1

        if index3[0] == -1 and index3[1] == rows+1:
            empty[index3[0]][index3[1]][j] = i[j]
         
        if index3[0] == -1:
            index3[1] += 1
            index3[0] = rows - 1
    

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='TP1 - procesa ppm')
    parser.add_argument('-s', '--size', action="store", metavar='SIZE', type=int,
                        required=True, help='Bloque de lectura')
    parser.add_argument('-f', '--file', action="store", metavar='FILE', type=str,
                        required=True, help='archivo a procesar')
    
    args = parser.parse_args()
    fd = args.file
    print(fd)
    args.size = args.size - (args.size%3) 
    chunk = args.size
    
    # rgb = ['r', 'g', 'b']
    file = open_file(fd)
    head, length = header(file) 
    len_head = length
    rotated_content_header, inverted_sz, o_size = rotate_header(head)
    os.lseek(file, len_head, 0)
    empty = plain_matrix(o_size, rotated_content_header)
    empty_original = plain_matrix(o_size, rotated_content_header)

    f = len(empty) - 1
    c = 0
    b = 0 
    
    index = [f, c ,b]
    index2 = [f, c ,b]
    index3 = [f, c ,b]

    while True:

        text = os.read(file, chunk)
        new = bytes_matrix(text)
        
        rotate(new, 0)
        rotate_g(new, 1)
        rotate_b(new, 2)
        
        if text == b''and len(text) < chunk :
            break
    
    dump(empty, rotated_content_header, fd)
 

