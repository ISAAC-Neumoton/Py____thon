# take user input to craete an array
# checks if it's empty
# promt again if empty
# ASks what to search for
# sorts the array if neede using bubble sort
# perform binary search
#return founf or not found

#prompt for array
def get_array():
    print("\n  SEARCH FOR A NUMBER IN ANY NUMERIC ARRAY\n")
    while True:
        user_input = input("Enter/paste your Array here, separated by commas : ")

        if not user_input:
            print("\nEnter an array to continue: \n\n\n\n")
            continue

        try:
            arr = list(map(int, user_input.split(",")))
            return arr #we exit the function if successfull
        except ValueError:
            print("Ensure that your are numbers:  \n\n\n\n")

get_arr= get_array()
print("Your array is: ", get_arr)

# prompt for element to search for
def get_element():
    while True:
        try:
            target = int(input("Enter the number you want to look for: "))
            return target
        except ValueError:
            print("Ensure you input is numeric: ")
            continue
target = get_element()

#sort the array by bubble sort

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0,n-i-1):

            if arr[j] > arr[j+1]:

                arr[j],arr[j+1] = arr[j+1], arr[j] 

    return arr
sorted_arr = bubble_sort(get_arr)

def search(arr,target):
    u = 0
    v = len(arr)-1

    while u <= v:
        m = (u+v)//2
        if arr[m] == target:
            return f"Found at {m}"
        
        elif arr[m] < target:
            u = m + 1
        else:
            v = m -1

    return "Not Found"
result = search(sorted_arr, target)
print(result)


