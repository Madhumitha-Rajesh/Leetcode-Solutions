class Solution:
    def subarraySum(self, arr, target):
        # code here
        win_sum=0
        left=0
        for right in range(len(arr)):
            win_sum+=arr[right]
            
            while win_sum>target:
                win_sum-=arr[left]
                left+=1
            if win_sum==target:
                return [left+1,right+1]
        return [-1]
                
