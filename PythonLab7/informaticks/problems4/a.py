numbers=[]
last=int(input())
for i in range(0,last):
    num=int(input())
    numbers.append(num)
i = 0
while i < len(numbers):
    if i%2==0:
        print(numbers[i])
    i += 1

