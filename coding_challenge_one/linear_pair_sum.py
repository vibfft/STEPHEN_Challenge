#!/usr/bin/python3

array1 = [1, 2, 3, 9]  # will return false when looking for sum of 8
array2 = [1, 2, 4, 4]  # will return true when looking for sum of 8
array3 = [2, 3, 4, 5]

# assumption is ordered list still


def pair_sum(arrayList: list, sum: int) -> None:

    low = 0
    high = len(arrayList) - 1
    while (low < high):  # O(n)
        tmp_sum = arrayList[low] + arrayList[high]
        if tmp_sum == sum:
            return True
        elif tmp_sum > sum:
            high -= 1
        elif tmp_sum < sum:
            low += 1
    return False

# one loop: O(n)


def main():

    print(pair_sum(array1, 8))
    print(pair_sum(array2, 8))
    print(pair_sum(array3, 9))


if __name__ == "__main__":
    main()
