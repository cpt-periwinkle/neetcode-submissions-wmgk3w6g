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
    public TreeNode invertTree(TreeNode root) {
        if (root == null)   {
            return null;
        }
        return invertRecursive(root);
    }

    private TreeNode invertRecursive(TreeNode curr) {
        if (curr != null)   {
            TreeNode val1 = invertRecursive(curr.left);
            TreeNode val2 = invertRecursive(curr.right);
            curr.left = val2;
            curr.right = val1;
        }
        return curr;
    }
}
