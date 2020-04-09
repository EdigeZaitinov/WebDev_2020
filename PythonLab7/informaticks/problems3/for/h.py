num=int(input())
word=""
for i in range(num,0,-1):
    if (num/i)==round(num/i):
        word=word+str(int(num/i))+" "
print(word)