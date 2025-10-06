public class IsSubsequence {
    public boolean isSubsequence(String s, String t) {
        if (s.isEmpty()) {
            return true;
        }

        int i = 0;
        for (final char c : t.toCharArray()) {
            if (s.charAt(i) == c && ++i == s.length()) {
                return true;
            }
        }

        return false;
    }

    public static void main(String[] args) {
        IsSubsequence solution = new IsSubsequence();

        // Test case 1
        String s1 = "abc";
        String t1 = "ahbgdc";
        System.out.println("Is \"" + s1 + "\" a subsequence of \"" + t1 + "\": " + solution.isSubsequence(s1, t1)); // Expected: true

        // Test case 2
        String s2 = "axc";
        String t2 = "ahbgdc";
        System.out.println("Is \"" + s2 + "\" a subsequence of \"" + t2 + "\": " + solution.isSubsequence(s2, t2)); // Expected: false

        // Test case 3
        String s3 = "";
        String t3 = "anystring";
        System.out.println("Is \"" + s3 + "\" a subsequence of \"" + t3 + "\": " + solution.isSubsequence(s3, t3)); // Expected: true

        // Test case 4
        String s4 = "ace";
        String t4 = "abcde";
        System.out.println("Is \"" + s4 + "\" a subsequence of \"" + t4 + "\": " + solution.isSubsequence(s4, t4)); // Expected: true
    }
}
