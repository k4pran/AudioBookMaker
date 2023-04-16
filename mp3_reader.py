import os
import fnmatch

def get_mp3_files(directory, pattern=None):
    mp3_files = []

    if pattern is None:
        pattern = "*.mp3"

    for root, _, files in os.walk(directory):
        for file in fnmatch.filter(files, pattern):
            mp3_files.append(os.path.join(root, file))

    return mp3_files
