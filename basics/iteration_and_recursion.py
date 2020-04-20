def iterTest(low, high):
    while low <= high:
        print(low)
        low += 1


def recurTest(low, high):
    if low <= high:
        print(low)
        recurTest(low+1, high)


