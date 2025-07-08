#couting sort 
def csort(arr):
    if not arr:
        return[]
    max_val=max(arr)
    count=[0]*(max_val+1)
    # freq

    for num in arr:
        count[num]+=1
    #count

    for i in range(1, len(count)):
        count[i]+=count[i-1]
    output=[0]*len(arr)
    # stable sort
    for num in reversed(arr):
        output[count[num]-1]=num
        count[num]-=1
    #coping sorted list

    for i in range(len(arr)):
        arr[i]=output[i]
size=int(input("Enter the elements:"))
arr=[]
print("Enter the Elements:")
for _ in range(size):
    num=int(input())
    arr.append(num)
print("before:",arr)
csort(arr)
print("After:",arr)