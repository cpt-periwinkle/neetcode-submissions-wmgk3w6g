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
    public boolean isValidBST(TreeNode root) {
        return validRecursive(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    private boolean validRecursive(TreeNode curr, int min, int max)  {
        if (curr == null)   {
            return true;
        }
        if (curr.val <= min || curr.val >= max)   {
            return false;
        }
        return validRecursive(curr.left, min, curr.val) && validRecursive(curr.right, curr.val, max);
    }
}
