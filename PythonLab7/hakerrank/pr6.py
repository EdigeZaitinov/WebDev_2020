def main():
    num=int(input())
    print(leap(num))

def leap(num):    
    if ((num%4==0 and num%100!=0) or (num%400==0 and num%4==0) or (num%100!=0 and num%400==0)):
        return "true"
    elif ((num%4!=0 and num%100==0) or (num%400!=0 and num%4!=0) or (num%100==0 and num%400!=0)):
        return "false" 

main()