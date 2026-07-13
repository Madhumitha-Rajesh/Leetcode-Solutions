class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        #find the sum of 1st window
        win_sum=sum(arr[:k])
        max_sum=win_sum
        
        for i in range(k,len(arr)):
            #slide the window
            win_sum=win_sum-arr[i-k]+arr[i]
            
            #update maximum length
            max_sum=max(max_sum,win_sum)
        return max_sum
            
        
                
