class TimeMap {
    Map<String, TreeMap<Integer, String>> timeMap;

    public TimeMap() {
        timeMap = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        if (timeMap.containsKey(key)){
            TreeMap<Integer, String> tp = timeMap.get(key);
            tp.put(timestamp, value);
        } else {
            TreeMap<Integer, String> tp = new TreeMap<>();
            tp.put(timestamp,value);
            timeMap.put(key,tp);
        }
    }
    
    public String get(String key, int timestamp) {
        if (timeMap.containsKey(key))  {
            TreeMap<Integer, String> tp = timeMap.get(key);
            Map.Entry<Integer, String> map = tp.floorEntry(timestamp);
            if (map == null)    {
                return "";
            } else {
                return map.getValue();
            }
                
        } else {
            return "";
        }
    }
}
