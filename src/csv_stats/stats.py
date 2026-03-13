from dataclasses import dataclass


@dataclass
class ColumnStats:
    min: float | None
    max: float | None
    avg: float | None


def column_stats(values: list[str]) -> ColumnStats:
    nums = []
    for value in values:
        try:
            nums.append(float(value))
        except ValueError:
            pass  #
    if not nums:
        return ColumnStats(min=None, max=None, avg=None)
    return ColumnStats(min=min(nums), max=max(nums), avg=sum(nums) / len(nums))
