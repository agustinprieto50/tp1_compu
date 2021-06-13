import os


# def rot(z, bytes_str):
    
#     f = 0
#     c = 0
#     b = 0


#     rows = len(z)
    
#     cols = len(z[0])
    

#     ff = 0
#     cc = (len(bytes_str[0]))-1
#     bb = 0



#     for i in range(3):
#         for j in range(rows*cols):
        
#             z[f][c][i] =bytes_str[ff][cc][i]
#             f += 1
#             cc -= 1
#             if cc == -1:
#                 f = 0
#                 c += 1
#                 cc = (len(bytes_str[0]))-1
#                 ff += 1
#             if f == (rows-1) and c == (cols-1):
#                 z[f][c][i] = bytes_str[ff][cc][i]
#                 f = 0
#                 c = 0
#                 ff = 0
#                 cc = (len(bytes_str[0]))-1
        
#     return z





def plain_matrix(rc, head):
    r, c = rc
    c = int(c.decode('utf-8'))
    r = int(r.decode('utf-8'))
    matrix = [[[0, 0, 0] for i in range(c)] for j in range(r)]
    return matrix

    
def bytes_matrix(bytes_str):
    item = list()
    row = list()
    original_list = list()
    for i in bytes_str:
        x = bytes([i])
        original_list.append(x)
    for i in original_list:
        item.append(i)
        if len(item) == 3:
            row.append(item) 
            item = []
    return row


# def rotate(empty, chunk, j):

 
#     chunk_list = chunk
#     rows = len(empty)
#     cols = len(empty[0])

#     color = [0,1,2]
#     for j in color:
#         f = rows - 1
#         print(f)
#         c = 0
#         b = 0 
#         for i in chunk_list:
#             empty[f][c][j] = i[j]
#             f -= 1
#             if f == -1:
#                 c+=1
#                 f = rows - 1
#             if f == 0 and c == (cols-1):
#                 empty[f][c][j] = i[j]
    
#     return empty


# def matrix(bytes_str, row_col):
    
#     matriz = list()
#     item = list()
#     row = list()
#     r, c = row_col


#     r = int(r.decode('utf-8'))
#     c = int(c.decode('utf-8'))
#     for i in bytes_str:
#         item.append(bytes([i]))
#         if len(item) == 3:
#             row.append(item)
#             item = []

#             if len(row) == c:
#                 matriz.append(row)
#                 # print(len(row))
#                 row = []
    
#     return matriz


# def filtro(text, length_header, rotated_content_header, inverted_sz, o_size, ):
#     # os.lseek(fd, int(length_header), 0)
#     # text = os.read(fd, chunk_sz)

#     # original_matrix = matrix(text, inverted_sz) 
#     plain_rotated = plain_matrix(o_size, rotated_content_header)

#     while True:
#         if text == b'':
#             rotated = rotate(plain_rotated, text, 'hdh')
        

#     for i in rotated:
#         print(i)

    # plain_ppm = os.open('rotate.ppm', os.O_RDWR | os.O_CREAT)
    # os.write(plain_ppm, rotated_content_header)
    # if text == b'':
    #     sep = b''
    #     for i in rotated:
    #         row = b''
    #         for x in i:
    #             row += sep.join(x)
    #         os.write(plain_ppm, row)





        
        # if i == chunk_list[len(chunk_list)-1]:
        #     empty[index[0]][index[1]][j] = i[j]
       
    
            #   print(empty)
        # if i == chunk_list[len(chunk_list)-1]:
        #     # index = new
        #     # print(constant)
        #     j += 1
        #     index =constant
            # print('here', index)
            # print(empty)
            
            # if index[0] == 0 and index[1] == (cols-1):
                
               
    
    # return empty




 # if index[0] == -1 and index[1] == rows:
        #     # constant[2] += 1
           
        #     index = constant
            