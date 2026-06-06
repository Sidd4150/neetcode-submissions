class TimeMap:

    def __init__(self):
        self.Main = defaultdict(list)
        self.times = defaultdict(str)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.Main[key].append(timestamp)
        self.times[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.Main:
            check = self.Main[key]
            for time in check[::-1]:
                if time <= timestamp:
                    return self.times[time]

        return ""

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)