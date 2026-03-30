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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        
        ListNode runner = dummy;
        ListNode walker = dummy;

        for(int i = 0; i <= n; i++)  {
            runner = runner.next;
        }

        while (runner != null)  {
            walker = walker.next;
            runner = runner.next;
        }
        
        walker.next = walker.next.next;
        return dummy.next;
    }
}
