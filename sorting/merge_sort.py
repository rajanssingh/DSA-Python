def main():
    print("Merge sort")
    user_input = input("Enter the array numbers separated by spaces: \n")
    arr = list(map(int,user_input.split()))
    print(f"Array before sort : \n{arr}")

    sorted_arr = merge_sort(arr)

    print(f"Array after sort : \n{sorted_arr}")

def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    print(mid)
    l = arr[:mid]
    r = arr[mid:]

    sorted_l = merge_sort(l)
    sorted_r = merge_sort(r)

    return merge(sorted_l,sorted_r)

def merge(l, r):
    res = []
    i = j = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            res.append(l[i])
            i+=1
        else:
            res.append(r[j])
            j+=1

    while i < len(l):
        res.append(l[i])
        i+=1
    while j < len(r):
        res.append(r[j])
        j+=1

    return res


if __name__ == "__main__":
    main()