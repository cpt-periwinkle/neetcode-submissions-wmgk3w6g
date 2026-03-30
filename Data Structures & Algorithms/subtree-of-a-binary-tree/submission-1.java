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
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        // Base cases
        if (subRoot == null) {
            return true;  // Empty tree is always a subtree
        }
        if (root == null) {
            return false;  // Can't find subtree in an empty tree
        }
        
        // Check if the trees match from current root
        if (isSameTree(root, subRoot)) {
            return true;
        }
        
        // Recursively check left and right subtrees
        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }
    
    // Helper method to check if two trees are identical
    private boolean isSameTree(TreeNode p, TreeNode q) {
        // If both are null, they're the same
        if (p == null && q == null) {
            return true;
        }
        
        // If one is null and the other isn't, they're different
        if (p == null || q == null) {
            return false;
        }
        
        // Check if values are the same and recursively check subtrees
        return p.val == q.val && 
               isSameTree(p.left, q.left) && 
               isSameTree(p.right, q.right);
    }
}
