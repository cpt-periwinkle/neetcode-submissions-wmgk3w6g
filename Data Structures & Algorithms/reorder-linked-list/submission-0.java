/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) {
            return;
        }
        Stack<ListNode> stack = new Stack<>();
        ListNode curr = head;
        int count = 0;

        while (curr != null)   {
            stack.push(curr);
            curr = curr.next;
            count++;
        }

        curr = head;
        int countPop = count / 2;
        for (int i = 0; i < countPop; i++)  {
            ListNode temp = curr.next;
            curr.next = stack.pop();
            curr.next.next = temp;
            curr = temp;
        }
        if (curr != null) {
            curr.next = null;
        }
    }
}
