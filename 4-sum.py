def four_sum(nums):
    n = len(nums)

    for i in range(n):
        for j in range(i, n):
            l = j + 1
            r = n - 1

            while l < r:
                if nums[i] + nums[j] + nums[l] + nums[r] == 0:
                    print([nums[i], nums[j], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    
                elif nums[i] + nums[j] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1