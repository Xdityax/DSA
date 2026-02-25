'''arr=[2,4,6,8,10]
pre=[0]*len(arr)
pre[0]=arr[0]
for i in range(1,len(arr)):
    pre[i]=pre[i-1]+arr[i] 
print(pre)  
'''
#take the input from the user for prefix sum  
size=int(input("Enter the size of the array: "))
arr=[]
for i in range(size):
    arr.append(int(input("Enter the element: ")))
pre=[0]*len(arr)
pre[0]=arr[0]
que=int(input("Enter the number of queries: "))
for i in range(que):
    if i==0:
        pre[0]=arr[0]
        a=int(input("Enter the starting number: "))
        b=int(input("Enter the ending number: "))
d=arr[a]
c=arr[b]
for i in range(1,len(arr)):
    pre[i]=pre[i-1]+arr[i]
print("element is ", pre)
print("Sum:", pre[b] - pre[a-1] if a > 0 else pre[b])
