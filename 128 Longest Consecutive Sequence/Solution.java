import java.util.HashSet;

class Solution128 {
    public int longestConsecutive(int[] nums) {
        // Step 1: Create a set to hold the unique numbers from the array
        HashSet<Integer> numsSet = new HashSet<>();
        for (int num : nums) {
            numsSet.add(num);
        }

        int res = 0; // Result to store the longest streak

        // Step 2: Loop through the nums array
        for (int num : nums) {
            // Check if it's the start of a sequence (num - 1 doesn't exist in the set)
            if (!numsSet.contains(num - 1)) {
                int longest = 1; // Start of a new sequence
                int currentNum = num;

                // Step 3: Check how long the consecutive sequence is
                while (numsSet.contains(currentNum + longest)) {
                    longest++;
                }

                // Step 4: Update the result with the longest sequence found so far
                res = Math.max(res, longest);
            }
        }

        return res; // Return the longest consecutive sequence
    }

    public static void main(String[] args) {
        Solution128 solution = new Solution128();
        int[] nums = {100, 4, 200, 1, 3, 2};
        int[] nums1 = {0, 3, 7, 2, 5, 8, 4, 6, 0, 1};

        // Testing the function
        int result = solution.longestConsecutive(nums1);
        System.out.println(result);  // Output should be 9 for nums1
    }
}
