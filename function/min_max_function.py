# min_max_function.py

students = ["Roel", "Joel", "Charlie", "David", "Caesar", "Frank", "Grace", "Victor", "Magtanggol", "Gregor"]

# Built-in functions to get the min and max names
print("Alphabetically first student:", min(students))
print("Alphabetically last student:", max(students))

# Custom function to get the max name (alphabetically)
def max_custom(students):
    return sorted(students)[-1]

print("Custom max student:", max_custom(students))
