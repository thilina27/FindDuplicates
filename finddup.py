import os
from pathlib import Path
from filecmp import cmp

FILE_DIR = Path('path to file')
files = sorted(os.listdir(FILE_DIR))

duplicate_files = []

# find duplicates
for file in files:

    isdup = False

    for cls in duplicate_files:
        # compare
        isdup = cmp(
            FILE_DIR / file,
            FILE_DIR / cls[0],
            shallow=False
        )
        if isdup:
            cls.append(file)
            break
    # add to dups
    if not isdup:
        duplicate_files.append([file])


print(duplicate_files)
