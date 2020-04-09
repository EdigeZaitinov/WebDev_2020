def main():   
    num=int(input())
    if wrd(num)==1:
        print("Weird")
    elif wrd(num)==0:
        print("Not Weird")

def wrd(num):
    if num%2==1 or (num%2==0 and (num>=6 and num<=20)):
        return 1
    elif (num%2==0 and (num>=2 and num<=5)) or (num%2==0 and num>20):
        return 0

main()