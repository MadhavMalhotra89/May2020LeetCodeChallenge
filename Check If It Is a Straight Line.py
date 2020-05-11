class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if not coordinates:
            return False
        direction = 0
        for i in range(1, len(coordinates)):
            top = (coordinates[i][1] - coordinates[i-1][1])
            bottom  = (coordinates[i][0] - coordinates[i-1][0])
            if bottom == 0:
                return False
            slope = top // bottom
            if direction == 0:
                direction = slope
            else:
                if direction != slope:
                    return False
        return True
