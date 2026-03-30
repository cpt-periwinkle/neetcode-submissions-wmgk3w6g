class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        s_dict = {}
        t_dict = {}
        for index in range(len(s)):
            s_dict[s[index]] = 1 + s_dict.get(s[index], 0)
            t_dict[t[index]] = 1 + t_dict.get(t[index], 0)

        return s_dict == t_dict
