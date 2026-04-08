class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # Store the string so helper functions can access it
        self.s = s

        # res will store all valid palindrome partitions
        self.res = []

        # part stores the current partition being built
        self.part = []

        # Start DFS from index 0
        self.dfs(0)
        return self.res

    def dfs(self, i):
        # Base case:
        # If we have reached the end of the string,
        # then the current partition is complete and valid
        if i >= len(self.s):
            self.res.append(self.part.copy())
            return

        # Try every possible substring starting at index i
        # If s[i:j] is a palindrome, we can choose it as one part
        for j in range(i, len(self.s)):
            if self.isPalindrome(i, j):
                # Choose the palindrome substring
                self.part.append(self.s[i:j + 1])

                # Recurse on the remaining suffix
                self.dfs(j + 1)

                # Backtrack:
                # remove the last chosen substring so we can try
                # a different cut for the next possibility
                self.part.pop()

    def isPalindrome(self, l, r):
        # Two-pointer check:
        # a substring is a palindrome if it reads the same
        # from left to right and right to left
        while l < r:
            if self.s[l] != self.s[r]:
                return False
            l += 1
            r -= 1
        return True