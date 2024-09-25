import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class Solution347 {
    public int[] topKFrequent(int[] nums, int k) {
        // Step 1: Create a HashMap to count the frequency of each element
        HashMap<Integer, Integer> countMap = new HashMap<>();
        for (int num : nums) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }

        // Step 2: Create a list of buckets, where the index represents the frequency
        List<Integer>[] bucket = new ArrayList[nums.length + 1];
        for (int i = 0; i < bucket.length; i++) {
            bucket[i] = new ArrayList<>();
        }

        // Step 3: Fill the bucket with elements based on their frequency
        for (int key : countMap.keySet()) {
            int freq = countMap.get(key);
            bucket[freq].add(key);
        }

        // Step 4: Extract the top K frequent elements
        List<Integer> result = new ArrayList<>();
        for (int i = bucket.length - 1; i >= 0 && result.size() < k; i--) {
            for (int num : bucket[i]) {
                result.add(num);
                if (result.size() == k) {
                    break;
                }
            }
        }

        // Convert the result list to an array and return it
        int[] topK = new int[k];
        for (int i = 0; i < k; i++) {
            topK[i] = result.get(i);
        }
        return topK;
    }

    public static void main(String[] args) {
        Solution347 solution = new Solution347();
        int[] nums = {1, 1, 1, 2, 2, 2, 3, 3}; // {1}
        int k = 2; // 1
        int[] result = solution.topKFrequent(nums, k);
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}
