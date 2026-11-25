# List unique roll numbers from the list

roll_numbers = [101, 105, 102, 101, 108, 108, 110]


for roll in roll_numbers:
    if roll_numbers.count(roll) == 1:
        print("Unique numbers in list: ", roll)


# Find a record of a Employee from list of Tuples

records = [
    (101, "Aice", 50000),
    (102, "Bob", 65000),
    (103, "Charlie", 45000)
]

employeeId = int(input("Enter employee id to search: "))

for employee in records:
    if employee.count(employeeId) == 1:
        print("Employee record exists", employee)


