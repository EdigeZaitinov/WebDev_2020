range1=int(input())
range2=int(input())
balance=int(input())
devisor=int(input())
word=""
for i in range(range1,range2):
    if (i%devisor)==balance:
        word=word+str(i)+" "
print(word)