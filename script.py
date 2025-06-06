import os

def convert_heic_with_magick(directory, recursive=False):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".heic"):
                full_path = os.path.join(root, file)
                new_file = os.path.splitext(file)[0] + ".jpg"
                output_path = os.path.join(root, new_file)

                command = f'magick "{full_path}" "{output_path}"'
                result = os.system(command)
                if result == 0:
                    print(f"[OK] Converted: {file} -> {new_file}")
                else:
                    print(f"[ERR] Failed to convert: {file}")
        if not recursive:
            break

convert_heic_with_magick(r"C:\Users\max3l\Documents\seng474\ss\lecture8", recursive=True)
