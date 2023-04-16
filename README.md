# AudioBookMaker

AudioBookMaker is a command-line tool for converting a collection of MP3 files into a single M4B audiobook file. This tool is written in Python and uses FFmpeg for audio conversion and the Mutagen library for handling metadata.

## Installation

1. Install Python 3.11 or later.
2. Install FFmpeg. Ensure that the `ffmpeg` executable is in your system's PATH.
3. Clone or download this repository.
4. Install the required Python packages with pip:

pip install -r requirements.txt


## Usage

Run `main.py` with the following arguments:

- `input_directory`: The path to the directory containing the MP3 files you want to convert.
- `output_file_path`: The path to the output M4B file, including the desired filename.
- `pattern` (optional): A filename pattern to match specific MP3 files within the input directory.

Example:

python main.py "C:\Users\YourUsername\Downloads\MyAudiobook" "C:\Users\YourUsername\Audiobooks\MyAudiobook.m4b" "*.mp3"


This command will read all MP3 files from the `MyAudiobook` directory, convert and merge them into a single M4B file named `MyAudiobook.m4b` in the `Audiobooks` directory.

## Credits

This project was created with the assistance of ChatGPT, an AI language model developed by OpenAI.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
