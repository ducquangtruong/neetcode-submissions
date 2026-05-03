class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [[position[i], speed[i]] for i in range(n)]
        cars.sort(reverse = True)
        stack = []

        for car in cars:
            stack.append((target - car[0]) / car[1])
            while len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)