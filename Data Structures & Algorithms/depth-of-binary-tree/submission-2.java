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
    public int maxDepth(TreeNode root) {
        if (root == null)   {
            return 0;
        }
        return countRecursive(root);
    }

    private int countRecursive(TreeNode curr)    {
        if (curr == null)   {
            return 0;
        }
        int leftCount = countRecursive(curr.left);
        int rightCount = countRecursive(curr.right);
        return Math.max(leftCount, rightCount) + 1;
    }
}
