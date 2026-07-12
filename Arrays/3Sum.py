class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans=[]

        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            #skip duplicate i values
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                tot=nums[i]+nums[left]+nums[right]
                if nums[i]+nums[left]+nums[right]==0:
                    ans.append([nums[i],nums[left],nums[right]])
                    #skip left duplicates
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    #skip right duplicates
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left += 1
                    right -= 1
                elif tot<0 :
                    left+=1
                else:
                    right-=1
        return ans

            

            

        
