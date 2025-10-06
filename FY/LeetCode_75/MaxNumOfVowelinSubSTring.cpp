#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxVowels(string s, int k) {
     
        auto isVowel = [](char c) {
            return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
        };
        
     
        int cnt = count_if(s.begin(), s.begin() + k, isVowel);
        int ans = cnt;
        
        for (int i = k; i < s.size(); ++i) {
            cnt += isVowel(s[i]) - isVowel(s[i - k]); 
            ans = max(ans, cnt); 
        }
        
        return ans; 
    }
};

int main() {
    Solution solution;

    // Test case 1
    string s1 = "abciiidef";
    int k1 = 3;
    cout << "Max vowels in substring of length " << k1 << " in \"" << s1 << "\": " 
         << solution.maxVowels(s1, k1) << endl;

    // Test case 2
    string s2 = "aeiou";
    int k2 = 2;
    cout << "Max vowels in substring of length " << k2 << " in \"" << s2 << "\": " 
         << solution.maxVowels(s2, k2) << endl;

    // Test case 3
    string s3 = "leetcode";
    int k3 = 3;
    cout << "Max vowels in substring of length " << k3 << " in \"" << s3 << "\": " 
         << solution.maxVowels(s3, k3) << endl;

    return 0;
}
