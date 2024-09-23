import java.util.HashMap;

class Solution242b {
    // Merge function to merge two sorted subarrays
    public void merge(char[] arr, int start, int mid, int end) {
        char[] left = new char[mid - start + 1];
        char[] right = new char[end - mid];

        // Fill left and right arrays
        for (int i = 0; i < left.length; i++) {
            left[i] = arr[start + i];
        }
        for (int i = 0; i < right.length; i++) {
            right[i] = arr[mid + 1 + i];
        }

        int l = 0, r = 0, k = start;

        // Merge the arrays back into arr
        while (l < left.length && r < right.length) {
            if (left[l] <= right[r]) {
                arr[k] = left[l];
                l++;
            } else {
                arr[k] = right[r];
                r++;
            }
            k++;
        }

        // Copy remaining elements if any
        while (l < left.length) {
            arr[k] = left[l];
            l++;
            k++;
        }
        while (r < right.length) {
            arr[k] = right[r];
            r++;
            k++;
        }
    }

    // Recursive merge sort function
    public void mergeSort(char[] arr, int start, int end) {
        if (start < end) {
            int mid = (start + end) / 2;

            mergeSort(arr, start, mid);
            mergeSort(arr, mid + 1, end);
            merge(arr, start, mid, end);
        }
    }

    // isAnagram function using merge sort
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        char[] sArr = s.toCharArray();
        char[] tArr = t.toCharArray();

        mergeSort(sArr, 0, sArr.length - 1);
        mergeSort(tArr, 0, tArr.length - 1);

        // Check if both sorted arrays are equal
        for (int i = 0; i < sArr.length; i++) {
            if (sArr[i] != tArr[i]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution242b solution = new Solution242b();
        String s = "anagram"; // "rat"
        String t = "nagaram"; // "car"
        boolean result = solution.isAnagram(s, t);
        System.out.println(result);
    }
}