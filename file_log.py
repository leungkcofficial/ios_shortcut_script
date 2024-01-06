import hashlib
import uuid
import os, sys
import json
from datetime import datetime

def generate_sha1(file_path):
    """Generate the SHA-1 hash of a file."""
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            sha1.update(chunk)
    return sha1.hexdigest()

def generate_random_uuid():
    """Generate a random UUIDv4."""
    return uuid.uuid4()

def write_metadata_to_json(sha1_hash, random_uuid, file_extension):
    """Write metadata to a JSON file."""
    metadata = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
        "sha1": sha1_hash,
        "uuid": str(random_uuid),
        "type": file_extension
    }
    json_file_path = "result.json"
    with open(json_file_path, 'w') as json_file:
        json.dump(metadata, json_file, indent=4)
    return json_file_path

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    sha1_hash = generate_sha1(file_path)
    random_uuid = generate_random_uuid()
    file_extension = os.path.splitext(file_path)[1][1:] # Remove the dot from extension

    json_file_path = write_metadata_to_json(sha1_hash, random_uuid, file_extension)
    print("Metadata written to:", json_file_path)
