def binarySearch(arr: list, target: int) -> bool:

    l = 0
    r = len(arr) - 1

    while l <= r:
        m = l + (r-l)//2

        if arr[m] == target:
            return True
        elif target < arr[m]:
            r = m-1
        else:
            l = m+1
    return False

def sort(arr):
    if len(arr) == 0 or len(arr) == 1:
        return arr
    pivot = arr[-1]

    left = [num for num in arr[:-1] if num <= pivot ]
    right = [num for num in arr[:-1] if num > pivot]

    return sort(left) + [pivot] + sort(right)


def maximumSwap( num: int) -> int:

    num = [char for char in str(num)]
    n = len(num)

    right_max = [0]* (n-1)

    maxx = num[n-1]
    curr_index = n-1

    for i in range(n-2,-1,-1):
        if int(num[i+1]) > int(maxx):
            curr_index = i+1
            maxx = num[i+1]
            right_max[i] = (curr_index, maxx)
        else:
            right_max[i] = (curr_index, maxx)

    for i in range(n-1):
        if int(num[i]) < int(right_max[i][1]):
            num[i], num[right_max[i][0]] = num[right_max[i][0]], num[i]
            break
    return int(''.join(num))

import numpy as np
def shortestPathBinaryMatrix(grid:list) -> int :

    n = len(grid)

    if grid[0][0] != 0 or grid[n - 1][n - 1] != 0 :
        return -1

    result = []

    def recursion(point: (int, int), clear_path_length) -> bool :

        i, j = point

        grid[i][j] = 2

        if i == (n - 1) and j == (n - 1):
            print(result)
            if not result :
                result.append(clear_path_length)
            else :
                result[0] = min(result[0], clear_path_length)

        for i_off, j_off in [(-1, -1), (1, -1), (-1, 1), (1, 1), (0, 1), (0, -1), (-1, 0), (1, 0)] :
            r, c = i + i_off, j + j_off
            if 0 <= r < n and 0 <= c < n and grid[r][c] == 0 :
                return recursion((r, c), clear_path_length + 1)
                grid[i][j] = 0

        print(np.array(grid))

    recursion((0, 0), 1)

    if result :
        return result[0]
    else :
        return -1

grid = [[0,0,0],[1,1,0],[1,1,0]]
print(shortestPathBinaryMatrix(grid))



def mergeSort(arr: list) -> list:

    n = len(arr)

    if len(arr) == 1:
        return arr

    m = len(arr) // 2

    l_arr = mergeSort(arr[: m])
    r_arr = mergeSort(arr[m: ])

    result = [0] * n
    i = 0
    l = 0
    r = 0

    while (l < len(l_arr)) and (r < len(r_arr)):
        if l_arr[l] <= r_arr[r]:
            result[i] = l_arr[l]
            l += 1
        else:
            result[i] = r_arr[r]
            r += 1
        i += 1

    while l < len(l_arr):
        result[i] = l_arr[l]
        i += 1
        l += 1
    while r < len(r_arr):
        result[i] = r_arr[r]
        i += 1
        r += 1

    return result

print(mergeSort([1,24,14,22,23,26]))


def findKthPositive( arr: list, k: int) -> int :
    left, right = 0, len(arr) - 1
    left, right = 0, len(arr) - 1
    while left <= right :
        # print(left, right)
        pivot = left + (right - left) // 2
        print(left,pivot, right)

        if arr[pivot] - pivot - 1 < k :
            left = pivot + 1
        else :
            right = pivot - 1

    return left + k

print(findKthPositive([2,3,4,7,11],5))