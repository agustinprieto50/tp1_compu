import os


def plain_matrix(rc, head):
    r, c = rc
    c = int(c.decode('utf-8'))
    r = int(r.decode('utf-8'))
    matrix = [[['\x00', '\x00', '\x00'] for x in range(c)] for y in range(r)]
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
