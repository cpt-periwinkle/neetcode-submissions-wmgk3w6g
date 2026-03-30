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
    private boolean balanced = true;

    public boolean isBalanced(TreeNode root) {
        nodeCount(root);
        return balanced;
    }

    private int nodeCount(TreeNode curr) {
        if (curr == null)   {
            return 0;
        }
        int leftCount = nodeCount(curr.left);
        int rightCount = nodeCount(curr.right);
        if (Math.abs(leftCount - rightCount) > 1)  {
            balanced = false;
        }
        return Math.max(leftCount, rightCount) + 1;
    }
}
