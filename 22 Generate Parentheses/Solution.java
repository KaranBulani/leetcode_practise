import java.util.ArrayList;
import java.util.List;

class Solution22 {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        backtrack("", 0, 0, n, res);
        return res;
    }

    private void backtrack(String s, int open, int close, int n, List<String> res) {
        if (open == close && open == n) {
            res.add(s);
            return;
        }
        if (open < n) {
            backtrack(s + "(", open + 1, close, n, res);
        }
        if (close < open) {
            backtrack(s + ")", open, close + 1, n, res);
        }
    }

    public static void main(String[] args) {
        Solution22 solution = new Solution22();
        int n1 = 1;
        int n2 = 2;
        int n3 = 3;
        List<String> result = solution.generateParenthesis(n3);
        System.out.println(result);
    }
}
