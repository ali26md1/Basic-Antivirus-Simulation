import os
import hashlib
import shutil

# Folder to scan
SCAN_FOLDER = "scan_folder"

# Quarantine folder
QUARANTINE_FOLDER = "quarantine"

# This hash corresponds to the word "hello"
MALWARE_HASHES = {
    "5d41402abc4b2a76b9719d911017c592"
}

def calculate_hash(file_path):
    hasher = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except:
        return None

def scan_files():
    # Create quarantine folder if not exists
    if not os.path.exists(QUARANTINE_FOLDER):
        os.makedirs(QUARANTINE_FOLDER)

    print("Scanning started...\n")

    # Go through files
    for root, dirs, files in os.walk(SCAN_FOLDER):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_hash(file_path)

            if file_hash is None:
                print(f"Could not read: {file}")
                continue

            print(f"Checking: {file}")

            if file_hash in MALWARE_HASHES:
                print(f"Malware detected: {file}")

                quarantine_path = os.path.join(QUARANTINE_FOLDER, file)
                shutil.move(file_path, quarantine_path)

                print(f"Moved to quarantine: {file}\n")
            else:
                print(f"Safe: {file}\n")

    print("Scan complete.")

# Run program
if __name__ == "__main__":
    scan_files()