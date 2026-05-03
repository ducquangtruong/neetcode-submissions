class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def calculateTime(car):
            return (target - car[0]) / car[1]

        n = len(position)
        cars = [[position[i], speed[i]] for i in range(n)]
        cars.sort(reverse = True)
        stack = []

        for car in cars:
            stack.append(car)
            while len(stack) > 1 and calculateTime(stack[-1]) <= calculateTime(stack[-2]):
                stack.pop()
        
        return len(stack)