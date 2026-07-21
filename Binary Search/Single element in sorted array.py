class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            #make the mid even if odd
            if mid%2==1:
                mid-=1
            #check if mid and the next element are same and move left
            if nums[mid]==nums[mid+1]:
                left=mid+2
            else:
                right=mid
        return nums[left]
        
        
