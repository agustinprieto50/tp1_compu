z = [
     [[b'\xff', b'\xff', b'\xff'], [b'\xff', b'\xff', b'\xff'], [b'\xff', b'\xff', b'\xff'], [b'\xff', b'\xff', b'\xff']],
     [[b'\xff', b'\xff', b'\xff'], [b'\xff', b'\xff', b'\xff'], [b'\xff', b'\xff', b'\xff'], [b'\xff', b'\xff', b'\xff']],
     [[b'\xff', b'\xff', b'\xff'], [b'\xff', b'\xff', b'\xff'], [b'\xff', b'\xff', b'\xff'], [b'\xff', b'\xff', b'\xff']],
     ]

by = [b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h', b'i', b'j', b'k', b'l', b'm', b'n', b'o', b'p', b'q', b'r',
b's', b't', b'u', b'v', b'w', b'x', b'y', b'z', b'1', b'2', b'3', b'4',b'5', b'6', b'7', b'8', b'9', b'#']


rows = len(z)
cols = len(z[0])



print(by[0::3], 'aca')


item = list()
row = list()
for i in by:
  
    item.append(i)

    if len(item) == 3:
        row.append(item) 
        item = []

index = [0,1,2]
for j in index:
    f = rows - 1
    c = 0
    b = 0 
    for i in by[j::3]:
        print(i)
        z[f][c][j] = i
        print
        f -= 1
        
        if f == -1:
            c+=1
            f = rows - 1
        if f == 0 and c == (cols-1):
            z[f][c][j] = i



for i in z:
    print(i)



indice = []




# for i in range(3):
#     for j in range(rows*cols):
    
    
#         z_small[f][c][i] = small[ff][cc][i]
#         f += 1
#         cc -= 1
#         if cc == -1:
#             f = 0
#             c += 1
#             cc = (len(by[0]))-1
#             ff += 1
#         if f == (rows-1) and c == (cols-1):
#             z_small[f][c][i] = small[ff][cc][i]
#             f = 0
#             c = 0
#             ff = 0
#             cc = (len(small[0]))-1


            
    
#     # if 
#     # print(z)
    
#     # if cc == 0:
#     #     f = 0
#     #     cc = 3
#     #     ff +=1
#     #     c += 1
# for i in z_small:
#     print(i)


#     # zero[f_new][c_new][b_new] = byte_str[f_old][c_old][b_old]
#         #print(zero)
#         # f_new += 1
#         # # b_new += 1
#         # c_old -= 1
#         # if c_old == -1:
#         #     c_old = cantidad_col-1
#         #     f_old += 1
#         #     c_new +=1
#         #     f_new = 0



#         # c_new += 1
#         # f_new = 0
#         # f_old += 1
#         # c_old = cantidad_col -1

        
     
        
            
            
        # if f_old == 2 and c_old == 0:
        #     for i in zero:
        #         print(i)
        #     break
    









# if total == int(len(chunk[0])/3):
        #     total = 0
        #     print('2 wait hijo')
        #     barrier.wait()  






# def rotate(chunk, chunksz):
#     j = 0
#     global index
#     global empty
#     rows = len(empty)
#     total = 0
#     while True:
#         print('1 wait hijo r')
#         barrier.wait()
        
#         if total == (len(chunk)/3):
#             print('2 wait hijo r')
#             barrier.wait()
#         for i in chunk[0]:
#             empty[index[0]][index[1]][j] = i[j]
#             total += 1
            
#             index[0] -= 1
#             if index[0] == -1 and index[1] == rows+1:
#                 empty[index[0]][index[1]][j] = i[j]
#                 total += 1
        
#             if index[0] == -1:
#                 index[1] += 1
#                 index[0] = rows - 1
#         if len(chunk[0]) < chunksz:
#             break
#         print('3 wait hijo r')
#         barrier.wait()

    
# def rotate_g(chunk, chunksz):
#     j = 1
#     global index2
#     global empty
#     rows = len(empty)
#     total = 0
#     while True:
#         barrier.wait()
#         print('1 wait hijo g')
#         print(total)
#         print('aca')
#         if total == (len(chunk)/3):
#             print('2 wait hijo g')
#             barrier.wait()
#         for i in chunk[0]:
#             empty[index2[0]][index2[1]][j] = i[j]
#             total += 1
#             index2[0] -= 1
#             if index2[0] == -1 and index2[1] == rows+1:
#                 empty[index2[0]][index2[1]][j] = i[j]
#                 total += 1
#             if index2[0] == -1:
#                 index2[1] += 1
#                 index2[0] = rows - 1
#         if len(chunk[0]) < chunksz:
#             break
#         print('3 wait hijo g')
#         barrier.wait()


# def rotate_b(chunk, chunksz):
#     j = 2
#     global index3
#     global empty
#     rows = len(empty)
#     total = 0
#     while True:
#         print('1 wait hijo b')
#         barrier.wait()
        
#         if total == (len(chunk)/3):
#             print('2 wait hijo b')
#             barrier.wait()
#         for i in chunk[0]:
#             empty[index3[0]][index3[1]][j] = i[j]
#             total += 1
#             index3[0] -= 1
#             if index3[0] == -1 and index3[1] == rows+1:
#                 empty[index3[0]][index3[1]][j] = i[j]
#                 total += 1

#             if index3[0] == -1:
#                 index3[1] += 1
#                 index3[0] = rows - 1
#         if len(chunk[0]) < chunksz:
#             break
#         print('3 wait hijo b')
#         barrier.wait()
        