arr = [5, 10, 15, 20]

target = int(input("Search element: "))

for i in range(len(arr)):
    if arr[i] == target:
        print("Found at index", i)
        break
else:
    print("Not Found")
