def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer:
# output will be 3, then 4
# the loop goes through numbers 
# 1,2,3 if condition checks whether each number is greater than 1
# 1 is not greater than 1, so it will be skipper and 2 and 3 will be passed
# by add_one which adds 1 to 2,3 print displays the 3,4


# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer:
# add_one(2) returns 3, becasude function adding 1 to 2
# print will display result on the screen, in the loop print diplay the value added 1 by add_one


