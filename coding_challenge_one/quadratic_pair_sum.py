#!/usr/bin/python3

array1 = [1, 2, 3, 9]  # will return false when looking for sum of 8
array2 = [1, 2, 4, 4]  # will return true when looking for sum of 8

# assumption is that the list is sorted
def pair_sum(arrayList: list, num: int) -> None:

    SUM = num
    for item in arrayList:      # n
        for item2 in arrayList: # n
            if (item + item2) == 8:
                print(f"num1: {item}, num2: {item}")
                return True

    return False

# nested loops are multiplication, hence O(n^2)

def main():

    print(pair_sum(array1, 8))
    print(pair_sum(array2, 8))

if __name__ == "__main__":
    main()
