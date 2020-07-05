def change(nums):
    for i in range(len(nums)):
        nums[i]+=1

temp=[1,2,3,4,5,6,7,8,9]
change(temp)
print(temp)