def sort_colors(nums):
    counter = [0] * 3
    for item in nums:
        counter[item] += 1

    nums[:] = []
    for i in range(len(counter)):
        nums += [i] * counter[i]

a = [2,0,2,1,1,0]
sort_colors(a)
print(a)