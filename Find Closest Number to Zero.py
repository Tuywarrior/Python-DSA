##Logic:
'''
Create 2 variables, one of the difference and the other for the max number. 
Loop through the list and check if the difference is greater than or equal to the absolute value of the number
-> If yes: update the difference variable with it and if the number is larger than the max number variable, update it also

'''


##Code:
def findClosestNumber(self, nums: List[int]) -> int:
        least_diff=1e5
        largest_num=-1e5
        for i in nums:
            if least_diff>=abs(i):
                least_diff=min(least_diff,abs(i))
                if(largest_num!=abs(i)):
                    largest_num=i
                print(largest_num)
        return round(largest_num) 
