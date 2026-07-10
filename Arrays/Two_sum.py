class Solution:
	def twoSum(self, arr, target):
		# code here
		
		seen=set()
		
		for num in arr:
		    compliment=target-num
		    
		    if compliment in seen:
		        return True
		    
		    seen.add(num)
		return False
		  
		        
		  
		    
		  
		       
