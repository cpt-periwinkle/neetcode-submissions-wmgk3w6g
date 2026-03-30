class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Rename for convenience
        A, B = nums1, nums2

        # Total number of elements and midpoint
        total = len(nums1) + len(nums2)
        half = total // 2

        # Always binary search on the smaller array
        # This ensures O(log(min(n, m))) complexity
        if len(B) < len(A):
            A, B = B, A

        # Binary search boundaries on A
        l, r = 0, len(A) - 1

        while True:
            # Partition index for A
            i = (l + r) // 2

            # Partition index for B
            # Ensures left partition has exactly 'half' elements total
            j = half - i - 2

            # Elements around the partition:
            # Aleft | Aright
            # Bleft | Bright

            # Handle out-of-bounds using ±infinity
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # ---- Check if partition is valid ----
            # All elements in left partition ≤ all elements in right partition
            if Aleft <= Bright and Bleft <= Aright:

                # If total is odd → median is the first element in right partition
                if total % 2:
                    return min(Aright, Bright)

                # If total is even → median is average of middle two values
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # ---- Adjust binary search ----

            # If Aleft is too big, we went too far right in A
            # → move left
            elif Aleft > Bright:
                r = i - 1

            # Otherwise, we are too far left in A
            # → move right
            else:
                l = i + 1