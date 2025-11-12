class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        # define DP as longest valid parentheses start at index i        
        dp = [0] * len(s)

        # first scan, pairs up all () as base case
        for i in range(len(s)-1):
            if s[i] == '(' and s[i+1] == ')':
                dp[i] = 2

        old_sum = 0
        while sum(dp) > old_sum:                     
            old_sum = sum(dp)      
                  
            for i in range(len(dp)):                
                if i + dp[i] < len(dp):                     
                    dp[i] = max(dp[i], dp[i] + dp[i+dp[i]])
                    
                if i > 0 and s[i-1] == '(' and i+dp[i] < len(dp) and s[i+dp[i]] == ')':
                    dp[i-1] = max(dp[i-1], dp[i] + 2)

        return max(dp)









        