# Printing a simple Python program
print("Hello, world!")
num1 = 2
num2 = 5

print ("the answer is", num1 + num2)

# Variables in Python
name = "Ayodeji"
print (f"Hello, {name}!")

# Format string
location = "London"
transport = "boat"
print(f"{name} is going to {location} by {transport}.")

# Conditional statements(if, elif and else statements).
x = 29
if x > 0:
    print("x is a positive number")
elif x < 0:
    print("x is a negative number")
else:
    print("x is zero")

# Variables, format string and input function
text = input()
print(f"Hello, {text}")

# Python tuples and loop
objects = [x, name, location, transport, "text"]

for object in objects:
    print(object)

# Sets
s = set()
s.add(3)
s.add(5)
s.add(7)
s.add(1)
print(s)

# Dictionaries
ages = {"Ade":25, "Bimpe":23}
ages["Dayo"] = 27
ages["Dayo"] += 1
print(ages)

# Definition (def) function
def add(x):
    return x + 4

def main():
    for i in range (10):
        print("{} + 4 = {}".format(i, add(i)))
    
if __name__ == "__main__":
    main() 