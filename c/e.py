a = int(input())

c = str(a)
count = 0
for  i in range(len(c)):
    count = count + int(c[i])
print(count)