num=int(input())
num1=0
for i in range(num,0,-1):
    if (num/i)==round(num/i):
        num1+=1
print(num1)