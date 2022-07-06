n = int(input())
minN = n
i = 2
while i < n :
    if n % i == 0:
        minN = min(minN,i)
    i = i +1
print(minN)