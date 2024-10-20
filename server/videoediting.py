from pydub import AudioSegment
from pydub.playback import play
from moviepy.editor import VideoFileClip, AudioFileClip
import tempfile
import os
import shutil


def speed_up_audio():
    audio = AudioSegment.from_file("output.wav")
    video = VideoFileClip("./media/videos/videogen/480p15/GeneratedScene.mp4")
    
    audio_duration = len(audio) // 1000 # seconds
    video_duration = int(video.duration) # seconds


    if audio_duration > video_duration:
        factor = (audio_duration / video_duration)
        faster_audio = audio.speedup(playback_speed=factor)
        faster_audio.export("output_speed.wav", format="wav")
        return "speed"
    return "normal"

def output_video(audio):
    video = VideoFileClip("./media/videos/videogen/480p15/GeneratedScene.mp4")
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
            print("Loading audio...")
            if audio == "speed": # speeded up
                audio_video = AudioFileClip("output_speed.wav") # moviepy audio format 
            elif audio == "normal": # no speed modification
                audio_video = AudioFileClip("output.wav") # moviepy audio format 
            
            print("Loading video...")
            video = VideoFileClip("./media/videos/videogen/480p15/GeneratedScene.mp4")

            print("Setting audio...")
            final_video = video.set_audio(audio_video)

            print("Writing video file...")
            final_video.write_videofile(temp_video.name, codec="libx264", audio_codec="aac", threads=2, fps=30)

            # copy temporary file to final output
            shutil.copy(temp_video.name, "../client/src/components/videos/output_video.mp4")
        print("Video file written successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_media():
    # clear audio files
    files = ["output.wav", "output_speed.wav"]
    for file in files:
        if os.path.exists(file):
            os.remove(file)
    
    # clear media
    media_path = "./media/videos/videogen/480p15"
    if os.path.exists(media_path) and os.path.isdir(media_path):
        try:
            shutil.rmtree(media_path)
        except Exception as e:
            print(f"Failed to delete {media_path}. Reason: {e}")

    # clear videogen file
    with open('videogen.py', 'w') as file:
        file.write("")
