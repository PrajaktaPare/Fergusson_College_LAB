public class StringCompression {
    public int compress(char[] chars) {
        int writeIndex = 0; 
        int length = chars.length;

        for (int start = 0; start < length;) {
            int end = start + 1;

            // Find the range of repeated characters
            while (end < length && chars[end] == chars[start]) {
                end++;
            }

            // Write the character
            chars[writeIndex++] = chars[start];

            // Write the count if greater than 1
            if (end - start > 1) {
                String count = String.valueOf(end - start);
                for (char c : count.toCharArray()) {
                    chars[writeIndex++] = c;
                }
            }

            // Move to the next character group
            start = end;
        }

        return writeIndex;
    }

    public static void main(String[] args) {
        StringCompression solution = new StringCompression();

        // Test case 1
        char[] chars1 = {'a', 'a', 'b', 'b', 'c', 'c', 'c'};
        int length1 = solution.compress(chars1);
        System.out.print("Compressed chars1: ");
        for (int i = 0; i < length1; i++) {
            System.out.print(chars1[i]);
        }
        System.out.println(" | Length: " + length1);

        // Test case 2
        char[] chars2 = {'a'};
        int length2 = solution.compress(chars2);
        System.out.print("Compressed chars2: ");
        for (int i = 0; i < length2; i++) {
            System.out.print(chars2[i]);
        }
        System.out.println(" | Length: " + length2);

        // Test case 3
        char[] chars3 = {'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd'};
        int length3 = solution.compress(chars3);
        System.out.print("Compressed chars3: ");
        for (int i = 0; i < length3; i++) {
            System.out.print(chars3[i]);
        }
        System.out.println(" | Length: " + length3);
    }
}
