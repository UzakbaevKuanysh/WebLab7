n = int(input())
a = str(n)
sum = 0
for i in range(len(a)):
    sum = sum + int(a[len(a)-i-1]) * (2 ** i)
print(sum)