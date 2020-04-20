from random import randint
import time
from functools import wraps
def timer(name):

    def _timer(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            stop = time.perf_counter()
            print(f'Runtime of <{name}>: {stop - start:0.4f} seconds')
            return result

        return wrapper

    return _timer
        


def _random_pivot(nums, l, r):
    """
    For quick sort: random pick an element from nums and swap it with 1st element
    """
    p = randint(l, r)
    nums[l], nums[p] = nums[p], nums[l]


def _insertion_sort(nums, l, r):
    for i in range(l + 1, r + 1):
        val = nums[i]
        for j in range(i, l, -1):
            if nums[j - 1] > val:
                nums[j] = nums[j - 1]
            else:
                nums[j] = val
                break


class SortTestHelper():

    @staticmethod
    def genRandomArray(n = 100, low = 0, high = 1000):
        assert(low <= high)
        ret = [0] * n
        for i in range(n):
            ret[i] = randint(low, high)
        return ret


    @staticmethod
    def genNearlyOrderArray(n, swaps):
        ret = [0] * n
        for i in range(n):
            ret[i] = i
        for i in range(swaps):
            x, y = randint(0, n - 1), randint(0, n - 1)
            ret[x], ret[y] = ret[y], ret[x]
        return ret
    

    @staticmethod
    def __isSorted(nums):
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
        return True


    @classmethod
    def testSort(cls, sortFunc, nums):

        @timer(sortFunc.__name__)
        def _test():
            sortFunc(nums)
        
        _test()
        assert(cls.__isSorted(nums))