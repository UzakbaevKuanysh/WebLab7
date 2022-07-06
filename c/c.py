a = int(input())
b = int(input())
if a > b :
    print('Error, a can not bet greater than b !')
    exit()
for  i in range(a,b):
    if type(i ** (1/2)) is int:
        print(i, end =" ")