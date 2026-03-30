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
    private List<List<Integer>> soln = new ArrayList<>();
    public List<List<Integer>> levelOrder(TreeNode root) {
        levelRecursive(root, 0);
        return soln;
    }

    private void levelRecursive(TreeNode curr, int depth)   {
        if (curr == null)   {
            return;
        }

        if (soln.size() == depth)   {
            soln.add(new ArrayList<>());
        }

        soln.get(depth).add(curr.val);
        levelRecursive(curr.left, depth+1);
        levelRecursive(curr.right, depth+1);
    }
}
