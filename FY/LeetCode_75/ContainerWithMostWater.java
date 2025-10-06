public class ContainerWithMostWater {
    public int maxArea(int[] height) {
        int ans = 0;
        int l = 0;
        int r = height.length - 1;

        while (l < r) {
            final int minHeight = Math.min(height[l], height[r]);
            ans = Math.max(ans, minHeight * (r - l));
            if (height[l] < height[r])
                ++l;
            else
                --r;
        }

        return ans;
    }

    public static void main(String[] args) {
        ContainerWithMostWater solution = new ContainerWithMostWater();

        // Test case 1
        int[] height1 = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        System.out.println("Max area (Test case 1): " + solution.maxArea(height1)); // Expected: 49

        // Test case 2
        int[] height2 = {1, 1};
        System.out.println("Max area (Test case 2): " + solution.maxArea(height2)); // Expected: 1

        // Test case 3
        int[] height3 = {4, 3, 2, 1, 4};
        System.out.println("Max area (Test case 3): " + solution.maxArea(height3)); // Expected: 16

        // Test case 4
        int[] height4 = {1, 2, 1};
        System.out.println("Max area (Test case 4): " + solution.maxArea(height4)); // Expected: 2
    }
}
