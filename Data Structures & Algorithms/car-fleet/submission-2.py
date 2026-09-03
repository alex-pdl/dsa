class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        
        speed = [b for (a, b) in sorted(zip(position, speed))]
        position = sorted(position)

        for i in range(len(position)-1, -1, -1):
            time_of_finish = (target - position[i]) / speed[i]
            
            if not bool(fleets):
                fleets.append(time_of_finish)
                continue

            if time_of_finish > fleets[-1]:
                fleets.append(time_of_finish)
            else: 
                pass
            
        #print(fleets)

        return len(fleets)