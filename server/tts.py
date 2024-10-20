import os
import yaml

from deepgram import (
    DeepgramClient,
    SpeakOptions,
)

script_dir = os.path.dirname(__file__)
config_path = os.path.join(script_dir, "keys.yaml")

try:
    with open(config_path, 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)
except Exception as e:
    print("Keys file not found")
key = cfg.get('deepgram')


filename = "output.wav"

def tts(text):
    try:
        # STEP 1: Create a Deepgram client using the API key from environment variables
        deepgram = DeepgramClient(api_key=key)

        # STEP 2: Configure the options (such as model choice, audio configuration, etc.)
        options = SpeakOptions(
            model="aura-asteria-en",
            encoding="linear16",
            container="wav",
        )

        # STEP 3: Call the save method on the speak property
        response = deepgram.speak.v("1").save(filename, {"text": text}, options)
        print(response.to_json(indent=4))

    except Exception as e:
        print(f"Exception: {e}")

