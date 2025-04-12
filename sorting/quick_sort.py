def main():
    print("Quick sort")
    user_input = input("Enter the array numbers separated by spaces: \n")
    arr = list(map(int,user_input.split()))
    print(f"Array before sort : \n{arr}")

    sorted_arr = quick_sort(arr)

    print(f"Array after sort : \n{sorted_arr}")

def quick_sort(arr):
    # base case 0 or 1 element
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr[1:] if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(more)


if __name__ == "__main__":
    main()