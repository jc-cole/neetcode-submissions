class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [
            [position[i], speed[i]] for i in range(len(position))
        ]

        cars.sort(key=lambda lis : lis[0], reverse=True)

        times = []

        for pos, spd in cars:
            arrival_time = (target - pos) / spd
            
            if not times or arrival_time > times[-1]:
                times.append(arrival_time)

        return len(times)