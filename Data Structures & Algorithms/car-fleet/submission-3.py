class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort cars by position
        cars = sorted(zip(position, speed))

        fleets, t = 0, 0
        for i in range(len(cars)):
            new_t = (target-cars[-(i+1)][0])/cars[-(i+1)][1]
            if new_t > t:
                t = new_t
                fleets += 1
        return fleets

