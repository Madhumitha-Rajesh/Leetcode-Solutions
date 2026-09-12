class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        j=k-1
        curr_sum=sum(nums[i:j+1])
        max_sum=curr_sum
        for _ in range(len(nums)-k):
            curr_sum-=nums[i]
            i+=1
            j+=1
            curr_sum+=nums[j]
            max_sum=max(max_sum,curr_sum)
        return max_sum/k
