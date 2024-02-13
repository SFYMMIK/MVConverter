# MVConverter

## Description
This is a simple Minimalistic Video to Audio converter tool created by Szymon Grajner[Me]. It allows you to convert Video files between two formats: MP3 and WAV.

## Features

- Convert single or multiple video files to audio files.
- Supported input video formats: `.mp4`, `.mkv`, `.avi`, `.wmv`, `.flv`, `.mov`.
- Supported output audio formats: `.mp3`, `.wav`.

## Prerequisites

- Python 3.x
- `moviepy` library (install via `pip3 install moviepy`)

## Usage

1. Run the program using Python: `python3 MVConverter.py`

2. Choose whether to convert one file or multiple files.
   
   - For a single file conversion, provide the path to the video file and the output directory.
   
   - For multiple files conversion, provide the directory containing the video files and the output directory.

3. Select the output audio format: `mp3` or `wav`.

4. The program will display an animation while converting the files and notify you upon completion.

## Installation

```shell
git clone https://github.com/SFYMMIK/MVConverter.git
```

## Example

### Convert a Single Video File

```shell
python3 MVConverter.py
Enter 'o' for one file or 'm' for multiple files: o
Enter output format (mp3 / wav) [default=mp3]: mp3
Enter input file path: /path/to/video.mp4
Enter output directory: /path/to/output
```

## License
This project is licensed under the [GNU General Public License v3.0](LICENSE).

The GNU General Public License is a free, copyleft license for software and other kinds of works. You are free to distribute and modify this software under the condition that any derivative works are also distributed under the same license terms and conditions.

## Contact
For any questions, issues, or suggestions, feel free to contact the author: [Szymon Grajner](https://sfymmik.web.fc2.com).
