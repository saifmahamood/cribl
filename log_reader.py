import os

LOG_DIR = '/var/log'

def fetch_logs(filename, keyword, num_lines, chunk_size=1024):
    file_path = os.path.join(LOG_DIR, filename)
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {filename} not found in {LOG_DIR}")

    matching_lines = []

    with open(file_path, 'rb') as file:
        file.seek(0, os.SEEK_END)
        position = file.tell()
        buffer = bytearray()

        while position >= 0 and len(matching_lines) < num_lines:
            # Move back by chunk_size or to the beginning of the file
            read_size = min(chunk_size, position + 1)
            file.seek(position - read_size + 1)
            chunk = file.read(read_size)
            
            # Read the chunk in reverse
            for char in reversed(chunk):
                if char == b'\n' and buffer:
                    line = buffer.decode()[::-1]  # Decode and reverse
                    if keyword.lower() in line.lower():
                        matching_lines.append(line.strip())
                    buffer = bytearray()
                else:
                    buffer.extend(char.to_bytes(1, 'big'))
            
            position -= read_size

        # Handle the first line if no newline was encountered
        if buffer and len(matching_lines) < num_lines:
            line = buffer.decode()[::-1]
            if keyword.lower() in line.lower():
                matching_lines.append(line.strip())

    return matching_lines[::-1]
