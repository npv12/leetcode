def next_permutation(nums):
    breakpoint_index = -1

    # Need to start from behind to ensure that the first digit is greater than the digit behind
    for i in range(len(nums)-2, -1, -1):
        if nums[i] < nums[i + 1]:
            # index i is the break point
            breakpoint_index = i
            break

    if breakpoint_index == -1:
        # Sorted in descending order
        nums.reverse()
        return

    print(breakpoint_index)

    for i in range(len(nums)-1, breakpoint_index, -1):
        if nums[i] > nums[breakpoint_index]:
            # Swap the first digit from back to breakpoint_index-1 which is greater than the digit at breakpoint_index-1
            nums[i], nums[breakpoint_index] = nums[breakpoint_index], nums[i]
            break

    # Reverse the digits after breakpoint_index
    nums[breakpoint_index + 1:] = reversed(nums[breakpoint_index + 1:])

    print(nums)
 

nums = [1,2]
next_permutation(nums)
