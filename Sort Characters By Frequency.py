import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        min_heap = []
        obj = {}
        answer = ''
        for i in s:
            obj[i] = obj.get(i, 0) + 1
        for key, value in obj.items():
            heappush(min_heap, (-value, key))
        for _ in range(len(min_heap)):
            popped = heappop(min_heap)
            value = -popped[0]
            key = popped[1]
            for _ in range(value):
                answer += key
        return answer
