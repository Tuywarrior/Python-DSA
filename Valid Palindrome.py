#Logic:
-> Use a 2 pointer technique to start from the beginning and at the end respectively. Check if the two chars at the indices are same or not.
If not return False. If it's not an alphanumeric character, skip it

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s==" ":
            return True
        i=0
        j=len(s)-1
        while i<j:
            if s[i].lower()==s[j].lower():
                i+=1
                j-=1
            elif not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            else:
                return False
        return True
