def main():
    bool1=int(input())
    bool2=int(input())
    print(xor(bool1,bool2))

def xor(num1,num2):
    if(num1==0 or num1==1) and (num2==0 or num2==1):
        if num1!=num2:
            return 1
        else:
            return 0
    else:
        return "not bool"

main()