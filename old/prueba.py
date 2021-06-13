a = [0,0,0,0,0,0]
b = [55,266,314,54,8,4]
ct = 0
print(int(len(a)/3))
for i in range(int(len(a)/3)):
    print(i)
    a[i] = b[i]
    i +=3

print(a)