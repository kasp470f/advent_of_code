import os
import sys

def create_aoc_structure(year: str):
    base_dir = os.path.join(os.getcwd(), year)
    
    try:
        os.makedirs(base_dir, exist_ok=True)
        for day in range(1, 25):
            day_dir = os.path.join(base_dir, f"day_{day:02}")
            os.makedirs(day_dir, exist_ok=True)
        print(f"Advent of Code {year} structure created successfully.")
    except Exception as e:
        print(f"Error creating directory structure: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <year>")
        sys.exit(1)
    
    year = sys.argv[1]
    if not year.isdigit() or len(year) != 4:
        print("Please provide a valid 4-digit year.")
        sys.exit(1)
    
    create_aoc_structure(year)