# AI Youtube Shorts Generator

AI Youtube Shorts Generator is a Python tool designed to generate engaging YouTube shorts from long-form videos. By leveraging the power of GPT-4 and Whisper, it extracts the most interesting highlights, detects speakers, and crops the content vertically for shorts. This tool is currently in version 0.1 and might have some bugs.


## Features

- **Video Download**: Given a YouTube URL, the tool downloads the video.
- **Transcription**: Uses Whisper to transcribe the video.
- **Highlight Extraction**: Utilizes OpenAI's GPT-4 to identify the most engaging parts of the video.
- **Speaker Detection**: Detects speakers in the video.
- **Vertical Cropping**: Crops the highlighted sections vertically, making them perfect for shorts.

## Installation

### Prerequisites

- Python 3.7 or higher
- FFmpeg
- OpenCV

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/Gourob47/YT-Short-Creations-V1.git
   ```

2. Install the required Python packages:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   python main.py

   Note: Python and pip required.

   ```

3. Set up the environment variables. Create a `.env` file in the project root directory and add your OpenAI API key:
   ```bash
   OPENAI_API=your_openai_api_key_here
   ```

## Usage

1. Ensure your `.env` file is correctly set up with your OpenAI API key.
2. Run the main script and enter the desired YouTube URL when prompted:
   ```bash
   python main.py
   ```



