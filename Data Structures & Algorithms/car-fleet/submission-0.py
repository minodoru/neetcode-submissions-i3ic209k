class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_pairs = sorted(zip(position, speed))
        position = [x[0] for x in sorted_pairs]
        speed = [x[1] for x in sorted_pairs]
        if not len(position):
            return 0
        fleets, t = 0, 0
        for i in range(len(position)):
            new_t = (target-position[-(i+1)])/speed[-(i+1)]
            print(i, position[-(i+1)], speed[-(i+1)], new_t, t)
            if new_t > t:
                t = new_t
                fleets += 1
                print("added fleet, total ", fleets)
        return fleets

