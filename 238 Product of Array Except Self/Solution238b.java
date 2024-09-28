class Solution238b {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        res[0] = 1;

        // Calculate the left product
        for (int i = 1; i < nums.length; i++) {
            res[i] = res[i - 1] * nums[i - 1];
        }

        // Calculate the right product and update the result array
        int right = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            res[i] = res[i] * right;
            right = right * nums[i];
        }

        return res;
    }

    public static void main(String[] args) {
        Solution238b solution = new Solution238b();
        int[] nums = {1, 2, 3, 4};  // Example input
        int[] nums1 = {-1, 1, 0, -3, 3};
        int[] result = solution.productExceptSelf(nums1);

        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
