numbers=[]
last=int(input())
for i in range(0,last):
    num=int(input())
    numbers.append(num)
for j in range(0,last):
    if numbers[j]%2==0:
        print(numbers[j])