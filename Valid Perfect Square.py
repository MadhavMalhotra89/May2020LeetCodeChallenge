class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        """for i in range(0, int(pow(num,0.5)+1)):
            if i*i == num:
                return True
        return False"""
        left, right = 2, num //2
        while left <= right:
            mid = (left + right) // 2
            guess_sq = mid * mid
            if guess_sq == num:
                return True
            elif guess_sq > num:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
