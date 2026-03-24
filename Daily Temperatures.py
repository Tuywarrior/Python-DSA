class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        my_stack=[]
        n=len(temperatures)
        my_list=[0]*n
        # 73 74 75 71 69 72 76 73
        my_stack.append((temperatures[0],0))
        for i in range(1,n):
            while my_stack and my_stack[-1][0]<temperatures[i]:
                #print(my_stack)
                my_list[my_stack[-1][1]]=i-my_stack[-1][1]
                my_stack.pop()
            my_stack.append((temperatures[i],i))
        return my_list
