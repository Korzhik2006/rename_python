import os

def rename_files(directory, base_name):

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    files.sort()

    count = 0
    for index, filename in enumerate(files):
        next, ext = os.path.splitext(filename)
        new_name = f"{base_name}_{index + 1}{ext}"

        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)

        os.rename(old_path, new_path)
        count += 1
    return count