#! python3
# __author__ = "YangJiaHao"
# date: 2018/12/25


def quick_sort(ARRAY):
    """Pure implementation of quick sort algorithm in Python
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> quick_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> quick_sort([])
    []
    >>> quick_sort([-2, -5, -45])
    [-45, -5, -2]
    """
    ARRAY_LENGTH = len(ARRAY)
    if( ARRAY_LENGTH <= 1):
        return ARRAY
    else:
        PIVOT = ARRAY[0]
        GREATER = [ element for element in ARRAY[1:] if element > PIVOT ]
        LESSER = [ element for element in ARRAY[1:] if element <= PIVOT ]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)




def quick_sort(array, left, right):
    if left >= right:
        return
    low = left
    high = right
    key = array[low]
    while left < right:
        while left < right and array[right] > key:
            right -= 1
        array[left] = array[right]
        while left < right and array[left] <= key:
            left += 1
        array[right] = array[left]
    array[left] = key
    quick_sort(array, low, left - 1)
    quick_sort(array, left + 1, high)


def shellSort(array):
    "Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1."
    gap = len(array) // 2
    # loop over the gaps
    while gap > 0:
        # do the insertion sort
        for i in range(gap, len(array)):
            val = array[i]
            j = i
            while j >= gap and array[j - gap] > val:
                array[j] = array[j - gap]
                j -= gap
            array[j] = val
        gap //= 2


def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


# 归并排序
def merge_sort(lists):
    # 归并排序
    if len(lists) <= 1:
        return lists

    num = len(lists) // 2

    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])

    return merge(left, right)


# 冒泡排序
def bubble_sort(nums):
    if len(nums) <= 1:
        return nums

    for i in range(1, len(nums)):
        for j in range(len(nums) - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


def quick_sort(nums, left, right):
    if left >= right:
        return

    l, r = left, right

    mid = nums[left]

    while l < r:
        while nums[r] > mid and r > l:
            r -= 1
        nums[l] = nums[r]

        while nums[l] <= mid and l < r:
            l += 1
        nums[r] = nums[l]

    nums[l] = mid
    quick_sort(nums, left, l - 1)
    quick_sort(nums, l + 1, right)

    return nums

nums = [1,4,3,2,5,0]

print(quick_sort(nums,0,len(nums)-1))


