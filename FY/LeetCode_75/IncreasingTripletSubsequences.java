public class IncreasingTripletSubsequences {
    public boolean increasingTriplet(int[] nums) {
        int first = Integer.MAX_VALUE;
        int second = Integer.MAX_VALUE;

        for (final int num : nums) {
            if (num <= first) {
                first = num;
            } else if (num <= second) { // first < num <= second
                second = num;
            } else { // first < second < num (third)
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        IncreasingTripletSubsequences solution = new IncreasingTripletSubsequences();

        // Test cases
        int[] nums1 = {1, 2, 3, 4, 5}; // Expected: true
        int[] nums2 = {5, 4, 3, 2, 1}; // Expected: false
        int[] nums3 = {2, 1, 5, 0, 4, 6}; // Expected: true

        System.out.println("Test Case 1: " + solution.increasingTriplet(nums1)); // Output: true
        System.out.println("Test Case 2: " + solution.increasingTriplet(nums2)); // Output: false
        System.out.println("Test Case 3: " + solution.increasingTriplet(nums3)); // Output: true
    }
}
