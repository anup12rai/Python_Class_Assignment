#  Write a Python function to find the maximum number among three given numbers.  ( Rainbow Tip: max() function)

ui = []
def maxnum(ip):
    return max(ip)
for i in range(1,4):
    ip = int(input("Enter any 3 number: "))
    we = ui.append(ip)
print("the maximum number is ",maxnum(ui))    