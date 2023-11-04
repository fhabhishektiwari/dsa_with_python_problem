# evn_num=2
# n=5
# while evn_num<n:
#     print(evn_num)
#     evn_num+=2

# write a program to print odd number btwn 1 to 100.
# odd_num=1
# n=100
# while odd_num<=n:
#     if(odd_num%2!=0):
#         print(odd_num)
#     odd_num=odd_num+1


# write a program to check whether number is prime number
# n=8
# i=2
# is_prime_number=True
# while i<n:
#     if(n%i==0):
#         is_prime_number=False
#         break
#     i=i+1
# if is_prime_number:
#     print("Prime number")
# else:
#     print("Not prime number")


# to check size of variable
# import sys
# a="1.4"
# size= sys.getsizeof(a)
# print(size)

# =======================================================
# a=9
# if(a==9):
#     print("Nine")
# if(a>0):
#     print("Positive")
# else:
#     print("Negative")
#
# =======================================================
# a = 2
# b = a + 1
# a = 3
# if(a == b):
#     print(a)
# else:
#     print(a + 1)

# =======================================================
# a=24
# if(a>20):
#     print("Love")
# elif(a==24):
#     print("Lovely")
# else:
#     print("Abhishek Tiwari")
# =======================================================
#
# user_input=input("Enter a character: ")
# if 'a' <=user_input<='z':
#     print("It is lowercase")
# elif 'A' <=user_input<='Z':
#     print("It is Uppercase")
# elif '0'<=user_input<='9':
#     print("it is Numeric")
# else:
#     print("Invalid")
# =======================================================
# st_num=int(input("Enter start number: "))
# end_num=int(input("Enter end number: "))
# while st_num<=end_num:
#     print(st_num)
#     st_num+=1
# =======================================================
# write a program to print the sum of 1 to N
# st_num=int(input("Enter start number: "))
# temp=st_num;
# end_num=int(input("Enter end number: "))
# sum_of_num=0
# while st_num<=end_num:
#     sum_of_num=sum_of_num+st_num
#     st_num+=1
# print(f"the sum of {temp} to {end_num} = {sum_of_num}")

# =======================================================
# write a program to print sum of all even number the number between 1 to N

# st_num = int(input("Enter start number: "))
# temp = st_num;
# end_num = int(input("Enter end number: "))
# sum_of_num = 0
# while st_num <= end_num:
#     if st_num%2==0:
#         sum_of_num = sum_of_num+st_num
#     st_num+=1
# print(f"the sum of Even number between {temp} to {end_num} = {sum_of_num}")
# =======================================================
prime_num=2;
n=int(input("Enter a number: "))
while prime_num<n:
    if n%prime_num==0:
        print(f"{prime_num} Not prime")
    else:
        print(f"{prime_num} Prime")
    prime_num+=1



# ======================================================
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         self.l1=l1[::-1]
#         self.l2=l2[::-1]
#         int_number1 = int("".join(map(str, self.l1)))
#         int_number2 = int("".join(map(str, self.l2)))
#         sum=int_number1+int_number2
#         print(type(sum),sum)
#         int_to_list=[int(el) for el in str(sum)]
#         return int_to_list[::-1]
#         # return int_to_list[::-1]
#
# # l1=[2,4,3]
# # l2=[5,6,4]
# l1=[0]
# l2=[0]
# obj=Solution()
# obj.addTwoNumbers(l1,l2)
