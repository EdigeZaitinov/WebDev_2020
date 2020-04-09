num1=int(input())
num2=int(input())
word=""
for i in range(num1,num2):
    if i%2==0:
        word=word+str(i)+" "
print(word)