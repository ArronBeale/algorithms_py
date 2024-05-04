import time

def bubble_sort(arr):
    """
    This function sorts an array using the Bubble Sort algorithm.
    It compares each element with the next element and swaps them if they are in the wrong order.
    Then, it moves to the next pair of elements and repeats the process until the array is sorted.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(arr)
                time.sleep(0.5)

def selection_sort(arr):
    """
    This function sorts an array using the Selection Sort algorithm.
    It finds the minimum element in the unsorted part of the array and swaps it with the first element of the unsorted part.
    Then, it moves to the next element and repeats the process until the array is sorted.
    """
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)
        time.sleep(1)     

def main():
    print("Select an algorithm:")
    print("1. Bubble Sort")
    print("2. Selection Sort")

    choice = input("Enter your choice: ")

    if choice == "1":
        arr = [64, 34, 25, 12, 22, 11, 90]
        print("Original array:", arr)
        bubble_sort(arr)
        print("Sorted array:", arr)
    if choice == "2":
        arr = [64, 34, 25, 12, 22, 11, 90]
        print("Original array:", arr)
        selection_sort(arr)
        print("Sorted array:", arr)
    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
