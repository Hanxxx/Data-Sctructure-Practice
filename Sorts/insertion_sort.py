def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        tmp = nums[i]
        for j in range(i, 0, -1):
            if nums[j - 1] > tmp:
                nums[j] = nums[j - 1]
            else:
                nums[j] = tmp
                break
