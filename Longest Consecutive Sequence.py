Brute Force:

-> We use the sort function to sort the list and then check if the preceding number is small than the current number
-> Time Complexity: O(NlogN)


## CODE: 
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        count=1
        max_count=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1] and nums[i]-nums[i-1]==1:
                count+=1
                max_count=max(max_count,count)
            elif nums[i]==nums[i-1]:
                continue
            else:
                count=1
        return max_count


Advanced Solution:
-> In this we store the list in a set. The solution involves first confirming the smallest num of the sequence and if yes, we move ahead
with a while loop to confirm the presence of a consecutive sequence in that set.
-> Time complexity: O(N) 
-> Space Complexity: O(N)

-> Although we do parse the while loop but we are checking the element only twice and not looping through it twice because the case where 
num is not the starting element is being skipped and not used in the while loop.


## CODE:
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1=set(nums)   
        seq=0
        for num in set1:
            if num-1 not in set1:
                next=num
                counter=0
                while next in set1:
                    next+=1
                    counter+=1
                seq=max(seq,counter)
        return seq

