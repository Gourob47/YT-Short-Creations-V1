import os
from pytubefix import YouTube
import ffmpeg
import re




def get_video_size(stream):

    return stream.filesize / (1024 * 1024)

# def download_youtube_video(url):
#     try:
#         yt = YouTube(url)

#         video_streams = yt.streams.filter(type="video").order_by('resolution').desc()
#         audio_stream = yt.streams.filter(only_audio=True).first()

#         print("Available video streams:")
#         for i, stream in enumerate(video_streams):
#             size = get_video_size(stream)
#             stream_type = "Progressive" if stream.is_progressive else "Adaptive"
#             print(f"{i}. Resolution: {stream.resolution}, Size: {size:.2f} MB, Type: {stream_type}")

#         choice = int(input("Enter the number of the video stream to download: "))
#         selected_stream = video_streams[choice]

#         if not os.path.exists('videos'):
#             os.makedirs('videos')

#         print(f"Downloading video: {yt.title}")
#         video_file = selected_stream.download(output_path='videos', filename_prefix="video_")

#         if not selected_stream.is_progressive:
#             print("Downloading audio...")
#             audio_file = audio_stream.download(output_path='videos', filename_prefix="audio_")

#             print("Merging video and audio...")
#             output_file = os.path.join('videos', f"{yt.title}.mp4")
#             stream = ffmpeg.input(video_file)
#             audio = ffmpeg.input(audio_file)
#             stream = ffmpeg.output(stream, audio, output_file, vcodec='libx264', acodec='aac', strict='experimental')
#             ffmpeg.run(stream, overwrite_output=True)

#             os.remove(video_file)
#             os.remove(audio_file)
#         else:
#             output_file = video_file

        
#         print(f"Downloaded: {yt.title} to 'videos' folder")
#         print(f"File path: {output_file}")
#         return output_file

#     except Exception as e:
#         print(f"An error occurred: {str(e)}")
#         print("Please make sure you have the latest version of pytube and ffmpeg-python installed.")
#         print("You can update them by running:")
#         print("pip install --upgrade pytube ffmpeg-python")
#         print("Also, ensure that ffmpeg is installed on your system and available in your PATH.")




def sanitize_filename(filename):
    """Sanitize the filename to remove invalid characters."""
    return re.sub(r'[\\/*?:"<>|]', '_', filename)

def get_video_size(stream):
    """Estimate the size of the video stream in MB."""
    if stream.filesize:
        return stream.filesize / (1024 * 1024)
    return 0.0

def download_youtube_video(url):
    try:
        yt = YouTube(url)

        # Sanitize video title for file naming
        sanitized_title = sanitize_filename(yt.title)

        # Get video and audio streams
        video_streams = yt.streams.filter(type="video").order_by('resolution').desc()
        audio_stream = yt.streams.filter(only_audio=True).first()

        print("Available video streams:")
        for i, stream in enumerate(video_streams):
            size = get_video_size(stream)
            stream_type = "Progressive" if stream.is_progressive else "Adaptive"
            print(f"{i}. Resolution: {stream.resolution}, Size: {size:.2f} MB, Type: {stream_type}")

        # User selects a video stream
        choice = int(input("Enter the number of the video stream to download: "))
        selected_stream = video_streams[choice]

        # Create output directory if it doesn't exist
        if not os.path.exists('videos'):
            os.makedirs('videos')

        print(f"Downloading video: {sanitized_title}")
        video_file = selected_stream.download(output_path='videos', filename=f"video_{sanitized_title}.mp4")

        # If the selected stream is not progressive, download audio and merge
        if not selected_stream.is_progressive:
            print("Downloading audio...")
            audio_file = audio_stream.download(output_path='videos', filename=f"audio_{sanitized_title}.mp4")

            print("Merging video and audio...")
            output_file = os.path.join('videos', f"{sanitized_title}.mp4")
            ffmpeg.input(video_file).output(ffmpeg.input(audio_file), output_file, vcodec='libx264', acodec='aac').run(overwrite_output=True)

            # Clean up temporary files
            os.remove(video_file)
            os.remove(audio_file)
        else:
            output_file = video_file

        print(f"Downloaded: {sanitized_title} to 'videos' folder")
        print(f"File path: {output_file}")
        return output_file

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please make sure you have the latest version of pytube and ffmpeg-python installed.")
        print("You can update them by running:")
        print("pip install --upgrade pytube ffmpeg-python")
        print("Also, ensure that ffmpeg is installed on your system and available in your PATH.")


if __name__ == "__main__":
    youtube_url = input("Enter YouTube video URL: ")
    download_youtube_video(youtube_url)
