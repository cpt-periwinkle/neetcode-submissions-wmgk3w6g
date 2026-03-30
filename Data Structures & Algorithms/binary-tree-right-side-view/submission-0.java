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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> rightView = new ArrayList<>();
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty())    {
            int levelSize = q.size();
            TreeNode right = null;

            for (int i = 0; i < levelSize; i++) {
                TreeNode node = q.poll();
                if (node != null)   {
                    right = node;
                    q.offer(node.left);
                    q.offer(node.right);
                }
            }

            if (right != null)  {
                rightView.add(right.val);
            }
        }
        return rightView;
    }
}
