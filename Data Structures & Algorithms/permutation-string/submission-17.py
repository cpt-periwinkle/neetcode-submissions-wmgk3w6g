class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}

        for ch in s1:
            s1_freq[ch] = 1 + s1_freq.get(ch, 0)

        need = len(s1_freq)
        have = 0

        win_freq = {}
        left = 0
        for right in range(len(s2)):
            right_ch = s2[right]
            left_ch = s2[left]

            win_freq[right_ch] = 1 + win_freq.get(right_ch, 0)

            if right_ch in s1_freq:
                if s1_freq[right_ch] == win_freq[right_ch]:
                    have += 1
                elif s1_freq[right_ch] + 1 == win_freq[right_ch]:
                    have -= 1
            
            if right - left + 1 > len(s1):
                if left_ch in s1_freq:
                    if s1_freq[left_ch] == win_freq[left_ch]:
                        have -= 1
                    elif s1_freq[left_ch] + 1 == win_freq[left_ch]:
                        have += 1
                left += 1
                win_freq[left_ch] -= 1

            if have == need:
                return True
        
        return False