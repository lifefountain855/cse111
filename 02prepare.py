import math

# get the inputs
inp0 = int(input("the number of manufactured items: "))
inp1 = int(input("the number of items that the user will pack per box: "))

# calculate the number of boxes needed
res =math.ceil(inp0/inp1)

print(f"the number of boxes needed is {res}")