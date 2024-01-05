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

def rename_file_with_uuid(file_path, uuid):
    """Rename the file with the given UUID."""
    directory, old_file_name = os.path.split(file_path)
    new_file_name = f"{uuid}{os.path.splitext(old_file_name)[1]}"
    new_file_path = os.path.join(directory, new_file_name)
    os.rename(file_path, new_file_path)
    return new_file_path

def write_metadata_to_json(file_path, sha1_hash, random_uuid, file_extension):
    """Write metadata to a JSON file."""
    metadata = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],
        "sha1": sha1_hash,
        "uuid": str(random_uuid),
        "type": file_extension
    }
    json_file_path = file_path + ".data.json"
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
    new_file_path = rename_file_with_uuid(file_path, random_uuid)
    file_extension = os.path.splitext(new_file_path)[1][1:] # Remove the dot from extension

    json_file_path = write_metadata_to_json(new_file_path, sha1_hash, random_uuid, file_extension)
    print("Metadata written to:", json_file_path)
