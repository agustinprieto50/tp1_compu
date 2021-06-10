import os


def rotate(z, bytes_str):
    
    f = 0
    c = 0
    b = 0


    rows = len(z)
    
    cols = len(z[0])
    

    ff = 0
    cc = (len(bytes_str[0]))-1
    bb = 0



    for i in range(3):
        for j in range(rows*cols):
        
            z[f][c][i] =bytes_str[ff][cc][i]
            f += 1
            cc -= 1
            if cc == -1:
                f = 0
                c += 1
                cc = (len(bytes_str[0]))-1
                ff += 1
            if f == (rows-1) and c == (cols-1):
                z[f][c][i] = bytes_str[ff][cc][i]
                f = 0
                c = 0
                ff = 0
                cc = (len(bytes_str[0]))-1
        
    return z


def plain_matrix(rc, head):
    plain_ppm = os.open('rotate.ppm', os.O_RDWR | os.O_CREAT)
    os.write(plain_ppm, head)
    sep = b''
    r, c = rc
    c = int(c.decode('utf-8'))
    r = int(r.decode('utf-8'))

    matrix = [[[0, 0, 0] for i in range(c)] for j in range(r)]
   
    return matrix
    

def matrix(bytes_str, row_col):
    
    matriz = list()
    item = list()
    row = list()
    r, c = row_col


    r = int(r.decode('utf-8'))
    c = int(c.decode('utf-8'))
    for i in bytes_str:
        item.append(bytes([i]))
        if len(item) == 3:
            row.append(item)
            item = []

            if len(row) == c:
                matriz.append(row)
                # print(len(row))
                row = []
    
    return matriz


def filtro(fd, length_header, rotated_content_header, inverted_sz, o_size, chunk_sz):
    os.lseek(fd, int(length_header), 0)
    text = os.read(fd, chunk_sz)

    original_matrix = matrix(text, inverted_sz) 
    plain_rotated = plain_matrix(o_size, rotated_content_header)


    rotated = rotate(plain_rotated, original_matrix)


    plain_ppm = os.open('rotate.ppm', os.O_RDWR | os.O_CREAT)
    os.write(plain_ppm, rotated_content_header)
    sep = b''
    for i in rotated:
        row = b''
        for x in i:
            row += sep.join(x)
        os.write(plain_ppm, row)
