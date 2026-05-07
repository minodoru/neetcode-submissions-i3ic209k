class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort cars by position
        sorted_pairs = sorted(zip(position, speed))
        position = [x[0] for x in sorted_pairs]
        speed = [x[1] for x in sorted_pairs]

        fleets, t = 0, 0
        for i in range(len(position)):
            new_t = (target-position[-(i+1)])/speed[-(i+1)]
            if new_t > t:
                t = new_t
                fleets += 1
        return fleets

