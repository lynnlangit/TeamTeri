import csv
import random
import os

def load_greetings():
    """Load greetings from the CSV file."""
    greetings = []
    csv_path = os.path.join('samples', 'greetings.csv')
    
    with open(csv_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            greetings.append(row['greeting'])
    
    return greetings

def main():
    """Test version with hardcoded name."""
    greetings = load_greetings()
    
    name = "Alice"  # Test name
    greeting = random.choice(greetings)
    
    print(f"{greeting} {name}.")

if __name__ == "__main__":
    main()