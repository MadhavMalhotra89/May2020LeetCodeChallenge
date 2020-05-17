class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        obj1 = {}
        for i in p:
            obj1[i] = obj1.get(i, 0) + 1
        matched = 0
        answer = []
        window_start = 0
        for index, val in enumerate(s):
            if val in obj1:
                obj1[val] -= 1
                if obj1[val] == 0:
                    matched += 1
            if matched == len(obj1):
                answer.append(window_start)
            if index >= len(p) - 1:
                temp = s[window_start]
                window_start += 1
                if temp in obj1:
                    if obj1[temp] == 0:
                        matched -= 1
                    obj1[temp] += 1
        return answer
