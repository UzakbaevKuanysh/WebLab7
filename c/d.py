a = int(input())
b = int(input())
c = str(a)
count = 0
for  i in range(len(c)):
    if c[i] == str(b):
        count = count + 1
print(count)