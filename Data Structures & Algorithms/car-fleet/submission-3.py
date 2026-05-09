class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(position[i], speed[i]) for i in range(len(position))])
        # Store the time taken for each car
        stk = []

        for car in cars:
            time = (target - car[0]) / car[1]
            while stk and time >= stk[-1]:
                stk.pop()
            
            stk.append(time)
        
        return len(stk)