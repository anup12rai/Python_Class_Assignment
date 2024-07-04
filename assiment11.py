# Write a Python function to calculate the factorial of a given non-negative integer.
def factorial(df):
    if df == 0 and df == 1:
        return 1
    else:
        an = 1
        for i in range(df,1,-1):
            an *= i
            return an
        



df = int(input("Enter the number: "))
print(factorial(df))