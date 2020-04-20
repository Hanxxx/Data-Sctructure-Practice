def __merge(nums, l, mid, r):
    tmp = nums[l: r + 1]
    i, j = 0, mid + 1 - l
    for k in range(l, r + 1):
        if i == mid + 1 - l:
            nums[k] = tmp[j]
            k += 1
            j += 1
        elif j == len(tmp):
            nums[k] = tmp[i]
            k += 1
            i += 1
        elif tmp[i] < tmp[j]:
            nums[k] = tmp[i]
            k += 1
            i += 1
        else:
            nums[k] = tmp[j]
            k += 1
            j += 1    

def __merge_sort(nums, l, r):
    if l >= r:
        return 
    mid = (l + r) // 2
    
    __merge_sort(nums, l, mid)
    __merge_sort(nums, mid + 1, r)
    if nums[mid] > nums[mid + 1]: # Else [l,r] is sorted
        __merge(nums, l, mid, r)
    

def merge_sort(nums):
    """
    Top-down, recursive merge sort
    """
    __merge_sort(nums, 0, len(nums) - 1)

def merge_sort_bottom_up(nums):
    n = len(nums)
    size = 1
    while size <= n:
        for i in range(0, n - size, size * 2):
            __merge(nums, i, i + size - 1, min(n - 1, i + 2 * size - 1))
        size *= 2