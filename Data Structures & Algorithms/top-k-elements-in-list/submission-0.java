class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }
        
        Map<Integer, ArrayList<Integer>> bucketMap = new HashMap<>();
        for (int num : frequencyMap.keySet()) {
            int freq = frequencyMap.get(num);
            if (!bucketMap.containsKey(freq)) {
                bucketMap.put(freq, new ArrayList<>());
            }
            bucketMap.get(freq).add(num);
        }
        
        int[] result = new int[k];
        int index = 0;
        for (int freq = nums.length; freq > 0 && index < k; freq--) {
            if (bucketMap.containsKey(freq)) {
                for (int num : bucketMap.get(freq)) {
                    if (index < k) {
                        result[index++] = num;
                    } else {
                        break;
                    }
                }
            }
        }
        
        return result;
    }
}
