import java.util.Stack;

class Solution150 {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();

        for (String token : tokens) {
            switch (token) {
                case "+":
                    stack.push(stack.pop() + stack.pop());
                    break;
                case "-":
                    int b1 = stack.pop();
                    int a1 = stack.pop();
                    stack.push(a1 - b1);
                    break;
                case "*":
                    stack.push(stack.pop() * stack.pop());
                    break;
                case "/":
                    int b2 = stack.pop();
                    int a2 = stack.pop();
                    stack.push(a2 / b2);  // Integer division in Java
                    break;
                default:
                    stack.push(Integer.parseInt(token));
                    break;
            }
        }
        return stack.peek();
    }

    public static void main(String[] args) {
        Solution150 solution = new Solution150();
        String[] token1 = {"2", "1", "+", "3", "*"};  // 9
        String[] token2 = {"4", "13", "5", "/", "+"}; // 6
        String[] token3 = {"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}; // 22
        int result = solution.evalRPN(token3);
        System.out.println(result);
    }
}