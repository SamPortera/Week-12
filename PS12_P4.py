# Function to load player names and batting averages from a file
def load_players(filename):
    player_names = ["Rizzo", "Bryant", "Baez"]
    batting_averages = [ .350, .300, .284]
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    player_names.append(parts[0])
                    try:
                        batting_averages.append(float(parts[1]))
                    except ValueError:
                        print(f"Invalid batting average for player {parts[0]}. Skipping.")
                else:
                    print(f"Invalid line format: {line.strip()}")
    except FileNotFoundError:
        print(f"File {filename} not found!")
    return player_names, batting_averages

# Function to display players and batting averages
def display_players(players, averages):
    print("\nPlayer Names and Batting Averages:")
    for player, average in zip(players, averages):
        print(f"{player} - {average:.3f}")

# Function to search for a player by last name
def search_player(players, averages, search_name):
    found = False
    for i in range(len(players)):
        if players[i].lower() == search_name.lower():
            print(f"\nFound: {players[i]} - Batting Average: {averages[i]:.3f}")
            found = True
            break
    if not found:
        print(f"\nPlayer '{search_name}' not found.")

# Main program
filename = 'players.txt'
players, averages = load_players(filename)

# Check if data was loaded before proceeding
if players:
    # Display all players
    display_players(players, averages)

    # Repeatedly ask user for player name to search
    while True:
        search_name = input("\nEnter a player's last name to search (or type 'exit' to quit): ")
        if search_name.lower() == 'exit':
            print("Goodbye!")
            break
        search_player(players, averages, search_name)
else:
    print("No player data available to search.")
