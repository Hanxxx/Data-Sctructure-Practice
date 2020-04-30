from binary_search import binary_search, binary_search_floor, binary_search_ceil
from sort_utils import SortTestHelper
N = 40
array = SortTestHelper.genRandomArray(N, 1, 3)
array.sort()
print(array)
while 1:
    target = input("target to search:   ")
    if not target.isnumeric():
        break
    print(binary_search_ceil(array, int(target)))
