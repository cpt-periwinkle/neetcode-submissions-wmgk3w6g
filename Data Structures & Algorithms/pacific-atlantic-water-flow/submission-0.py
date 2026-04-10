from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        # pac = cells that can reach Pacific
        # atl = cells that can reach Atlantic
        pac = set()
        atl = set()

        def dfs(r, c, visit, prevHeight):
            # Stop if:
            # 1. Out of bounds
            # 2. Already visited in this ocean traversal
            # 3. Current height is smaller than previous height
            #    (because when going backwards from the ocean,
            #     we can only move to same/higher cells)
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visit or
                heights[r][c] < prevHeight
            ):
                return

            # Mark this cell as reachable from this ocean
            visit.add((r, c))

            # Continue exploring neighbors
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # Run DFS from top and bottom borders
        # Top row touches Pacific
        # Bottom row touches Atlantic
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        # Run DFS from left and right borders
        # Left column touches Pacific
        # Right column touches Atlantic
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        # Any cell that appears in both sets can reach both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res