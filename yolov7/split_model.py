import os

def split_file(input_file, chunk_size):
    with open(input_file, 'rb') as f:
        chunk_num = 1
        while chunk := f.read(chunk_size):
            with open(f'{input_file}_part_{chunk_num}', 'wb') as chunk_file:
                chunk_file.write(chunk)
            chunk_num += 1

input_file = 'best.pt'
chunk_size = 45 * 1024 * 1024  # 50 MB (adjust as needed)
split_file(input_file, chunk_size)
