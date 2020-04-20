from insertion_sort import insertion_sort
from selection_sort import selection_sort
from bubble_sort import bubble_sort
from merge_sort import merge_sort, merge_sort_bottom_up
from quick_sort import quick_sort
from quick_sort_2way import quick_sort_2way
from quick_sort_3way import quick_sort_3way
from heap_sort import heap_sort
from sort_utils import SortTestHelper

if __name__ == "__main__":

    size = 10000
    print(f'==========Sort test for random array==========')
    nums = SortTestHelper.genRandomArray(size, 0, size)
    N = [nums[:] for i in range(10)]
    SortTestHelper.testSort(insertion_sort, N[0])
    SortTestHelper.testSort(selection_sort, N[1])
    SortTestHelper.testSort(bubble_sort, N[2])
    SortTestHelper.testSort(merge_sort, N[3])
    SortTestHelper.testSort(merge_sort_bottom_up, N[4])
    SortTestHelper.testSort(quick_sort, N[5])
    SortTestHelper.testSort(quick_sort_2way, N[6])
    SortTestHelper.testSort(quick_sort_3way, N[7])
    SortTestHelper.testSort(heap_sort, N[8])
    SortTestHelper.testSort(sorted, N[9])