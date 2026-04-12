import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # If total cards can't be evenly divided into groups, impossible
        if len(hand) % groupSize != 0:
            return False

        # Count frequency of each card
        count = {}
        for card in hand:
            count[card] = 1 + count.get(card, 0)

        # Min-heap to always start from the smallest available card
        # Intuition: we must always build sequences starting from the smallest number
        # otherwise we risk leaving gaps later
        minH = list(count.keys())
        heapq.heapify(minH)

        # Keep forming groups until all cards are used
        while minH:
            # Always try to start a group from the smallest remaining card
            first = minH[0]

            # Try to build a consecutive group: [first, first+1, ..., first+groupSize-1]
            for i in range(first, first + groupSize):
                # If any required card is missing → cannot form valid group
                if i not in count:
                    return False

                # Use one occurrence of this card
                count[i] -= 1

                # If this card is fully used up
                if count[i] == 0:
                    # Critical intuition:
                    # We must remove cards from heap in sorted order.
                    # If i is not the smallest element, it means we skipped
                    # a smaller card that still has remaining count → invalid
                    if i != minH[0]:
                        return False

                    # Remove the smallest element since it's fully used
                    heapq.heappop(minH)

        # Successfully formed all groups
        return True