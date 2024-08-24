import os
import re

# Minta pengguna untuk memasukkan path folder tempat file-file .txt berada
folder_path = input("Masukkan path folder tempat file .txt berada: ")

# Minta pengguna untuk memasukkan kata kunci pencarian
search_keywords = input("Search Keyword ? (pisahkan dengan tanda koma): ").split(' ')

# Minta pengguna untuk memasukkan nama file tujuan
output_file_name = input("Save File As ?: ")

# Membuka file results.txt untuk ditulis dengan menentukan codec UTF-8
with open("results.txt", 'a', encoding='utf-8') as result_file:

    # Loop melalui semua file dalam folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)

            # Membuka setiap file .txt dalam mode binary
            with open(file_path, 'rb') as file:
                try:
                    # Membaca file dalam bentuk chunk
                    chunk_size = 4096  # Sesuaikan ukuran chunk jika diperlukan
                    while chunk := file.read(chunk_size):
                        # Mendekode dan memisahkan baris
                        lines = chunk.decode('utf-8', errors='ignore').splitlines()

                        # Loop melalui setiap baris dalam file
                        for line in lines:
                            # Memeriksa apakah setidaknya satu kata kunci atau pola regex ada dalam baris
                            if any(re.search(keyword, line) for keyword in search_keywords):
                                # Menyimpan baris yang memenuhi kondisi ke dalam file tujuan
                                result_file.write(line + '\n')

                                # Juga menyimpan baris yang cocok ke dalam file yang ditentukan pengguna
                                with open(output_file_name, 'a', encoding='utf-8') as custom_result_file:
                                    custom_result_file.write(line + '\n')
                except UnicodeDecodeError:
                    print(f"Error decoding file: {file_path}")
                    continue