class Solution:
    def longestUniqueSubstring(self, s):
        # code here
        seen={}
        left=0
        max_len=0
        
        for right in range(len(s)):
            #check if ch is already in seen
            if s[right] in seen and seen[s[right]]>=left:
                left=seen[s[right]]+1
            #update seen
            seen[s[right]]=right
            
            #update max_len
            max_len=max(max_len,right-left+1)
        return max_len
            
