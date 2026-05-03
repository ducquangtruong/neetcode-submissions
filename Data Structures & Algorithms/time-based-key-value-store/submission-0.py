class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""

        res, arr = "", self.keyStore[key]
        start, end = 0, len(arr) - 1
        while start <= end:
            mid = (start + end) // 2
            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                start = mid + 1
            else:
                end = mid - 1

        return res
