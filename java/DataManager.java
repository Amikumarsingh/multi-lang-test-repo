// Java class with various errors

import java.util.ArrayList;
import java.util.List;
// Missing import: java.util.HashMap

public class DataManager {
    private List<String> items;
    
    public DataManager() {
        this.items = new ArrayList<>();
    }
    
    // Missing return type - syntax error
    public addItem(String item) {
        items.add(item);
    }
    
    public String getItem(int index) {
        if (index >= 0 && index < items.size()) {
            return items.get(index);
        }
        return null;
    }
    
    public int getCount() {
        return items.size();
    }
    
    // Type error: incompatible types
    public String concatenateItems() {
        int result = "";  // Should be String
        for (String item : items) {
            result += item + " ";
        }
        return result;
    }
    
    // Missing import for HashMap
    public HashMap<String, Integer> getItemCounts() {
        HashMap<String, Integer> counts = new HashMap<>();
        for (String item : items) {
            counts.put(item, counts.getOrDefault(item, 0) + 1);
        }
        return counts;
    }
    
    // Syntax error: missing semicolon
    public void clearItems() {
        items.clear()
    }
    
    // Logic error: wrong condition
    public boolean isEmpty() {
        return items.size() > 0;  // Should be == 0 or use items.isEmpty()
    }
}
