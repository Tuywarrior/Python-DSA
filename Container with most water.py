##Brute Force
-> Time complexity: O(N)^2
Logic: We iterate through 2 loops and check for the maximum area from the length and breadth obtained

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=len(height)
        area=0
        for i in range(l-1):
            length=height[i]
            for j in range(i+1,l):
                breadth=j-i
                length=min(height[j],height[i])
                area=max(area,length*breadth)
                #print(length,breadth)
        return area


#Advanced solution:
Logic: We iterate through only 1 loop moving forward, use a 2 pointer approach and check if the height of jth
value is less than the ith value then we move the jth pointer to the left and vice vera

-> Time complexity: O(N)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=len(height)
        area=0
        i=0
        j=l-1
        while i<j and i<l-1 and j>0:
            length=min(height[j],height[i])
            breadth=j-i
            area=max(area,length*breadth)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return area
