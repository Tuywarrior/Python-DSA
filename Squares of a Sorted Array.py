

#Brute Force: 
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            nums[i]= nums[i]*nums[i]
        nums.sort()
        return nums

# Advanced Solution:
-> Used a 2 pointer approach to square it and then sort it
-> Time Complexity: O(N)
-> Space Complexity: O(N)

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        j=len(nums)-1
        my_list=[0]*len(nums)
        k=j
        while(i<=j):
            if abs(nums[i])<=abs(nums[j]):
                my_list[k]=nums[j]**2
                j-=1
            else:
                my_list[k]=nums[i]**2
                i+=1
            k-=1
        return my_list
