"""
* * *
* * *
* * *
"""

# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         print("*",end=" ")
#         j=j+1
#     print("")
#     i=i+1

# ==========================================
"""
1 1 1
2 2 2
3 3 3
4 4 4
"""
#
# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(i,end=" ")
#         j=j+1
#     print("")
#     i=i+1

# ==========================================
"""
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
"""

# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(j,end=" ")
#         j=j+1
#     print("")
#     i=i+1

# ==========================================
"""
3 2 1
3 2 1
3 2 1
"""

# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     j=1
#     while j<=n:
#         k=n-j+1
#         print(k,end=" ")
#         j=j+1
#     print("")
#     i=i+1

"""
1 2 3
4 5 6 
7 8 9
"""
# n=int(input("Enter a number: "))
# i=1
# count=1
# while i<=n:
#     j=1
#     while j<=n:
#         print(count,end=" ")
#         count+=1
#         j=j+1
#     print("")
#     i=i+1

# ====================================================
"""
*
* *
* * *
* * * *
"""
# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print("*",end=" ")
#         j=j+1
#     print("")
#     i=i+1

# =========================================================
"""
1
2 2
3 3 3
4 4 4 4
"""

# n=int(input("Enter a number: "))
# i=1
# while i<=n:
#     j=1
#     while j<=i:
#         print(i,end=" ")
#         j=j+1
#     print("")
#     i=i+1

# =================================================
"""
1
2 3
4 5 6
7 8 9 10
"""
# n=int(input("Enter a number: "))
# row = current_number = 1
# while row<=n:
#     col=1
#     while col<=row:
#         print(current_number,end=" ")
#         current_number+=1
#         col=col+1
#     print("")
#     row=row+1

# =================================================
"""
1
2 3
3 4 5
4 5 6 7
"""
# num_of_row = int(input("Enter a number: "))
# row = 1
# while row<=num_of_row:
#     col=1
#     current_value = row
#     while col<=row:
#         print(current_value,end=" ")
#         current_value+=1
#         col=col+1
#     print("")
#     row=row+1

# =================================================
"""
1
2 1
3 2 1
4 3 2 1
"""
# num_of_row = int(input("Enter a number: "))
# row = 1
# while row<=num_of_row:
#     col=1
#     while col<=row:
#         print(row-col+1,end=" ")
#         col=col+1
#     print("")
#     row=row+1

# # =================================================
# """
# A A A
# B B B
# C C C
# """
# num_of_row = int(input("Enter a number: "))
# for i in range(num_of_row):
#     current_char = chr(ord('A') + i)
#     for j in range(num_of_row):
#         print(current_char, end=" ")
#     print()

# =================================================
"""
A B C
A B C
A B C
"""
# num_of_row = int(input("Enter a number: "))
# for i in range(num_of_row):
#     for j in range(num_of_row):
#         current_char = chr(ord('A') + j)
#         print(current_char, end=" ")
#     print()

# =================================================
"""
A B C
D E F
G H I
"""
# num_of_row = int(input("Enter a number: "))
# current_char='A'
# for i in range(num_of_row):
#     for j in range(num_of_row):
#         print(current_char, end=" ")
#         current_char = chr(ord(current_char) + 1)
#     print()

# =================================================
"""
A B C
B C D
C D E
"""
# num_of_row = int(input("Enter a number: "))
#
# for i in range(num_of_row):
#     current_char = chr(ord('A')+i)
#     for j in range(num_of_row):
#         print(chr(ord(current_char)+j), end=" ")
#     print()

# =================================================
"""
A 
B B
C C C
"""
# num_of_row = int(input("Enter a number: "))
# for i in range(num_of_row):
#     current_char=chr(ord('A')+i)
#     for j in range(i+1):
#         print(current_char, end=" ")
#     print()

# =================================================
"""
A 
B B
C C C
"""
# num_of_row = int(input("Enter a number: "))
# current_char='A'
# for i in range(num_of_row):
#     for j in range(i+1):
#         print(current_char, end=" ")
#         current_char = chr(ord(current_char) + 1)
#     print()

# =================================================
"""
A 
B C
C D E
D E F G
"""
num_of_row = int(input("Enter a number: "))
for i in range(num_of_row):
    current_char = chr(ord('A') + i)
    for j in range(i + 1):
        print(current_char, end=" ")
        current_char = chr(ord(current_char) + 1)
    print()