def find_missing_repeated(nums):
    n = len(nums)

    s = n * (n + 1) // 2
    sn = sum(nums)

    # For sum of squares
    s2 = n * (n + 1) * (2 * n + 1) // 6
    s2n = sum(map(lambda x: x * x, nums))

    # X - Y
    val1 = s - sn
    # X + Y
    val2 = (s2 - s2n) // val1

    # X = (val1 + val2) // 2
    # Y = (val2 - val1) // 2
    return (val1 + val2) // 2, (val2 - val1) // 2

a = [3, 1, 2, 5, 4, 6, 7, 5]
missing, repeated = find_missing_repeated(a)
print(f"Missing: {missing}, Repeated: {repeated}")