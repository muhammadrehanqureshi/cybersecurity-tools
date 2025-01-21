import re

def parse_log(file_path, search_pattern):
    try:
        with open(file_path, 'r') as log_file:
            print(f"Analyzing log file: {file_path}\n")
            matches = []
            for line_number, line in enumerate(log_file, 1):
                if re.search(search_pattern, line):
                    matches.append((line_number, line.strip()))
            
            if matches:
                print(f"Found {len(matches)} matches for pattern '{search_pattern}':\n")
                for match in matches:
                    print(f"Line {match[0]}: {match[1]}")
            else:
                print(f"No matches found for pattern '{search_pattern}'.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("Welcome to the Log Analyzer!")
    file_path = input("Enter the path to the log file: ").strip()
    search_pattern = input("Enter the pattern to search for (e.g., 'ERROR', 'failed login'): ").strip()
    
    parse_log(file_path, search_pattern)
