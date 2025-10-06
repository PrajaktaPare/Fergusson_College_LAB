#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        const int n = nums.size();
        vector<int> ans(n);       
        vector<int> prefix(n, 1); 
        vector<int> suffix(n, 1); 

        // Calculate the prefix product array
        for (int i = 1; i < n; ++i)
            prefix[i] = prefix[i - 1] * nums[i - 1];

        // Calculate the suffix product array
        for (int i = n - 2; i >= 0; --i)
            suffix[i] = suffix[i + 1] * nums[i + 1];

        // Calculate the result by multiplying prefix and suffix
        for (int i = 0; i < n; ++i)
            ans[i] = prefix[i] * suffix[i];

        return ans;
    }
};

int main() {
    Solution solution;

    // Test case 1
    vector<int> nums1 = {1, 2, 3, 4};
    vector<int> result1 = solution.productExceptSelf(nums1);
    cout << "Product Except Self for [1, 2, 3, 4]: ";
    for (int num : result1) {
        cout << num << " ";
    }
    cout << endl;

    // Test case 2
    vector<int> nums2 = {5, 6, 7};
    vector<int> result2 = solution.productExceptSelf(nums2);
    cout << "Product Except Self for [5, 6, 7]: ";
    for (int num : result2) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
