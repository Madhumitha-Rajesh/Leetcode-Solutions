class Solution:
    def isValid(self, s: str) -> bool:

        stk=[]
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            #push openining brackets into the stack
            if ch=='(' or ch=='{' or ch=='[':
                stk.append(ch)
            #if closing bracket
            else:
                if not stk:
                    return False
                #check if top of stack does not match closing brackets
                if stk[-1]!=pairs[ch]:
                    return False
                #matching pair found-> pop
                stk.pop()
                
        return len(stk)==0



        
