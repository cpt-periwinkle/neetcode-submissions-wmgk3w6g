class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        Map<Integer, Integer> speedMap = new HashMap<>();
        Stack<Integer> posStack = new Stack<>();
        int fleetSize = position.length;
        if (fleetSize == 0) {
            return 0;
        }
        for (int i = 0; i < fleetSize; i++)   {
            speedMap.put(position[i], speed[i]);
        }
        Arrays.sort(position);
        for (int i = 0; i < fleetSize; i++)   {
            posStack.push(position[i]);
        }
        float prevTime = -1;
        int fleetCount = 0;
        while (!posStack.isEmpty()) {
            int pos = posStack.pop();
            int dist = target - pos;
            float time = (float) dist / speedMap.get(pos);
            if (time > prevTime)    {
                fleetCount++;
                prevTime = time;
            }
        }
        return fleetCount;
    }
}
