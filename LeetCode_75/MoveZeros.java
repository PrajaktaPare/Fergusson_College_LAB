public class MoveZeros {
    public void moveZeroes(int[] nums) {
        int i = 0;
        for (final int num : nums) {
            if (num != 0) {
                nums[i++] = num;
            }
        }

        while (i < nums.length) {
            nums[i++] = 0;
        }
    }

    public static void main(String[] args) {
        MoveZeros solution = new MoveZeros();

        // Test case 1
        int[] nums1 = {0, 1, 0, 3, 12};
        solution.moveZeroes(nums1);
        System.out.print("After moving zeroes (Test case 1): ");
        for (int num : nums1) {
            System.out.print(num + " ");
        }
        System.out.println();

        // Test case 2
        int[] nums2 = {0, 0, 1};
        solution.moveZeroes(nums2);
        System.out.print("After moving zeroes (Test case 2): ");
        for (int num : nums2) {
            System.out.print(num + " ");
        }
        System.out.println();

        // Test case 3
        int[] nums3 = {4, 2, 4, 0, 0, 3, 0, 5, 1, 0};
        solution.moveZeroes(nums3);
        System.out.print("After moving zeroes (Test case 3): ");
        for (int num : nums3) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}
