def furthestBuilding(heights, bricks, ladders):
    """
    :type heights: List[int]
    :type bricks: int
    :type ladders: int
    :rtype: int
    """
    # Store the heights for which ladders are used

    ladder_height = []
    for i in range(1, len(heights)):
        print(ladders, bricks, ladder_height, heights[i])
        if ladders <= 0 and bricks <= 0:
            print("Breaking out")
            break

        if heights[i - 1] >= heights[i]:
            print(
                "Skipping for height: " + str(heights[i - 1]) + ", " + str(heights[i])
            )
            continue

        if ladders != 0:
            # Exhaust all ladders
            ladders -= 1
            ladder_height.append(heights[i] - heights[i - 1])
            continue

        ladder_height.sort()
        if len(ladder_height) > 0 and ladder_height[0] < heights[i] - heights[i - 1]:
            bricks -= ladder_height[0]
            ladder_height[0] = heights[i] - heights[i - 1]
        else:
            bricks -= heights[i] - heights[i - 1]


    print(bricks, ladder_height)
    if bricks < 0:
        return i - 1
    return i

heights = [4,12,2,7,3,18,20,3,19]
bricks = 10
ladders = 2

heights = [4,2,7,6,9,14,12]
bricks = 5
ladders = 1

print(furthestBuilding(heights, bricks, ladders))