import hashlib
import os
import json

def calculate_hash(file_path, hash_algorithm="sha256"):
    try:
        hash_func = hashlib.new(hash_algorithm)
        with open(file_path, "rb") as file:
            while chunk := file.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def save_hashes(directory, output_file="hashes.json", hash_algorithm="sha256"):
    hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path, hash_algorithm)
            if file_hash:
                hashes[file_path] = file_hash

    with open(output_file, "w") as hash_file:
        json.dump(hashes, hash_file, indent=4)
    print(f"Hashes saved to {output_file}.")

def check_integrity(hash_file="hashes.json", hash_algorithm="sha256"):
    try:
        with open(hash_file, "r") as file:
            saved_hashes = json.load(file)
    except FileNotFoundError:
        print(f"Hash file not found: {hash_file}")
        return

    for file_path, saved_hash in saved_hashes.items():
        current_hash = calculate_hash(file_path, hash_algorithm)
        if not current_hash:
            print(f"Missing file: {file_path}")
        elif current_hash != saved_hash:
            print(f"Tampered file: {file_path}")
        else:
            print(f"Unchanged file: {file_path}")

def main():
    print("File Integrity Checker")
    print("1. Save hashes")
    print("2. Check integrity")
    choice = input("Select an option (1/2): ").strip()

    if choice == "1":
        directory = input("Enter the directory to hash: ").strip()
        save_hashes(directory)
    elif choice == "2":
        hash_file = input("Enter the hash file to check against: ").strip()
        check_integrity(hash_file)
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
