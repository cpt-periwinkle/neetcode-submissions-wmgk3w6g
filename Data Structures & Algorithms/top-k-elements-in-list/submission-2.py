class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}  
        # map each number → its frequency

        freq = [[] for i in range(len(nums) + 1)]  
        # bucket array where index = frequency,
        # and value = list of numbers with that frequency

        # Step 1: Count frequencies
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Step 2: Place numbers into buckets based on frequency
        for num, value in count.items():
            freq[value].append(num)

        res = []

        # Step 3: Iterate from highest frequency to lowest
        # NOTE: The list freq is longer than the list nums, because we added + 1 to match with freq above
        #       We must keep this in mind and start from - 1 freq so it matches the real length
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)  # collect most frequent elements first

                # Stop once we have k elements
                if len(res) == k:
                    return res