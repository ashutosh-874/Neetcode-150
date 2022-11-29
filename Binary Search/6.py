# https://leetcode.com/problems/time-based-key-value-store/


class TimeMap:

    def __init__(self):
        self.hash = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash[key] = self.hash.get(key, []) + [(timestamp, value)]
        # print(self.hash)

    def get(self, key: str, timestamp: int) -> str:
        value_lst = self.hash.get(key)
        if value_lst is None: return ""
        else:
            res = ""
            left, right = 0, len(value_lst) - 1
            while left <= right:
                mid = (left + right) // 2
                if value_lst[mid][0] == timestamp:
                    return value_lst[mid][1]
                elif value_lst[mid][0] > timestamp:
                    right = mid - 1
                else:
                    res = value_lst[mid][1]
                    left = mid + 1

            return res

timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))
print(timeMap.get("foo", 3))
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))
print(timeMap.get("foo", 5))
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)