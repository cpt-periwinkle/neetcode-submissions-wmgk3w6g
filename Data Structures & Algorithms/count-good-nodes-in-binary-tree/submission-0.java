/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public int goodNodes(TreeNode root) {
        return goodRecursive(root, Integer.MIN_VALUE);
    }

    private int goodRecursive(TreeNode curr, int maxCount)    {
        if (curr == null)   {
            return 0;
        }
        int count = (curr.val >= maxCount) ? 1 : 0;
        int newMax = Math.max(maxCount, curr.val);

        count += goodRecursive(curr.left, newMax);
        count += goodRecursive(curr.right, newMax);
        return count;
    }
}
