from sort_utils import _random_pivot
def __partition_2way(nums, l, r):
    _random_pivot(nums, l, r)
    pivot = nums[l]
    i, j = l + 1, r
    while 1:
        while i <= j and nums[i] < pivot:
            i += 1
        while i <= j and nums[j] > pivot:
            j -= 1
        if i > j:
            break
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    nums[l], nums[j] = nums[j], nums[l]
    return j

def __quick_sort_2way(nums, l, r):
    if l >= r:
        return
    p = __partition_2way(nums, l, r)
    __quick_sort_2way(nums, l, p - 1)
    __quick_sort_2way(nums, p + 1, r)


def quick_sort_2way(nums):
    __quick_sort_2way(nums, 0, len(nums) - 1)
