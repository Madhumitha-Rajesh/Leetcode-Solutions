class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        
        max_sum=arr[0]
        
        curr_sum=0
        
        for num in arr:
            curr_sum+=num
            
            if curr_sum>max_sum:
                max_sum=curr_sum
            
            if curr_sum<0:
                curr_sum=0
        return max_sum
            
