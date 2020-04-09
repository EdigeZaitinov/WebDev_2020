import random
num=int(input())
num=str(num)
OK=0
OK1=0
num1=int(input())
if num==num[::-1] and len(num)==4:
    OK=1 
else:
    OK=0

if num1==1:
    OK1=1
else:
    OK1=0

if OK==OK1:
    print("YES")
else:
    print("NO")
