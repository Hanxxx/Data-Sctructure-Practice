from my_utils import timer

def oddGenerator(n, m):
    while n < m:
        yield n
        n += 2

def oddList(n, m):
    lst = []
    while n < m:
        lst.append(n)
        n += 2
    return lst

@timer('Generator')
def sumGen(n, m):
    sum(oddGenerator(n, m))
    
@timer('List')
def sumList(n, m):
    sum(oddList(n, m))

sumGen(1, 10000)
sumList(1, 10000)
