class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        soln_map = dict()
        for str in strs:
            count = [0] * 26
            for ltr in str:
                count[ord(ltr) - ord('a')] += 1

            key = tuple(count)
            if key in soln_map:
                soln_map[key].append(str)
            else:
                soln_map[key] = [str]

        return list(soln_map.values())
        
        