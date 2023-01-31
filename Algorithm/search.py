from typing import List, NewType


IndexNum = NewType('IndexNum', int)

def linear_search(numbers: List[int], value:int) -> IndexNum:
    for i in range(0, len(numbers)):
        if numbers[i] == value:
            return i
    return -1

def binary_search(numbers: List[int], value:int) -> IndexNum:
    left, right = 0, len(numbers)-1
    while right < left:
        mid = len(numbers) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] > value:
            left = mid + 1
        else:
            right = mid - 1

if __name__ == '__main__':
    nums= [11, 2, 3, 5, 6, 6, 77, 15]
    print(linear_search(nums, value=11))