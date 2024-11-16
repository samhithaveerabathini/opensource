a=int(input())
arr=list(map(int, input().split()))
sort =True
for i in range(1,a):
    if arr[i]<arr[i-1]:
        sort=False
        break
print("true" if sort else "false")
    
