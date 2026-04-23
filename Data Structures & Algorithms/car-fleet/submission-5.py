class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)
        fleet = 0
        last_time = 0

        for p, s in cars:
            time = (target - p) / s
            if time > last_time:
                fleet += 1
                last_time = time

        return fleet