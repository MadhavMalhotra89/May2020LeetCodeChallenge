class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        obj = {}
        obj1 = {}
        for s in s1:
            obj[s] = obj.get(s, 0) + 1
        for s in s2:
            obj1[s] = obj1.get(s, 0) + 1
        if obj1 == obj:
            return True
        window_start = 0
        found = 0
        for window_end in range(len(s2)):
            if s2[window_end] in obj:
                obj[s2[window_end]] -= 1
                if obj[s2[window_end]] == 0:
                    found += 1
            if found == len(obj):
                return True
            if window_end >= len(s1)-1:
                temp = s2[window_start]
                window_start += 1
                if temp in obj:
                    if obj[temp] == 0:
                        found -= 1
                    obj[temp] += 1
        return False
