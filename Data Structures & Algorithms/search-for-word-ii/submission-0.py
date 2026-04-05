# Trie node used to store words character by character
class TrieNode:
    def __init__(self):
        # Maps character -> next TrieNode
        self.children = {}

        # True if a complete word ends at this node
        self.endOfWord = False

    def addWord(self, word):
        # Start from the current node (root when called from findWords)
        curr = self

        # Insert each character into the trie
        for ch in word:
            # If this character path does not exist yet, create it
            if ch not in curr.children:
                curr.children[ch] = TrieNode()

            # Move to the next node
            curr = curr.children[ch]

        # Mark the end of the word
        curr.endOfWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build trie from all words
        root = TrieNode()
        for w in words:
            root.addWord(w)

        # Save board so dfs can access it
        self.board = board

        # Board dimensions
        self.ROWS = len(board)
        self.COLS = len(board[0])

        # Use a set so duplicate words are only added once
        self.res = set()

        # Tracks cells currently in the DFS path
        # This prevents reusing the same cell in one word path
        self.visit = set()

        # Start DFS from every cell in the board
        for r in range(self.ROWS):
            for c in range(self.COLS):
                self.dfs(r, c, root, "")

        # Convert result set to list
        return list(self.res)

    def dfs(self, r, c, node, word):
        # Base cases:
        # 1. Out of bounds
        # 2. Cell already used in current path
        # 3. Current board character is not a valid next trie path
        if (
            r < 0 or c < 0 or
            r >= self.ROWS or c >= self.COLS or
            (r, c) in self.visit or
            self.board[r][c] not in node.children
        ):
            return

        # Mark current cell as visited
        self.visit.add((r, c))

        # Move trie pointer to the child node for current character
        ch = self.board[r][c]
        node = node.children[ch]

        # Add current character to the word we are building
        word += ch

        # If this trie node marks the end of a word,
        # we found a complete word from the list
        if node.endOfWord:
            self.res.add(word)

        # Explore all 4 directions
        self.dfs(r - 1, c, node, word)  # up
        self.dfs(r + 1, c, node, word)  # down
        self.dfs(r, c - 1, node, word)  # left
        self.dfs(r, c + 1, node, word)  # right

        # Backtrack: remove this cell before returning
        self.visit.remove((r, c))