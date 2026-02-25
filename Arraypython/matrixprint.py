# Matrix Print
'''n=int(input("Enter the size of the matrix: "))
m=int(input("Enter the number of columns: "))
for i in range(n):
    for j in range(1,m+1):
        print(j, end=" ")
    print()'''


# Matrix Print
'''
n=int(input("Enter the size of the matrix: "))
for i in range(n):
    for j in range(1,n+1):
        if i<=j-1:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print() 

    
'''
# Matrix Print
'''
n=int(input("Enter the size of the matrix: "))
for i in range(n):
    for j in range(n):
        if j<=i:
            print(j+1,end=" ")
        else:
            print("",end=" ")
    print(" ")
'''

