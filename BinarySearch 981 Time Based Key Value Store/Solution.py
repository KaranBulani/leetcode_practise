'''
Time Complexity:  O(logn)              (for lookup)
Space Complexity: O(n)                 (for store dictionary)
'''

from collections import defaultdict

class TimeMap:
    def __init__(self):
        # Dictionary where each key maps to a list of [value, timestamp] pairs.
        # Example: store["foo"] = [["bar", 1], ["bar2", 4]]
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Stores the key-value pair along with its timestamp.
        Since timestamps are strictly increasing, we can just append.
        """
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        """
        Retrieves the value for the given key at the largest timestamp <= given timestamp.
        If no such timestamp exists, returns "".
        Uses binary search to achieve O(log n) lookup time.
        """
        res = ""  # Default return value if no valid timestamp is found
        # Get the list of [value, timestamp] pairs for the key
        values = self.store.get(key, [])

        L, R = 0, len(values) - 1  # Binary search boundaries
        while L <= R:
            M = (L + R) // 2  # Middle index

            if values[M][1] == timestamp:
                # Exact timestamp match found → return its value immediately
                res = values[M][0]
                return res
            elif values[M][1] < timestamp:
                # This timestamp is valid but might not be the closest
                # Save its value as a potential answer and search right for a closer one
                res = values[M][0]
                L = M + 1
            else:
                # Timestamp is too big → search left for a smaller one
                R = M - 1

        return res  # Return the closest valid value found, or "" if none


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

if __name__ == "__main__":
    timeMap = TimeMap()

    # Example from the question
    timeMap.set("foo", "bar", 1)
    print(timeMap.get("foo", 1))  # Expected: "bar"
    print(timeMap.get("foo", 3))  # Expected: "bar"
    timeMap.set("foo", "bar2", 4)
    print(timeMap.get("foo", 4))  # Expected: "bar2"
    print(timeMap.get("foo", 5))  # Expected: "bar2"

    print("----- Additional Edge Cases -----")

    # Case 1: Key not present at all
    print(timeMap.get("baz", 1))  # Expected: ""

    # Case 2: Timestamp earlier than any set timestamp
    timeMap.set("early", "start", 5)
    print(timeMap.get("early", 1))  # Expected: ""

    # Case 3: Multiple values for same key, querying exact timestamps
    timeMap.set("multi", "v1", 1)
    timeMap.set("multi", "v2", 2)
    timeMap.set("multi", "v3", 3)
    print(timeMap.get("multi", 1))  # Expected: "v1"
    print(timeMap.get("multi", 2))  # Expected: "v2"
    print(timeMap.get("multi", 3))  # Expected: "v3"

    # Case 4: Query between timestamps
    print(timeMap.get("multi", 4))  # Expected: "v3"

    # Case 5: Large timestamp jump
    timeMap.set("jump", "first", 10)
    timeMap.set("jump", "second", 1000)
    print(timeMap.get("jump", 500))  # Expected: "first"
    print(timeMap.get("jump", 1000))  # Expected: "second"
    print(timeMap.get("jump", 1500))  # Expected: "second"

    # Case 6: Multiple keys mixed
    timeMap.set("a", "x", 1)
    timeMap.set("b", "y", 2)
    print(timeMap.get("a", 1))  # Expected: "x"
    print(timeMap.get("b", 1))  # Expected: ""
    print(timeMap.get("b", 2))  # Expected: "y"