import hashlib


def calculate_checksum(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Process the file in chunks to handle large files
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except IOError:
        return "File not found or unable to read file."


# Example usage:
file_path = '/home/sourabh/Mahindra/images/icc/image_for_git.bin'
checksum = calculate_checksum(file_path)
print("SHA-256 Checksum:", checksum)
