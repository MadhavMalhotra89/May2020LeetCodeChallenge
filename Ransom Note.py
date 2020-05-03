class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        obj = {}
        for c in magazine:
            obj[c] = obj.get(c, 0) + 1
        for c in ransomNote:
            if c in obj and obj[c] > 0:
                obj[c] -= 1
            else:
                return False
        return True
