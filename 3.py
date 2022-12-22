def binary_search(sorted_list: List[int], x: int) -> int:
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == x:
            return mid
        elif sorted_list[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1
