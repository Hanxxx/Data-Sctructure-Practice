def heap_sort(nums):
    n = len(nums)
    def __shift_down(i, nums, n):
        val = nums[i]
        while i * 2 + 1 < n:
            j = i * 2 + 1   # j is left child of i
            if j + 1 < n and nums[j + 1] > nums[j]:
                # if right child exist and greater than left
                j = j + 1
            if val >= nums[j]:
                # found the position (i) for this value
                break
            nums[i] = nums[j]
            i = j
        nums[i] = val

    # Heapify
    for i in range((n - 2) // 2, -1, -1):
        __shift_down(i, nums, n)
    
    # In place heap pop, swap to the back.
    # shift_down for the rest of array
    for i in range(n - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        __shift_down(0, nums, i)

