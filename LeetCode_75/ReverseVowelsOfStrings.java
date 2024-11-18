import java.util.HashSet;
import java.util.Set;

class ReverseVowelsOfString {
    public String reverseVowels(String s) {
        Set<Character> vowels = new HashSet<>();
        for (char c : "aeiouAEIOU".toCharArray()) {
            vowels.add(c);
        }
        char[] chars = s.toCharArray();
        int left = 0, right = chars.length - 1;
        while (left < right) {
            while (left < right && !vowels.contains(chars[left])) {
                left++;
            }
            while (left < right && !vowels.contains(chars[right])) {
                right--;
            }

            char temp = chars[left];
            chars[left] = chars[right];
            chars[right] = temp;
            left++;
            right--;
        }
        return new String(chars);
    }

    public static void main(String[] args) {
        ReverseVowelsOfString  solution  = new ReverseVowelsOfString();

        String input1 = "hello";
        String input2 = "leetcode";
        String input3 = "aA";

        System.out.println("Input: " + input1 + " | Reversed Vowels: " + solution.reverseVowels(input1));
        System.out.println("Input: " + input2 + " | Reversed Vowels: " + solution.reverseVowels(input2));
        System.out.println("Input: " + input3 + " | Reversed Vowels: " + solution.reverseVowels(input3));
    }
}
