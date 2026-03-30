class TimeMap:

    def __init__(self):
        # Dictionary mapping:
        # key → list of [value, timestamp] pairs
        # Each list is maintained in increasing order of timestamp
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If key does not exist, initialize an empty list
        if key not in self.store:
            self.store[key] = []

        # Append the (value, timestamp) pair
        # Assumption: timestamps are strictly increasing for each key
        # → so list remains sorted by timestamp
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Default result if no valid timestamp is found
        res = ""

        # Get list of values for this key
        # If key doesn't exist, use empty list
        values = self.store.get(key, [])

        # Binary search to find the latest timestamp ≤ given timestamp
        left = 0
        right = len(values) - 1

        while left <= right:
            mid = left + (right - left) // 2

            # If current timestamp is valid (≤ query timestamp),
            # this could be a candidate answer
            if values[mid][1] <= timestamp:
                res = values[mid][0]   # store value as potential result

                # Try to find a closer (more recent) timestamp on the right
                left = mid + 1
            else:
                # Current timestamp is too large → search left half
                right = mid - 1

        # Return the best match found (or "" if none exists)
        return res