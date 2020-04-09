def main():
    num1=int(input())
    num2=int(input())
    num3=int(input())
    num4=int(input())
    print(minimum(num1,num2,num3,num4))

def minimum(num1,num2,num3,num4):
    nums=[num1,num2,num3,num4]
    minx=1000000
    for i in range(0,4):
        if minx>nums[i]:
            minx=nums[i]
    return minx

main()