n = int(input())

a = list(map(int, input().split()))
count = 0
for i in range(1,n):
    if (a[i]>0 and a[i-1] > 0) or (a[i] < 0 and a[i-1] < 0):
        count = count + 1
    if (count>0):
        print('YES')
        exit()
print('NO')