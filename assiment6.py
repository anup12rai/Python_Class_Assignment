# Write a Python program that takes a list of test scores as input. Determine and print the following:
# The average score.
# The highest score.
# The lowest score.
# The number of students who scored above 80.

ani = []
ave = 0
for i in range(5):
    
   er = int(input("Enter the number od the student scored: "))
   sa = ani.append(er)
print(ani)
   
for i in range(0,len(ani)):
       ave+=ani[i]
       op = ave/len(ani)
print("The average score")
print(float(op))

par = ani[0]
if i in ani[1:]:
    if i > par:
        par = i
        print(f"the highest score is {par}")
    
    elif i < par:
        par = i
        print(f"the lower score is {par}")