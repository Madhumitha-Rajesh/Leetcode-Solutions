class Solution:
    def rob(self, nums: List[int]) -> int:
        one=0
        two=0
        #recursion
        for money in nums:
            one,two=two,max(two,one+money)
        return two
