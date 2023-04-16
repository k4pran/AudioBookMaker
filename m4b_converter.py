import os
import tempfile
from pydub import AudioSegment
from mutagen.mp4 import MP4


def convert_mp3_to_m4b(mp3_files, output_dir, output_name):
    temp_dir = tempfile.gettempdir()
    temp_m4a_file = os.path.join(temp_dir, f"{output_name}.m4a.tmp")

    combined_audio = AudioSegment.empty()

    for mp3_file in mp3_files:
        audio = AudioSegment.from_mp3(mp3_file)
        combined_audio += audio

    combined_audio.export(temp_m4a_file, format="mp4", codec="aac", bitrate="64k")

    m4b_file = os.path.join(output_dir, f"{output_name}.m4b")
    temp_m4b_file = os.path.join(temp_dir, f"{output_name}.m4b.tmp")

    # Use FFmpeg to merge the M4A file with the cover image and metadata
    os.system(f'ffmpeg -i "{temp_m4a_file}" -c copy -f mp4 "{temp_m4b_file}"')

    # Rename the temporary M4B file to the final M4B file
    os.rename(temp_m4b_file, m4b_file)

    # Clean up the temporary M4A file
    os.remove(temp_m4a_file)

    return m4b_file
