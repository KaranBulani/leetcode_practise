import java.util.HashSet;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> numValues = new HashSet<>();

        for (int num : nums) {
            if (numValues.contains(num)) {
                return true;
            }
            numValues.add(num);
        }
        return false;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {1,1,1,3,3,4,3,2,4,2};  // Example input
        System.out.println(solution.containsDuplicate(nums));  // Output: true
    }
}