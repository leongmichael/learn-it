from pydub import AudioSegment
from pydub.playback import play
from moviepy.editor import VideoFileClip, AudioFileClip
import tempfile


# Load audio file
audio = AudioSegment.from_file("output.wav")
audio_duration = len(audio) // 1000 # seconds

video = VideoFileClip("./media/videos/videogen/480p15/GeneratedScene.mp4")
video_duration = int(video.duration) # seconds


def speed_up_audio():
    if audio_duration > video_duration:
        factor = (audio_duration / video_duration)
        faster_audio = audio.speedup(playback_speed=factor)
        faster_audio.export("output_speed.wav", format="wav")
        return "speed"
    return "normal"

def output_video(audio):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
            print("Loading audio...")
            if audio == "speed": # speeded up
                audio_video = AudioFileClip("output_speed.wav") # moviepy audio format 
            else: # no speed modification
                audio_video = AudioFileClip("output.wav") # moviepy audio format 
            
            print("Loading video...")
            video = VideoFileClip("./media/videos/videogen/480p15/GeneratedScene.mp4")

            print("Setting audio...")
            final_video = video.set_audio(audio_video)

            print("Writing video file...")
            final_video.write_videofile(temp_video.name, codec="libx264", audio_codec="aac", threads=2, fps=30)

            # Copy temporary file to final output
            import shutil
            shutil.copy(temp_video.name, "output_video.mp4")
        print("Video file written successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

