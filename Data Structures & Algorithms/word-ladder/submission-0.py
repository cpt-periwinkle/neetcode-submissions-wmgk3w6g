import collections
from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # If endWord is not in dictionary, no transformation is possible
        if endWord not in wordList:
            return 0

        # Map pattern -> list of words that match it
        # Example: "*ot" -> ["hot", "dot", "lot"]
        nei = collections.defaultdict(list)

        # Include beginWord so we can build patterns from it too
        wordList.append(beginWord)

        # Build pattern dictionary
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        # BFS setup
        visit = set([beginWord])  # avoid revisiting words
        q = deque([beginWord])    # start from beginWord
        res = 1                   # transformation length (level count)

        # Standard BFS
        while q:
            # Process one level at a time
            for i in range(len(q)):
                word = q.popleft()

                # If we reached the target, return number of steps
                if word == endWord:
                    return res

                # Generate all patterns for current word
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]

                    # Explore all neighbors sharing this pattern
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)

            # After processing one level, increment steps
            res += 1

        # If we never reached endWord
        return 0