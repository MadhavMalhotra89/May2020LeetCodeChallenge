class Solution:
    def firstUniqChar(self, s: str) -> int:
        obj = {}
        for key, value in enumerate(s):
            if value in obj:
                obj[value][0] += 1
            else:
                obj[value] = [1, key]
        #print(obj)
        for key,value in obj.items():
            if value[0] == 1:
                return value[1]
        return -1
