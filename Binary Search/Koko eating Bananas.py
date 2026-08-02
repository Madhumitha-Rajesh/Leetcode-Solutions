class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #set boundaries
        left=1
        right=max(piles)
        ans=right
        #binary search loop
        while left<=right:
            mid=(left+right)//2
            #calcualte hours 
            hours=0
            for pile in piles:
                hours+=(pile+mid-1)//mid

            if hours<=h:
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans
