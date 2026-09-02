class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = {}

        
        speed = [b for (a, b) in sorted(zip(position, speed))]
        position = sorted(position)

        for i in range(len(position)-1, -1, -1):
            fleet_idxs = fleets.values()
            vals = [val for lis in fleet_idxs for val in lis]
            if i in vals: continue


            time_of_finish_i = (target - position[i]) / speed[i]
            fleets[time_of_finish_i] = [i]
            
            car_before = i-1
            time_of_finish_cb = (target - position[car_before]) / speed[car_before]
            
            while time_of_finish_cb <= time_of_finish_i and car_before >= 0:
                fleets[time_of_finish_i].append(car_before)

                car_before -= 1
                time_of_finish_cb = (target - position[car_before]) / speed[car_before]

        return len(fleets.keys())