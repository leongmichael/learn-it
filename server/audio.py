from pydub import AudioSegment
from pydub.playback import play

# Load audio file
audio = AudioSegment.from_file("output.wav")

# Speed up
faster_audio = audio.speedup(playback_speed=2)


# Export the modified audio
faster_audio.export("output.wav", format="wav")
