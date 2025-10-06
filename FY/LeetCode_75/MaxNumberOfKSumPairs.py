from collections import Counter

def max_operations(nums, k):
    
    freq = Counter()
    operations = 0

    for num in nums:
        complement = k - num 

        if freq[complement] > 0:
            operations += 1  
            freq[complement] -= 1  
        else:
           
            freq[num] += 1

    return operations


if __name__ == "__main__":
 
    nums1 = [1, 2, 3, 4]
    k1 = 5
    print("Output:", max_operations(nums1, k1)) 

 
    nums2 = [3, 1, 3, 4, 3]
    k2 = 6
    print("Output:", max_operations(nums2, k2))  
