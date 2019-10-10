def BinarySearch (nums,target):
    '''
    Find the last position of target
    :param nums: [0,1,2,3,3,4,5,6,7]
    :param target: 3
    :return: 3
    '''
    if not nums:
        return -1

    start, end = 0, len(nums) -1

    while start + 1 < end :
        mid = (start + end)// 2

        if nums[mid] < target:
            start = mid

        elif nums[mid] == target:
            start = mid

        else:
            end = mid
        print(nums[start:end+1])

    if nums[end] == target:
        return end
    if nums[start] == target:
        return start
    return -1

if __name__ == '__main__':
    print(BinarySearch([1,1], 1))
    #print(BinarySearch([0,1,1,2,3,3,4,5,6,7],1))