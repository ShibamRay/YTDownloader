import os
import random
import string
import csv

# 🔧 Configure this:
VIDEO_FOLDER = './nxtV2'
OUTPUT_CSV = 'next.csv'
VIDEO_EXTENSIONS = ['.mp4', '.mov', '.mkv', '.avi']

def generate_random_name(length=12):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(10, length)))

def clean_name(name):
    name = name.replace('_', ' ').replace('-', ' ')
    name = ' '.join(name.split())  # Removes extra spaces
    return name.strip()

def rename_files_and_create_csv(folder_path, csv_path):
    data = []

    for filename in os.listdir(folder_path):
        name, ext = os.path.splitext(filename)
        if ext.lower() not in VIDEO_EXTENSIONS:
            continue

        original_clean = clean_name(name)
        new_name = generate_random_name() + ext

        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)

        data.append({
            'Original_Name': original_clean,
            'New_File_Name': new_name
        })

    # Write CSV
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Original_Name', 'New_File_Name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    print(f"✅ Renamed {len(data)} files. CSV saved to '{csv_path}'.")

# 🔁 Run the script
if __name__ == '__main__':
    rename_files_and_create_csv(VIDEO_FOLDER, OUTPUT_CSV)
