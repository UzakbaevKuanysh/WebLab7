a = int(input())
b = int(input())
if a<0:
    a = a* (-1)
c = a * b 
if ( c >= 109):
    print ( c - 109)
else:
    print(109 - c)