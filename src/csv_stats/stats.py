def column_stats(values: list[str]) -> dict[str, float | None]:
    nums = [] 
    for value in values:
        try:
            nums.append(float(value))
        except ValueError:
            pass #
        if not nums: 
            return {"min": None, "max": None, "avg": None}
    return {"min": min(nums), "max": max(nums), "avg": sum(nums) / len(nums)}