import java.util.ArrayList;
import java.util.List;

class Solution271 {

    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();
        for (String word : strs) {
            encoded.append(word.length()).append('#').append(word);
        }
        return encoded.toString();
    }

    // Decodes a single string to a list of strings.
    public List<String> decode(String str) {
        List<String> decoded = new ArrayList<>();
        int i = 0;

        while (i < str.length()) {
            int j = i;
            // Find the position of the next '#' character
            while (str.charAt(j) != '#') {
                j++;
            }
            // Get the length of the next word
            int length = Integer.parseInt(str.substring(i, j));
            // Extract the word using the length
            decoded.add(str.substring(j + 1, j + 1 + length));
            // Move the index past the current word
            i = j + 1 + length;
        }
        return decoded;
    }

    public static void main(String[] args) {
        Solution271 solution = new Solution271();
        List<String> strs = List.of("we", "say", ":", "yes", "!@#$%^&*()");
        String encoded = solution.encode(strs);
        System.out.println("Encoded: " + encoded);
        List<String> decoded = solution.decode(encoded);
        System.out.println("Decoded: " + decoded);
    }
}