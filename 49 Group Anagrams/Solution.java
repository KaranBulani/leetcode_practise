import java.util.*;

class Solution49 {
    public List<List<String>> groupAnagrams(String[] strs) {
        // Using a HashMap where the key is a tuple-like representation of the character counts
        Map<String, List<String>> groupedMap = new HashMap<>();

        for (String word : strs) {
            // Create an array to count character occurrences
            int[] charCount = new int[26];

            for (char c : word.toCharArray()) {
                charCount[c - 'a']++;
            }

            // Convert charCount array into a string as the key
            StringBuilder keyBuilder = new StringBuilder();
            for (int count : charCount) {
                keyBuilder.append(count).append('#'); // Append with a separator to avoid confusion between numbers
            }
            String key = keyBuilder.toString();

            // Add word to the corresponding list in the map
            groupedMap.computeIfAbsent(key, k -> new ArrayList<>()).add(word);
        }

        // Return all the lists of grouped anagrams
        return new ArrayList<>(groupedMap.values());
    }

    public static void main(String[] args) {
        Solution49 solution = new Solution49();
        String[] strs = {"bdddddddddd", "bbbbbbbbbbc"};//{"eat","tea","tan","ate","nat","bat"};//{""};//{"a"};
        List<List<String>> result = solution.groupAnagrams(strs);
        System.out.println(result);
    }
}