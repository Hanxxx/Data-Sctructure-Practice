from sort_utils import _random_pivot
def __partition(nums, l, r):
    _random_pivot(nums, l, r)
    pivot = nums[l]
    j = l
    for i in range(l + 1, r + 1):
        if nums[i] <= pivot:
            nums[j + 1], nums[i] = nums[i], nums[j + 1]
            j += 1
    nums[l], nums[j] = nums[j], nums[l]
    return j


def __quick_sort(nums, l, r):
    if l >= r:
        return
    p = __partition(nums, l ,r)
    __quick_sort(nums, l, p - 1)
    __quick_sort(nums, p + 1, r)


def quick_sort(nums):
    __quick_sort(nums, 0, len(nums) - 1)
