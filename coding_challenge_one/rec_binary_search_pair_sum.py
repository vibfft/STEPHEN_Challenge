#!/usr/bin/python3

array1 = [1, 2, 3, 9]  # will return false when looking for sum of 8
array2 = [1, 2, 4, 4]  # will return true when looking for sum of 8


def binary_search(num: int, low: int, high: int, arrayList: list, sum_value: int) -> None:

    if low <= high:
        mid = (high + low) // 2
        print(
            f"SUM: {sum_value}: compare_num: {num}, target_num: {arrayList[mid]}")
        if (arrayList[mid] + num) < sum_value:
            binary_search(num, mid + 1, high, arrayList, sum_value)
        elif (arrayList[mid] + num) > sum_value:
            binary_search(num, low, mid - 1, arrayList, sum_value)
        else:
            print(f"@MID: compare_sum: {arrayList[mid]}, target_num: {num}")
            return True
    else:
        return False

# assumption is ordered list hence you can do binary search


def pair_sum(arrayList: list, sum: int) -> None:

    low = 0
    high = len(arrayList) - 1
    for item in arrayList:    # n
        print(f"item: {item}")
        if binary_search(item, low, high, arrayList, sum):  # log n
            print("Is returned any time?")
            return True

    return False

# outer loop is n and inner nested loop is log n, hence O(n*log n)


def main():

    print(pair_sum(array1, 8))
    print(pair_sum(array2, 8))


if __name__ == "__main__":
    main()
