# Assign 10 last names to an array
last_names = ["James", "Jordan", "Johnson", "Bird", "Wade", 
              "Kidd", "Miller", "O'Neal", "Pippen", "Rodman"]

# Function to display the names
def display_names(names):
    print("Names in order:")
    for name in names:
        print(name)

# Function to display the names in reverse order
def display_names_reverse(names):
    print("\nNames in reverse order:")
    for name in reversed(names):
        print(name)

# Calling the functions
display_names(last_names)
display_names_reverse(last_names)
