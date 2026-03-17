Time Compelexity: O(N)
Space Complexity: O(1)

#Logic: have 2 pointers 1 at the beginning and the other at the end. Make sure to have conditions for the iteration:
1) if sum<target: i++
2) is sum>target: j++

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            if numbers[j]+numbers[i]>target:
                j-=1
            elif numbers[j]+numbers[i]<target:
                i+=1
            else:
                return [i+1,j+1]
