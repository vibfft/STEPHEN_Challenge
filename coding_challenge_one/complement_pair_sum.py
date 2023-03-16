#!/usr/bin/python3

array1 = [1, 2, 3, 9]  # will return false when looking for sum of 8
array2 = [1, 2, 4, 4]  # will return true when looking for sum of 8
array3 = [2, 3, 4, 5]

# assumption is unordered list
def pair_sum(arrayList: list, sum: int) -> None:

    comp_set = set()
    for item in arrayList:
        if item > sum:
            return False
        
        temp_comp = sum - item
        print(f"{temp_comp}, sum: {sum}, item: {item}, comp_set: {comp_set}")
        if item not in comp_set:
            comp_set.add(temp_comp)
        else:
            return True
    return False 
   
# one loop: O(n)

def main():

    print(pair_sum(array1, 8))
    print(pair_sum(array2, 8))
    print(pair_sum(array3, 9))
if __name__ == "__main__":
    main()
