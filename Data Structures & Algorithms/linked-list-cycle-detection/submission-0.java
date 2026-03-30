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
    public boolean hasCycle(ListNode head) {
        if (head == null || head.next == null)  {
            return false;
        }
        ListNode fp = head;
        ListNode sp = head;
        while (sp != null && sp.next != null)   {
            fp = fp.next;
            sp = sp.next.next;
            if (sp == fp)    {
                return true;
            }
        }
        return false;
    }
}
