class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """while k > 0:
            k -= 1
            i = 0
            while i < len(num) - 1:
                if num[i] > num[i+1]:
                    break
                i+=1
            num = num[:i] + num[i+1:]
        
        if len(num) == 0:
            return "0"
        else:
            return str(int(num))"""
        if len(num) <= k:
            return '0'
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        if k:
            stack = stack[:-k]
        return ''.join(stack).lstrip('0') or '0'
