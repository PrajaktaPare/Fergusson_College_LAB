class Solution:
    def reverseWords(self, s: str) -> str:
       words = s.split()
       words.reverse()
       return ' '.join(words)


if __name__ == "__main__":
    solution = Solution()
    input1 = "  hello world!  "
    input2 = "a good   example"
    input3 = "  Bob    Loves  Alice   "

    print("Input:", repr(input1), "| Reversed Words:", repr(solution.reverseWords(input1)))  # Expected: "world! hello"
    print("Input:", repr(input2), "| Reversed Words:", repr(solution.reverseWords(input2)))  # Expected: "example good a"
    print("Input:", repr(input3), "| Reversed Words:", repr(solution.reverseWords(input3)))  # Expected: "Alice Loves Bob"
