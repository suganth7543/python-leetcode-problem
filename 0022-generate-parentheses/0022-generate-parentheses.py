class Solution(object):
    def generateParenthesis(self, n):
        results = []
        stack = []
        stack.append(('', n, n))
        while stack:
            sofar, left, right = stack.pop()
            if left == 0 and right == 0:
                results.append(sofar)
            if left > 0:
                stack.append((sofar + "(", left-1, right))
            if right > left:
                stack.append((sofar + ")", left, right-1))
        return results