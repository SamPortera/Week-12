# Function to load names and scores from a file
def load_data(filename):
    names = ["Potter", "Granger", "Weasley", "Dumbledore" ]
    scores = [90, 92, 82, 100]
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 2:
                name = parts[0]
                try:
                    score = int(parts[1])
                    names.append(name)
                    scores.append(score)
                except ValueError:
                    print(f"Invalid score '{parts[1]}' for {name}, skipping.")
    return names, scores

# Function to display names and scores
def display_names_and_scores(names, scores):
    print("\nNames and Scores:")
    for name, score in zip(names, scores):
        print(f"{name} - {score}")

# Function to find and display highest and lowest scoring students
def display_highest_and_lowest(names, scores):
    if not scores:  # Safety check if scores is empty
        print("No scores to evaluate.")
        return

    high_var = scores[0]
    high_index = 0
    low_var = scores[0]
    low_index = 0

    for i in range(1, len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i

    print(f"\nHighest Score: {names[high_index]} - {high_var}")
    print(f"Lowest Score: {names[low_index]} - {low_var}")

# Main program
filename = 'students.txt'  # Make sure this file exists
last_names, exam_scores = load_data(filename)

display_names_and_scores(last_names, exam_scores)
display_highest_and_lowest(last_names, exam_scores)
