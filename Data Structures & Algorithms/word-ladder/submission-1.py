class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        pat_dict = defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pat = word[:i] + "*" + word[i + 1:]
                pat_dict[pat].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for j in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res
                
                for i in range(len(word)):
                    pat = word[:i] + "*" + word[i + 1:]

                    for child in pat_dict[pat]:
                        if child not in visited:
                            visited.add(child)
                            q.append(child)   
            res += 1
        
        return 0