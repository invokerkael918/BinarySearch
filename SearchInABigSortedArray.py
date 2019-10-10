def searchBigSortedArray(reader, target):
    """

    :param reader: [1, 3, 6, 9, 21, ...]
    :param target: 3
    :return: 1
    """
    k = 0
    while (reader[k]) < target:
        k = 2 * k + 1

    start, end = k, 0
    while start + 1 < end:
        mid = (start + mid) // 2

        if reader[mid] < target:
            start = mid
        elif reader[mid] == target:
            end = mid
        else:
            end = mid

    if reader[start] == target:
        return start
    if reader[end] == target:
        return end
    return -1


if __name__ == '__main__':
    print(searchBigSortedArray([1, 2, 6, 9, 21], 3))
