class Solution238a {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;

        // Create arrays for left and right products, initialized to 1
        int[] left = new int[n];
        int[] right = new int[n];
        int[] res = new int[n];

        left[0] = 1;
        right[n - 1] = 1;

        // Fill left array
        for (int i = 1; i < n; i++) {
            left[i] = left[i - 1] * nums[i - 1];
        }

        // Fill right array
        for (int i = n - 2; i >= 0; i--) {
            right[i] = right[i + 1] * nums[i + 1];
        }

        // Calculate result by multiplying left and right arrays
        for (int i = 0; i < n; i++) {
            res[i] = left[i] * right[i];
        }

        return res;
    }

    public static void main(String[] args) {
        Solution238a solution = new Solution238a();
        int[] nums = {1, 2, 3, 4};  // Example input
        int[] result = solution.productExceptSelf(nums);

        // Print the result
        for (int r : result) {
            System.out.print(r + " ");
        }
    }
}
