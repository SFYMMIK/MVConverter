# ATTENTION!!! This Program Has Been Made By Szymon Grajner And Is Not Suitable For Paid Reproduction
import sys
import sys
import os
import time
from moviepy.editor import VideoFileClip

def get_audio_duration(file_path):
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() in (".mp4", ".mkv", ".avi", ".wmv", ".flv", ".mov"):
        video = VideoFileClip(file_path)
        return video.duration
    else:
        return None

def convert_audio(input_files, output_format, output_directory):
    animation = ['\\', '|', '-', '/']
    for input_file in input_files:
        _, file_extension = os.path.splitext(input_file)
        if file_extension.lower() not in (".mp4", ".mkv", ".avi", ".wmv", ".flv", ".mov"):
            print(f"Skipping {input_file}, not a supported video file.")
            continue

        output_file = os.path.join(output_directory, os.path.splitext(os.path.basename(input_file))[0] + "." + output_format)
        print("Converting", input_file, end=' ')
        for i in range(10):  # Repeat animation 10 times
            sys.stdout.write('\b' + animation[i % len(animation)])
            sys.stdout.flush()
            time.sleep(0.1)

        video = VideoFileClip(input_file)
        audio = video.audio
        audio.write_audiofile(output_file)

        print('\b', end='', flush=True)  # Clear the animation
        print("Conversion complete!")

def main():
    num_files = input("Enter 'o' for one file or 'm' for multiple files: ")
    output_format = input("Enter output format (mp3 / wav) [default=mp3]: ").lower()
    if output_format not in ['mp3', 'wav', '']:
        print("Default format conversion - mp3.")
        output_format = 'mp3'

    if num_files == "o":
        input_file_path = input("Enter input file path: ")
        output_directory = input("Enter output directory: ")
        convert_audio([input_file_path], output_format, output_directory)
    elif num_files == "m":
        input_directory = input("Enter directory path: ")
        output_directory = input("Enter output directory: ")
        files = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, f))]
        convert_audio(files, output_format, output_directory)
    else:
        print("Invalid option!")

if __name__ == "__main__":
    main()
