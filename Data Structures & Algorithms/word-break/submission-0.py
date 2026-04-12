class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = True if substring s[i:] can be segmented into words in wordDict
        dp = [False] * (len(s) + 1)

        # Base case: empty string is always valid
        dp[len(s)] = True

        # Traverse string backwards
        for i in range(len(s) - 1, -1, -1):

            # Try every word in dictionary
            for w in wordDict:

                # Check if word fits starting at index i
                # and matches substring
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:

                    # If the rest of the string after this word is valid,
                    # then current position is also valid
                    dp[i] = dp[i + len(w)]

                # If we already found a valid split, stop early
                if dp[i]:
                    break

        # Answer: can the whole string be segmented?
        return dp[0]