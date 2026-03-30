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
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode counter = head;
        int totalNodes = 0;
        while (counter != null)    {
            totalNodes++;
            counter = counter.next;
        }

        ListNode prev = dummy;
        ListNode curr = prev.next;
        while (totalNodes >= k) {
            ListNode groupStart = curr;
            ListNode groupNext = null;

            for (int i = 0; i < k; i++) {
                ListNode temp = curr.next;
                curr.next = groupNext;
                groupNext = curr;
                curr = temp;
            }

            prev.next = groupNext;
            groupStart.next = curr;

            prev = groupStart;
            totalNodes -= k; 
        }

        return dummy.next;
    }
}
