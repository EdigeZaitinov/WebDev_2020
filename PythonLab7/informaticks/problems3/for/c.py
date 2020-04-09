first=int(input())
last=int(input())
word=""
for i in range(first,last):
    if (i**0.5)==round(i**0.5):
        word=word+str(i)+" "
print(word)

