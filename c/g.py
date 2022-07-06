a = int(input())

minnumber = a

for i in range(2,a):
    if a % i == 0:
        minnumber = min(minnumber,i)
print(minnumber)