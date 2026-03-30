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
    private int count;
    private int ans;
    public int kthSmallest(TreeNode root, int k) {
        count = k;
        inOrderTraversal(root);
        return ans;
    }

    private void inOrderTraversal(TreeNode curr)    {
        if (curr == null || count == 0)   {
            return;
        }
        inOrderTraversal(curr.left);
        count--;
        if (count == 0) {
            ans = curr.val;
            return;
        }
        inOrderTraversal(curr.right);
    }
}
