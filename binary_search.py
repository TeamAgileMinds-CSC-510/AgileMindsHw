# Example of binary_search
def binary_search(arr, search_value):
    lower_index = 0
    higher_index = len(arr) - 1

    while lower_index <= higher_index:
        middle_index = (lower_index + higher_index) // 2

        if arr[middle_index] == search_value:
            return middle_index
        elif arr[middle_index] > search_value:
            higher_index = middle_index - 1
        else:
            lower_index = middle_index + 1
    return -1


def main():
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    search_value = 15
    result = binary_search(arr, search_value)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")


if __name__ == "__main__":
    main()
