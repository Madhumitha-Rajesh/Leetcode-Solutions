class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        
        seen={}
        prefix_sum=0
        max_len=0
        
        for i in range(len(arr)):
            prefix_sum+=arr[i]
            #check if prefix sum=k
            if prefix_sum==k:
                max_len=i+1
            if (prefix_sum-k) in seen:
                length=i-seen[prefix_sum-k]
                max_len=max(max_len,length)
            if prefix_sum not in seen:
                seen[prefix_sum]=i
        return max_len
            

            
        
        
    
