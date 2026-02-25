# nearly sorted array
def nearly_sorted(arr, k):
    n = len(arr)
    for i in range(n):
        for j in range(max(0, i-k), min(n, i+k+1)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

if __name__ == "__main__":
    arr = int(input("Enter the nearly sorted array (space-separated): ").split())
    k = int(input("Enter the value of k: "))
    sorted_arr = nearly_sorted(arr, k)
    print("Sorted array:", sorted_arr)
    
