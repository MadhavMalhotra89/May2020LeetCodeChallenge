class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = []
        i = 0
        j = 0
        start = 0
        end = 1
        while  i < len(A) and j < len(B):
            aoverlaps_b = A[i][start] >= B[j][start] and A[i][start] <= B[j][end]
            boverlaps_a = B[j][start] >= A[i][start] and B[j][start] <= A[i][end]
            if aoverlaps_b or boverlaps_a:
                result.append([max(A[i][start],B[j][start]), min(A[i][end],B[j][end])])
            if A[i][end] < B[j][end]:
                i+=1
            else:
                j+=1
        return result
