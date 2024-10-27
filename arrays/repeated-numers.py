def duplicate_number(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    fast = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

a = [3, 1, 2, 5, 4, 6, 7, 5]
print(duplicate_number(a))