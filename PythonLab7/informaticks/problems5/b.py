def main():
    num1=int(input())
    num2=int(input())
    print(power(num1,num2))

def power(num1,num2):
    num3=num1
    for i in range(1,num2):
        num1*=num3
    return num1

main()