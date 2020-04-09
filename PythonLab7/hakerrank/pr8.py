def main():
    num1=int(input())
    num2=int(input())
    num3=int(input())
    num4=int(input())
    comprehensive_list(num1,num2,num3,num4)
    
def comprehensive_list(num1,num2,num3,num4):
    nums=[num1,num2,num3]
    for c in range(0,num4):
        it=0
        it+=1
        for i in range(0,len(nums)):
            nums[i]=nums[i]-it
            if (sum_of_array(nums)<num4) and sum_of_array(nums)>=0:
                print(nums)
                transposition(nums)        

def sum_of_array(nums):
    sum=0
    for i in range(0,len(nums)):
        sum=sum+nums[i]
    return sum

def transposition(nums):
    if nums[1]==nums[2] and nums[0]!=nums[1]: 
        print("["+str(nums[1])+", "+str(nums[0])+", "+str(nums[2])+"]") 
        print("["+str(nums[2])+", "+str(nums[1])+", "+str(nums[0])+"]") 
    if nums[0]==nums[1] and nums[1]!=nums[2]:
        print("["+str(nums[0])+", "+str(nums[2])+", "+str(nums[1])+"]") 
        print("["+str(nums[2])+", "+str(nums[1])+", "+str(nums[0])+"]") 
main()