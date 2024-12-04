import os

def walk_directory(path: str):
    all_files = []
    for (root, _ , files) in os.walk(path):
        for file in files:
            all_files.append(os.path.join(root, file))
    return all_files
