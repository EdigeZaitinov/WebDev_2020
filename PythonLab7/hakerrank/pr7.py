def main():
    num=int(input())
    print(print_array(num))

def print_array(num):
    nums=''
    for i in range(1,num+1):
        nums=nums+str(i)
    return nums

main()