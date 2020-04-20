from sort_utils import _random_pivot
def __partition_3way(nums, l, r):
    _random_pivot(nums, l, r)
    pivot = nums[l]
    i, j, k = l + 1, l, r + 1
    while i < k:
        if nums[i] > pivot:
            nums[i], nums[k - 1] = nums[k - 1], nums[i]
            k -= 1
        elif nums[i] < pivot:
            nums[j + 1], nums[i] = nums[i], nums[j + 1]
            j += 1
            i += 1
        else:
            i += 1
    nums[l], nums[j] = nums[j], nums[l]
    j -= 1
    return j + 1, k - 1


def __quick_sort_3way(nums, l, r):
    if l >= r:
        return
    p, q = __partition_3way(nums, l, r)
    __quick_sort_3way(nums, l, p - 1)
    __quick_sort_3way(nums, q + 1, r)


def quick_sort_3way(nums):
    __quick_sort_3way(nums, 0, len(nums) - 1)
