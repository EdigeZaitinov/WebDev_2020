def main():
    size=int(input())
    nums=[]
    for i in range(0,size):
        num=int(input())
        nums.append(num)
    print(second_max(nums))

def second_max(nums):
    first=-1000000
    second=-1000000
    nums=sorting(nums)
    for i in range(0,len(nums)):
        if first<nums[i]:
            second=first
            first=nums[i]
    return second

def sorting(nums):
    for i in range(0,len(nums)-1):
        for i in range(0,len(nums)-1):
            if nums[i]>nums[i+1]:
                vari=nums[i]
                nums[i]=nums[i+1]
                nums[i+1]=vari
    return nums
main()
