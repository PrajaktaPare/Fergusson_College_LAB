class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double sum = 0;
        for (int i = 0; i < k; ++i)
            sum += nums[i];
        double ans = sum;

        for (int i = k; i < nums.length; ++i) {
            sum += nums[i] - nums[i - k];
            ans = Math.max(ans, sum);
        }

        return ans / k;
    }
}

public class MaxAvgSubArray {
    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test case 1
        int[] nums1 = {1, 12, -5, -6, 50, 3};
        int k1 = 4;
        System.out.println("Max average for test case 1: " + solution.findMaxAverage(nums1, k1));

        // Test case 2
        int[] nums2 = {5, -10, 20, 7, 8};
        int k2 = 3;
        System.out.println("Max average for test case 2: " + solution.findMaxAverage(nums2, k2));

        // Test case 3
        int[] nums3 = {4, 2, 1, 3, 5};
        int k3 = 2;
        System.out.println("Max average for test case 3: " + solution.findMaxAverage(nums3, k3));

        // Test case 4 (edge case)
        int[] nums4 = {100};
        int k4 = 1;
        System.out.println("Max average for test case 4: " + solution.findMaxAverage(nums4, k4));
    }
}
