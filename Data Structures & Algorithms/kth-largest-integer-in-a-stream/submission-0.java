class KthLargest {
    private PriorityQueue<Integer> heap;
    private int k;

    public KthLargest(int k, int[] nums) {
        this.k = k;
        this.heap = new PriorityQueue<>();
        for (int num : nums)    {
            heap.offer(num);
            if (heap.size() > k)    {
                heap.poll();
            }
        }
    }
    
    public int add(int val) {
        heap.offer(val);
        if (heap.size() > k)    {
            heap.poll();
        }
        return heap.peek();
    }
}
