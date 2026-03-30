class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}      # Hashmap is more versatile as it doesn't depend on alphabets
        res = 0         # solution

        left = 0        # left pointer
        maxf = 0        # max counter
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)   # defaults to 0, adds 1 if existing
            maxf = max(maxf, count[s[right]])           # finds local maximum

            # maxf has the chance of becoming stale. This does not matter.
            # The idea behind this is because we only use this to check for validity.
            # If the max frequency increases, our answer just becomes more valid,
            # as we want it to become as large as possible.
            # If we reduce this max frequency, it reduces the validity condition.
            # It is OVERESTIMATING the frequency, while not losing the actual solution.

            # We don’t decrease max_freq because an overestimate only delays shrinking,
            # and that doesn’t affect the final maximum window size.

            while ((right - left + 1) - maxf > k):        # window size (r - l + 1) - maxf
                count[s[left]] -= 1                        # reduce the count of the character lost as left pointer moves
                left += 1                                  # move left pointer
            res = max(res, right - left + 1)                # Take the max window size

        return res