# Assign 10 last names to an array
last_names = ["Ruth", "Ortiz", "Bonds", "Sosa", "Rzzo", 
              "Bryant", "Baez", "Ross", "Swanson", "Happ"]

# Assign 10 exam scores to a parallel array
exam_scores = [85, 92, 78, 90, 88, 76, 95, 89, 84, 91]

# Function to display the names with their scores
def display_names_and_scores(names, scores):
    print("Names and Scores in order:")
    for i in range(len(names)):
        print(f"{names[i]} - {scores[i]}")

# Function to display the names with their scores in reverse order
def display_names_and_scores_reverse(names, scores):
    print("\nNames and Scores in reverse order:")
    for i in range(len(names)-1, -1, -1):
        print(f"{names[i]} - {scores[i]}")

# Calling the functions
display_names_and_scores(last_names, exam_scores)
display_names_and_scores_reverse(last_names, exam_scores)
