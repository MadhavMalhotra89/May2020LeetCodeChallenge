class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not S or not J:
            return 0
        count = 0
        for c in S:
            if c in J:
                count += 1
        return count
