def main():
    print("Insertion sort")
    user_input = input("Enter the array numbers separated by spaces: \n")
    arr = list(map(int,user_input.split()))
    print(f"Array before sort : \n{arr}")

    sorted_arr = insertion_sort(arr)

    print(f"Array after sort : \n{sorted_arr}")

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        # Insert key into sorted A[1....i-1]
        while j>0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = key
    return arr

if __name__ == "__main__":
    main()