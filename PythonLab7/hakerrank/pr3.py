def main():
    num1=int(input())
    num2=int(input())
    print(sum(num1,num2))
    print(dif(num1,num2))
    print(prod(num1,num2))

def sum(num1,num2):
    return num1+num2

def dif(num1,num2):
    return num1-num2

def prod(num1,num2):
    return num1*num2

main()