import re
import sys


a = int(input())
if a % 2 !=0:
    print('Weird')
elif (a % 2 == 0 and (a>1 and a < 6)):
    print('Not Weird')
elif (a % 2 == 0 and (a > 5 and a < 21)):
    print('Weird')
else:
    print('Not Weird')