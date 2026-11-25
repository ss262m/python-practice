# All Odd numbers until 20

for i in range(1, 21):
    if (i % 2 == 1):
        print(i)

# Print the table of 57

for i in range(57, 571, 57):
    print(i)

# Print all multiples of 3 from 1 to 50 skip 15

for i in range(1, 51):
    if i == 15:
        continue
    if(i % 3 == 0):
        print(i)

# Find number between 1 to 1000 which is divisible by 2 inpput numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
counter = 0
for i in range(1, 1001):
    if (i % a == 0 and i % b == 0):
        print(i)
        counter += 1
        if counter == 1:
            break