# Subarray sum equals K

def subarray_sum(nums, k):
    count, curr_sum = 0, 0
    prefix_sums = {0: 1}
    for num in nums:
        curr_sum += num
        count += prefix_sums.get(curr_sum - k, 0)
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
    return count
