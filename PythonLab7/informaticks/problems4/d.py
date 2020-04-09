numbers=[]
sum=0
last=int(input())
for i in range(0,last):
    num=int(input())
    numbers.append(num)
for j in range(0,last-1):
    if numbers[j]<numbers[j+1]:
        sum+=1
print(sum) 