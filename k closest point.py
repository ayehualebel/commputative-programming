class Solution(object):
    import math

    def kClosest(self,points, k):
        self.points=points
        self.k=k

        distances = []
        for point in points:
            x, y = point
            distance = math.sqrt(x ** 2 + y ** 2)
            distances.append((point, distance))

        distances.sort(key=lambda x: x[1])

        return [point[0] for point in distances[:k]]
