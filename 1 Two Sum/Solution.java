import java.util.HashMap;
import java.util.Arrays;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Create a HashMap to store the visited numbers and their indices
        HashMap<Integer, Integer> visitedValueIndex = new HashMap<>();

        // Iterate through the array
        for (int i = 0; i < nums.length; i++) {
            int difference = target - nums[i];

            // Check if the difference is already in the HashMap
            if (visitedValueIndex.containsKey(difference)) {
                return new int[] { visitedValueIndex.get(difference), i };
            }

            // Store the current number and its index in the HashMap
            visitedValueIndex.put(nums[i], i);
        }

        // Return an empty array if no solution is found (though per the problem statement, one always exists)
        throw new IllegalArgumentException("No two sum solution");
    }

    public static void main(String[] args) {
        Solution solution = new Solution();

        // Example test case
        int[] nums = {2, 7, 11, 15};
        int target = 9;

        int[] result = solution.twoSum(nums, target);
        System.out.println(Arrays.toString(result));
    }
}