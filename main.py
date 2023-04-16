import argparse
import os
from mp3_reader import get_mp3_files
from m4b_converter import convert_mp3_to_m4b

def main(input_directory, output_file_path, pattern=None):
    mp3_files = get_mp3_files(input_directory, pattern)
    output_name = os.path.basename(output_file_path)
    output_dir = os.path.dirname(output_file_path)

    if not output_dir:
        output_dir = os.getcwd()

    os.makedirs(output_dir, exist_ok=True)

    m4b_file = convert_mp3_to_m4b(mp3_files, output_dir, output_name)
    print(f"Created M4B file: {m4b_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert MP3 files to M4B format.")
    parser.add_argument("input_directory", help="Path to the directory containing the MP3 files.")
    parser.add_argument("output_file_path", help="Path for the output M4B file.")
    parser.add_argument("--pattern", help="Optional pattern to match specific MP3 files.")
    args = parser.parse_args()

    main(args.input_directory, args.output_file_path, args.pattern)
