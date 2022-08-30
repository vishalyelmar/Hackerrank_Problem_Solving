def minMaxSum(arr):
    arr=sorted(arr)
    return (sum(arr[:-1]),sum(arr[1:]))
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print(minMaxSum(arr))