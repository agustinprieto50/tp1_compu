import os
import sys
import re

class Manager():

    def open_file(self, f):
        try:
            f_read = os.open(f, os.O_RDWR)
            head_lenght = self.header(f_read)
            # empieza a leer desde el final del header
            os.lseek(f_read, (self.header(f_read))[1], 0)
        except FileNotFoundError:
            sys.stdout.write('ERROR. File "{}" does not exist.\n'.format(f))
            exit(1)
        return f_read

    def header(self, f):
        fd = os.read(f, 150)
        regex = re.split(r'(P6|P3){1,}(\n){1,}(#\s*.*)(\n){1,}(600|5[0-9][0-9]|4[0-9][0-9]|3[0-9][0-9]|2[0-9][0-9]|1[0-9][0-9]|[1-9]?[0-9]){1}(\s){1,}(500|4[0-9][0-9]|3[0-9][0-9]|2[0-9][0-9]|1[0-9][0-9]|[1-9]?[0-9]){1}(\n){1,}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])', fd)
        length_h = 0
        for i in regex:
            length_h += len(i.encode())
        return [regex, length_h]

