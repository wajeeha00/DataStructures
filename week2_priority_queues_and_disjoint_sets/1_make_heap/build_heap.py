# python3


def build_heap2(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps

def build_heap(data):
    swaps=[]
    for i in range(len(data)//2,-1,-1):
        sift_down(data,i,swaps)
    return swaps

def sift_down(data,i,swaps):
    min_index= i
    if 2*i+1 < len(data):
        l = 2*i + 1
        if data[l] < data[min_index]:
            min_index = l
    r = 2*i + 2
    if r < len(data) and data[r] < data[min_index]:
        min_index = r
    if i!=min_index:
        swaps.append((i,min_index))
        data[i],data[min_index] = data[min_index],data[i]
        sift_down(data,min_index,swaps)



def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
