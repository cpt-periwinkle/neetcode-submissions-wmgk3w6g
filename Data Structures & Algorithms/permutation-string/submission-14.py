class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        # frequency of each character needed from s1
        s1_freq = {}
        for char in s1:
            s1_freq[char] = 1 + s1_freq.get(char, 0)

        # number of unique chars we need to satisfy vs currently have
        need = len(s1_freq)
        have = 0

        # frequency of each character in the current window
        window_freq = {}
        left = 0

        for right in range(len(s2)):
            right_char = s2[right]
            left_char = s2[left]

            # expand window by adding right_char
            window_freq[right_char] = 1 + window_freq.get(right_char, 0)

            if right_char in s1_freq:
                if window_freq[right_char] == s1_freq[right_char]:
                    have += 1        # just hit exact count → have
                elif window_freq[right_char] == s1_freq[right_char] + 1:
                    have -= 1        # exceeded required count → lost satisfaction

            # shrink from left if window is too big
            if right - left + 1 > len(s1):
                if left_char in s1_freq:
                    if window_freq[left_char] == s1_freq[left_char]:
                        have -= 1    # was exact, removing breaks what we have
                    elif window_freq[left_char] == s1_freq[left_char] + 1:
                        have += 1    # was one over, removing restores have
                window_freq[left_char] -= 1
                left += 1

            if have == need:
                return True

        return False