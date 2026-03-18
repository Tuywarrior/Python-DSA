#Brute Force:
Time Compelxity: O(N)^3
Space Complexity: O(N)

-> Logic: We use 3 pointers, a for loop for the first pointer and a while loop for the other 2 pointers.
-> We start i from 0 , j from i+1 and k from the end itself. We check if the sum of the numebrs at these indices is equal to zero or not.
-> we also check if the list of numbers that we have obtained, is it already present in out List of lists or not?

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        my_list=[]
        #[-4,-1,-1,0,1,2]
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                list1=[nums[i],nums[j],nums[k]]
                if sum==0 and list1 not in my_list:
                    my_list.append(list1)
                    j+=1
                    k-=1
                elif sum<0:
                    j+=1
                else:
                    k-=1
        return my_list



##ADVANCED SOLUTION:
TIME COMPLEXITY: O(N)^2
SPACE COMPLEXITY: O(N)
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        my_list=[]
        #[-4,-1,-1,0,1,2]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                list1=[nums[i],nums[j],nums[k]]
                if sum==0:
                    my_list.append(list1)
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif sum<0:
                    j+=1
                else:
                    k-=1
        return my_list

