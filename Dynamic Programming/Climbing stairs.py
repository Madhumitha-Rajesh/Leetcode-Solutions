class Solution:
    def climbStairs(self, n: int) -> int:
        #recursion
        one=1
        two=1
        for i in range(n-1):
            one,two=two,one+two

        return two
