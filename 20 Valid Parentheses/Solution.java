import java.util.Stack;
import java.util.HashMap;
import java.util.Map;

class Solution20 {
    public boolean isValid(String s) {
        // Stack to keep track of opening brackets
        Stack<Character> stack = new Stack<>();

        // Map for bracket pairs
        Map<Character, Character> bracketPair = new HashMap<>();
        bracketPair.put('(', ')');
        bracketPair.put('[', ']');
        bracketPair.put('{', '}');

        // Traverse through each character in the string
        for (char bracket : s.toCharArray()) {
            // If it's an opening bracket, push to stack
            if (bracketPair.containsKey(bracket)) {
                stack.push(bracket);
            } else {
                // If stack is empty, it's an invalid string
                if (stack.isEmpty()) {
                    return false;
                }
                // Check if the current closing bracket matches the last opening bracket
                if (bracketPair.get(stack.peek()) == bracket) {
                    stack.pop();
                } else {
                    return false;
                }
            }
        }
        // If the stack is not empty, there are unmatched opening brackets
        return stack.isEmpty();
    }

    public static void main(String[] args) {
        Solution20 solution = new Solution20();
        String s0 = "]";
        String s1 = "()";
        String s2 = "()[]{}";
        String s3 = "(]";
        String s4 = "([])";

        boolean result = solution.isValid(s2);
        System.out.println(result);  // Output for s3
    }
}
