import sys
from gemini import enter_prompt
from tts import tts
from videoediting import speed_up_audio, output_video, delete_media
import re
import time
import subprocess

def process_prompt(prompt):
    print("running")
    response = enter_prompt(prompt)

    script = ""
    code = ""

    find_code = re.search(r'"code":\s*"(.*?)"\s*}', response, re.DOTALL)
    if find_code:
        code = find_code.group(1)
        # Unescape the escaped quotes and backslashes
        code = code.encode().decode('unicode_escape')
    else:
        print("code not found")
    
    find_script = re.search(r'"script":\s*"(.*?)",\s*"code":', response, re.DOTALL)
    if find_script:
        script = find_script.group(1)
        # Unescape the escaped quotes and backslashes
        script = script.encode().decode('unicode_escape')
    else:
        print("script not found")


    # text to speech
    tts(script)

    # write generated code to python file
    with open('videogen.py', 'w') as file:
        file.write(code)

    # run terminal script to generate manim video
    try:
        command = "manim videogen.py GeneratedScene -ql"
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # Get the output and error (if any)
        output = result.stdout.decode()
        error = result.stderr.decode()

        print("Output:\n", output)
        if error:
            print("Error:\n", error)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

    
    speed = speed_up_audio()
    time.sleep(0.5)
    output_video(speed)
    delete_media()
    
    return {"prompt": prompt}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
        process_prompt(prompt)
