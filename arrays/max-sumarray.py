def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0

    total = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        total += nums[i]
        max_sum = max(max_sum, total)
        if total < 0:
            total = 0

    return max_sum

max_sum = maxSubArray([-2, 1])
print(max_sum)