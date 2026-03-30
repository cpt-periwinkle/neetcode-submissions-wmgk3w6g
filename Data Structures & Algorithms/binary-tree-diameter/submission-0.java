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
    private int diameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        diameterRecursive(root);
        return diameter;
    }

    private int diameterRecursive(TreeNode curr)  {
        if (curr == null)  {
            return 0;
        }
        int leftCount = diameterRecursive(curr.left);
        int rightCount = diameterRecursive(curr.right);
        diameter = Math.max(diameter, leftCount + rightCount);
        return Math.max(leftCount, rightCount) + 1;
    }
}
