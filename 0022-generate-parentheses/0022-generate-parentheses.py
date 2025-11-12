class Solution:
    def generate(self,curr_str,ans,Open,Close,n):
        if(Open==Close and Open+Close==2*n):
            ans.append(curr_str)
            return
        if(Open>n):
            return
        if(Close>Open):
            return    
        self.generate(curr_str+"(",ans,Open+1,Close,n)
        self.generate(curr_str+")",ans,Open,Close+1,n)
    def generateParenthesis(self,n):
        curr_str=""
        ans=[]
        Open=0
        Close=0
        self.generate(curr_str,ans,Open,Close,n)
        return ans
obj=Solution()
n=2
print(obj.generateParenthesis(n))                    