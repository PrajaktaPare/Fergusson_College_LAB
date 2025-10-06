import java.util.*;

class Solution {
    public int longestOnes(int[] nums, int k) {
        int ans = 0;

        // Sliding window approach
        for (int l = 0, r = 0; r < nums.length; ++r) {
            if (nums[r] == 0)
                --k;
            while (k < 0)
                if (nums[l++] == 0)
                    ++k;
            ans = Math.max(ans, r - l + 1);
        }

        return ans;
    }
}

public class MaxConsecutiveOnes {
    public static void main(String[] args) {
        Solution solution = new Solution();

        // Test case 1
        int[] nums1 = {1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0};
        int k1 = 2;
        System.out.println("Longest subarray of ones with at most " + k1 + " zeroes flipped: " 
                           + solution.longestOnes(nums1, k1));

        // Test case 2
        int[] nums2 = {0, 0, 1, 1, 1, 0, 0};
        int k2 = 0;
        System.out.println("Longest subarray of ones with at most " + k2 + " zeroes flipped: " 
                           + solution.longestOnes(nums2, k2));

        // Test case 3
        int[] nums3 = {0, 0, 0, 1};
        int k3 = 4;
        System.out.println("Longest subarray of ones with at most " + k3 + " zeroes flipped: " 
                           + solution.longestOnes(nums3, k3));
    }
}
