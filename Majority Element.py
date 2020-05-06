class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length = len(nums)
        maj = length//2
        obj = {}
        for num in nums:
            obj[num] = obj.get(num, 0) + 1
        for key in obj:
            if obj[key] > maj:
                return key
