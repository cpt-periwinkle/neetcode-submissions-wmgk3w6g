class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] A = nums1;
        int[] B = nums2;
        int total = A.length + B.length;
        int half = (total + 1) / 2;

        if (B.length < A.length)    {
            int[] temp = A;
            A = B;
            B = temp;
        }

        int lb = 0, rb = A.length;

        while (lb <= rb)    {
            int mid = lb + (rb - lb) / 2;
            int value = half - mid;

            int Aleft = mid > 0 ? A[mid - 1] : Integer.MIN_VALUE;
            int Aright = mid < A.length ? A[mid] : Integer.MAX_VALUE;
            int Bleft = value > 0 ? B[value - 1] : Integer.MIN_VALUE;
            int Bright = value < B.length ? B[value] : Integer.MAX_VALUE;

            if (Aleft <= Bright && Bleft <= Aright)  {
                if (total % 2 != 0) {
                    return Math.max(Aleft, Bleft);
                } else {
                    return (Math.max(Aleft, Bleft) + Math.min(Aright, Bright)) / 2.0;
                }
            } else if (Aleft > Bright) {
                rb = mid - 1;
            } else {
                lb = mid + 1;
            }
        }
        return -1;
    }
}
