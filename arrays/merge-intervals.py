def merge_intervals(intervals):
    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if len(merged) == 0:
            merged.append(interval)
            continue
        if merged[-1][1] < interval[0]:
            # Current one cannot be merged into the new one
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged