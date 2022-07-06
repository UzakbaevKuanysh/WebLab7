a = int(input())
b = int(input())
if a > b :
    print('Error, a can not bet greater than b !')
    exit()
for  i in range(a,b):
    if i % 2 == 0 :
        print(i, end =" ")