num=int(input())
num1=1
i=1
word=""
while i!=num:
    if (num/i)==round(num/i):
        num1=int(num/i)
    i+=1
print(str(num1))
