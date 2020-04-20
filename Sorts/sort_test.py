from insertion_sort import *
from selection_sort import *
from bubble_sort import *
from merge_sort import *
from quick_sort import *
from quick_sort_2way import *
from quick_sort_3way import *
from sort_utils import SortTestHelper

if __name__ == "__main__":

    nums = SortTestHelper.genRandomArray(1000, 0, 10000)
    N = [nums[:] for i in range(10)]
    SortTestHelper.testSort(insertion_sort, N[0])
    SortTestHelper.testSort(selection_sort, N[1])
    SortTestHelper.testSort(bubble_sort, N[2])
    SortTestHelper.testSort(merge_sort, N[3])
    SortTestHelper.testSort(merge_sort_bottom_up, N[4])
    SortTestHelper.testSort(quick_sort, N[5])
    SortTestHelper.testSort(quick_sort_2way, N[6])
    SortTestHelper.testSort(quick_sort_3way, N[7])