numbers=[]
sum=0
last=int(input())
for i in range(0,last):
    num=int(input())
    numbers.append(num)
for j in range(0,last-1):
    if (numbers[j]>0 and numbers[j+1]>0):
        sum+=1
    elif (numbers[j]<0 and numbers[j+1]<0):
        sum+=1
if sum>1:
    print("YES")
else:
    print("NO")