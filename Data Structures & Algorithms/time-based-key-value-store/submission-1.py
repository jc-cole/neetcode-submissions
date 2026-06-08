class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.map:
            self.map[key] = [tuple([timestamp, value])]
        else:
            self.map[key].append(tuple([timestamp, value]))

    def get(self, key: str, timestamp: int) -> str:
        if not (key in self.map):
            return ""

        pairs = self.map[key]
        low = 0
        high = len(pairs) - 1

        closest = ""

        while low <= high:
            mid = (low + high) // 2
            mid_timestamp = pairs[mid][0]
            if mid_timestamp == timestamp:
                return pairs[mid][1]
            elif mid_timestamp > timestamp:
                high = mid - 1
            elif mid_timestamp < timestamp:
                closest = pairs[mid][1]
                low = mid + 1
        
        return closest
        
