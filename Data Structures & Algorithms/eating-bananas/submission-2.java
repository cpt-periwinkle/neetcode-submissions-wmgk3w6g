class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        Arrays.sort(piles);
        int lb = 1;
        int ub = piles[piles.length - 1];
        int soln = ub;
        
        while (lb <= ub)    {
            int mid = lb + (ub - lb) / 2;
            long totalTime = 0;
            for (int pile : piles)    {
                totalTime += Math.ceil((double) pile / mid);
            }
            if (totalTime <= h)  {
                soln = mid;
                ub = mid - 1;
            } else if (totalTime > h)    {
                lb = mid + 1;
            }
        }
        return soln;
    }
}
