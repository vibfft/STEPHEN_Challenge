#!/usr/bin/python3

array1 = [1, 2, 3, 9]  # will return false when looking for sum of 8
array2 = [1, 2, 4, 4]  # will return true when looking for sum of 8


def binary_search(num: int, arrayList: list, sum_value: int) -> None:
    SUM = sum_value
    high = len(arrayList) - 1
    mid = 0
    low = 0

    while low <= high:
        mid = (high + low) // 2
        print(f"SUM: {SUM}: compare_num: {num}, target_num: {arrayList[mid]}")
        if (arrayList[mid] + num) < SUM:
            low = mid + 1
        elif (arrayList[mid] + num) > SUM:
            high = mid - 1
        else:
            print(f"@MID: compare_sum: {arrayList[mid]}, target_num: {num}")
            return True

# assumption is ordered list hence you can do binary search


def pair_sum(arrayList: list, sum: int) -> None:

    for item in arrayList:    # n
        if binary_search(item, arrayList, sum):  # log n
            return True

    return False

# outer loop is n and inner nested loop is log n, hence O(n*log n)


def main():

    print(pair_sum(array1, 8))
    print(pair_sum(array2, 8))


if __name__ == "__main__":
    main()
