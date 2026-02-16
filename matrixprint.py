n=int(input("Enter the size of the matrix: "))
m=int(input("Enter the number of columns: "))
for i in range(n):
    for j in range(1,m+1):
        print(j, end=" ")
    print()