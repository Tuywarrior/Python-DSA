##Proper Logic Code:
-> Time Complexity: O(N)
Logic: We need 2 arrays: left and right which stores the left/right most max value from the ith element.
  Then we loop through the array again to calculate the water stored by this formula:
potential=min(left,right)-value
waterstored+=potential

##CODE:
class Solution:
    def trap(self, height: List[int]) -> int:
        l=len(height)
        left=right=0
        max_left=[0]*l
        max_right=[0]*l
        #looping to fill max_left and max_right
        for i in range(l):
            j=-(i+1)
            max_left[i]=left
            max_right[j]=right
            left=max(left,height[i])
            right=max(right,height[j])

        trap=0
        for i in range(l):
            potential=min(max_left[i],max_right[i])-height[i]
            if potential>0:
                trap+=potential
        return trap

