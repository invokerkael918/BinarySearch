def kClosestNumbers(A, target, k):
    """

    :param A:
    :param target:
    :param k:
    :return:
    """
    right = find_the_upper(A,target)
    left = right - 1
    result = []
    for _ in range(k):
        if is_left_closer(A,target,left,right):
            result.append(A[left])
            left-=1

        else:
            
            result.append(A[right])
            right+=1
    return result

def find_the_upper(A, target):
    start, end = 0, len(A) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if A[mid] >= target:
            end = mid
        else:
            start = mid

    if A[start] >= target:
        return start
    if A[end] >= target:
        return end
    return end + 1

def is_left_closer(A,target,left,right):
    if left<0:
        return False
    if right >= len(A):
        return True
    return A[right] - target  >= target - A[left]



if __name__ == '__main__':
    print(kClosestNumbers([1,2,7,8,9],3,3))
