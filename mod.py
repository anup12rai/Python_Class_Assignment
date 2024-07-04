# def is_palindrome(number):
#     number_str = str(number)
#     return number_str == number_str[::-1]

# user_input = int(input("Enter the integer: "))
# if is_palindrome(user_input):
#     print("apl")
# else:
#     print("not")
user = int (input("Enter the number: "))
us = str(user[::-1])
print(us)