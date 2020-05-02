# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def getAnswer(start, end):
            while start < end: # start has to be less than end. Otherwise you will get TLE.
                mid = start + (end - start)//2
                if not isBadVersion(mid):
                    start = mid + 1
                else:
                    end = mid
            return start
        
        return getAnswer(0, n)
