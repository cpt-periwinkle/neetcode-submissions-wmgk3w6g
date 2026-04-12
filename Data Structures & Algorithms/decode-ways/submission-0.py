class Solution:
    def numDecodings(self, s: str) -> int:
        # memo[i] = number of ways to decode substring s[i:]
        # Base case: empty string has 1 valid decoding
        memo = {len(s): 1}
        
        def dfs(i):
            # If already computed, reuse result (avoid recomputation)
            if i in memo:
                return memo[i]

            # If we reach the end, this path formed a valid decoding
            if i == len(s):
                return 1

            # A substring starting with '0' cannot be decoded
            if s[i] == "0":
                return 0
            
            # Choice 1: take one digit (always valid if not '0')
            # Count all ways from the rest of the string
            res = dfs(i + 1)

            # Choice 2: take two digits (only if valid 10–26)
            # If valid, add all ways from skipping two positions
            if i < len(s) - 1:
                if (s[i] == "1") or (s[i] == "2" and s[i + 1] < "7"):
                    res += dfs(i + 2)

            # Store result for this index
            memo[i] = res

            # res = total number of valid decoding paths from index i
            return res

        # Start decoding from index 0
        return dfs(0)