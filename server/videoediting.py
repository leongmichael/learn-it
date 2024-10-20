from pydub import AudioSegment
from pydub.playback import play
from moviepy.editor import VideoFileClip, AudioFileClip


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
    if audio == "speed": # speeded up
        audio_video = AudioFileClip("output_speed.wav") # moviepy audio format 
    else: # no speed modification
        audio_video = AudioFileClip("output.wav") # moviepy audio format 
    final_video = video.set_audio(audio_video)
    final_video.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac")

