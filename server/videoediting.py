from pydub import AudioSegment
from pydub.playback import play
from moviepy.editor import VideoFileClip


# Load audio file
audio = AudioSegment.from_file("output.wav")
audio_duration = len(audio) // 1000 # seconds

video = VideoFileClip("./media/videos/videogen/480p15/GeneratedScene.mp4")
video_duration = int(video.duration) # seconds


def speed_up_audio():
    if audio_duration > video_duration:
        factor = audio_duration / video_duration
        faster_audio = audio.speedup(playback_speed=factor)
        faster_audio.export("output.wav", format="wav")
