#!/usr/bin/python3
import os
import argparse
from re import T
from filtro import plain_matrix, bytes_matrix
from manager import open_file, header, dump, rotate_header
from threading import Thread, Barrier


barrier = Barrier(4)

def rotate(chunk, chunksz):
    j = 0
    global index
    global empty
    rows = len(empty)
    while True:
        print('1 wait hijo r')
        barrier.wait()
        for i in chunk[0]:
            empty[index[0]][index[1]][j] = i[j]
            index[0] -= 1
            if index[0] == -1 and index[1] == rows+1:
                empty[index[0]][index[1]][j] = i[j]
            if index[0] == -1:
                index[1] += 1
                index[0] = rows - 1
        if len(chunk[0]) < chunksz:
            break
        barrier.wait()

    
def rotate_g(chunk, chunksz):

    j = 1
    global index2
    global empty
    rows = len(empty)
    while True:
        print('1 wait hijo g')
        barrier.wait()
        for i in chunk[0]:
            empty[index2[0]][index2[1]][j] = i[j]
            index2[0] -= 1
            if index2[0] == -1 and index2[1] == rows+1:
                empty[index2[0]][index2[1]][j] = i[j]
            if index2[0] == -1:
                index2[1] += 1
                index2[0] = rows - 1
        if len(chunk[0]) < chunksz:
            break
        barrier.wait()


def rotate_b(chunk, chunksz):

    j = 2
    global index3
    global empty
    rows = len(empty)
    while True:
        print('1 wait hijo b')
        barrier.wait()
        for i in chunk[0]:
            empty[index3[0]][index3[1]][j] = i[j]
            index3[0] -= 1
            if index3[0] == -1 and index3[1] == rows+1:
                empty[index3[0]][index3[1]][j] = i[j]
            if index3[0] == -1:
                index3[1] += 1
                index3[0] = rows - 1
        if len(chunk[0]) < chunksz:
            break
        barrier.wait()


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='TP1 - procesa ppm')
    parser.add_argument('-s', '--size', action="store", metavar='SIZE', type=int,
                        required=True, help='Bloque de lectura')
    parser.add_argument('-f', '--file', action="store", metavar='FILE', type=str,
                        required=True, help='archivo a procesar')
    # parser.add_argument('-l', '--', action="store", metavar='SIZE', type=int,
    #                     required=True, help='Bloque de lectura')
    
    args = parser.parse_args()
    fd = args.file
    args.size = args.size - (args.size%3) 
    chunk = args.size
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

    tasks = [rotate, rotate_g, rotate_b]
    new = [0]
    threads = []
    for i in tasks:
        threads.append(Thread(target=i, args=(new, chunk)))

    while True:
        text = os.read(file, chunk)
        new[0] = bytes_matrix(text)
        for i in threads:
            if not i.is_alive() :
                i.start()
        barrier.wait()
        if len(text) < chunk :
            break
        barrier.wait()
    
    for i in threads:
        i.join()
    dump(empty, rotated_content_header, fd)
 
