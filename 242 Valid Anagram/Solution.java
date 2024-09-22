import java.util.HashMap;

class Solution242a {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> s_count = new HashMap<>();
        for (char c : s.toCharArray()) {
            s_count.put(c, s_count.getOrDefault(c, 0) + 1);
        }

        HashMap<Character, Integer> t_count = new HashMap<>();
        for (char c : t.toCharArray()) {
            t_count.put(c, t_count.getOrDefault(c, 0) + 1);
        }

        for (char key : s_count.keySet()) {
            if (!s_count.get(key).equals(t_count.getOrDefault(key, 0))) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution242a solution = new Solution242a();
        String s = "anagram"; // "rat"
        String t = "nagaram"; // "car"
        boolean result = solution.isAnagram(s, t);
        System.out.println(result);
    }
}