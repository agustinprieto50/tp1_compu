#!/usr/bin/python3
import os
import argparse
from matrix_worker import plain_matrix
from manager import open_file, header, dump, rotate_header
from threading import Thread, Barrier



barrier = Barrier(4)

# j indica la posicion dentro del pixel
def rotate(chunk, chunksz, j):

    # empty es una variable global que representa a la nueva imagen
    global empty

    # fila inicial en empty
    f = len(empty) - 1

    # columna inicial en empty
    c = 0
    b = 0

    index = [f, c ,b]

    # cantidad de filas de la nueva matriz rotada
    rows = len(empty)

    total = 0
    
    while True:
        print('1 wait hijo r')
        # realiza un wait para no empezar a ejecutar antes de que 
        # el hilo main haya llenado el buffer
        barrier.wait()
        
        # a cada byte lo reubicamos en la nueva matriz
        # chunk[0] es el buffer
        for i in chunk[0]:
            print(i)
            # le indicamos el indice
            empty[index[0]][index[1]][j] = i
            
            # subimos una fila
            index[0] -= 1
            total += 1
            
            # aca hace el ultimo ingreso a la matriz rotada
            if index[0] == -1 and index[1] == rows+1:
                print('entro')
                empty[index[0]][index[1]][j] = i
                total += 1
            
            # cuando se ingresaron todos los elementos de una columnna, pasamos a la siguiente
            if index[0] == -1:
                index[1] += 1
                index[0] = rows - 1
            
        # condicion para que frene el loop
        # cuando no haya nada mas para leer
        if len(chunk[0]) < chunksz:
            break

        print('3 wait hijo r')
        
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

    # chequeamos que se multiplo de 3
    chunk = args.size - (args.size%3) 
    # abrimos le archivo
    file = open_file(fd)
    head, length = header(file) 
    len_head = length
    rotated_content_header, inverted_sz, o_size = rotate_header(head)
    os.lseek(file, len_head, 0)
    # es la matriz vacia pero rotada
    empty = plain_matrix(o_size, rotated_content_header)
    empty_original = plain_matrix(o_size, rotated_content_header)

    new = [0]

    threads = []
    for i in range(3):
        # agregamos hilos a la lista thread
        threads.append(Thread(target=rotate, args=(new, chunk, i)))


    contador = 0
    # el tamaño de la imagen rotada
    total_size = len(empty)* (len(empty[0])) * (len(empty[0][0]))

    while True:
        text = os.read(file, chunk)
        new[0] = text

        # suma lo leido
        contador += len(new[0])
       
        # solo startea hilos si no fueron starteados anteriormente
        for i in threads:
            if not i.is_alive() :
                i.start()

        # hacamos un wait para que no se ejecuten los threads primero
        barrier.wait()
        
        # corta cuando el largo de lo leido sea menor al 
        # tamaño del chunk y cuanodo el contador sea igual
        # al tamaño total
        if len(text) < chunk and contador >= total_size:
            break
        
        print('2 wait padre')

        # que no se ejecuten los hilos cuando no hay nada nuevo en el buffer
        barrier.wait()
        
    for i in threads:
        i.join()

    for i in empty:
        print(i)
    
    # lo escribimos en la imagen nueva
    dump(empty, rotated_content_header, fd)
    print('se rotó correctamente la imagen')
