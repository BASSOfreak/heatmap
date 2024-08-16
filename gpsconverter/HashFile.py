import hashlib
import module_variables

def hash_file(file_path: str):
    sha1 = hashlib.sha1()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(module_variables.BUF_SIZE)
            if not data:
                break
            sha1.update(data)

    return sha1.hexdigest()


