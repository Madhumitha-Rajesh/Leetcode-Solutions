class Solution:
    def isPalindrome(self, s: str) -> bool:

        s1=s.lower()
        left=0
        right=len(s)-1
        
        while left<right:
            #skip invalid characters from left
            while left<right and not s1[left].isalnum():
                left+=1
            #skip invalid characters from right
            while left<right and not s1[right].isalnum():
                right-=1

            if s1[left]!=s1[right]:
                return False
            left+=1
            right-=1
        return True

        
        
        
