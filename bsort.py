def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1]=arr[j+1],arr[j]
        print(arr)
size=int(input("Enter the elements:"))
arr=[]
print("Enter the Elements:")
for _ in range(size):
    num=int(input())
    arr.append(num)
print("Original list:",arr)
bubble_sort(arr)
print("BubbleSorted:",arr)


