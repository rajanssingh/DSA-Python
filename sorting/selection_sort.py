def main():
    print("Selection sort")
    user_input = input("Enter the array numbers separated by spaces: \n")
    arr = list(map(int,user_input.split()))
    print(f"Array before sort : \n{arr}")

    sorted_arr = selection_sort(arr)

    print(f"Array after sort : \n{sorted_arr}")


def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest_index))
    return sorted_arr

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

if __name__ == "__main__":
    main()