from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import re

from gemini import enter_prompt
from tts import tts
from videoediting import speed_up_audio, output_video

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


# http://127.0.0.1:8000/

@app.get("/")
def read_root():
    return {"Hello": "World"}


# TODO: error handling at each step

'''
Steps:
1. gather prompt
2. pass prompt into gemini
3. parse result to 2 separate variables: script and code
4. generate the video 
5. generate the tts script
6. speed up script so that it is same length as the video 
7. add together with pymovie?
8. save to folder
9. frontend displays video 
'''
@app.get("/prompt/{prompt}")
def read_prompt(prompt: str):
    # print(prompt)
    print("running")
    response = enter_prompt(prompt)
#     response = '''

# {
# "script": "A parabola.  It's a U-shaped curve.  Here's a parabola on a graph, represented by the equation y equals x squared.  

# Notice the special point called the focus, inside the curve.  And here's the directrix, a line outside the curve.  

# Every point on the parabola is the same distance from the focus as it is from the directrix.  Look at this line, from the focus to a point on the parabola, and then down to the directrix.  They form a right angle.

# Parabolas are useful for focusing energy.  Think about satellite dishes.  They're shaped like parabolas, with the focus at the center. Signals from all directions are reflected towards the focus.

# That's a quick look at parabolas!  They're a lot more fascinating than they seem at first.",
# "code": "from manim import *

# class GeneratedScene(Scene):
#     def construct(self):
#         # Title
#         title = Text("Parabolas:  A Journey into Curves").scale(1.2)
#         self.play(Write(title))
#         self.wait(3)
#         self.play(FadeOut(title))

#         # Axes
#         axes = Axes(
#             x_range=[-5, 5, 1],
#             y_range=[-2, 10, 2],
#             x_length=10,
#             y_length=8,
#             axis_config={"include_numbers": True, "label_direction": UP},
#         )
#         axes.add_coordinates()
#         self.play(Create(axes))
#         self.wait(2)

#         # Parabola
#         parabola = axes.plot(lambda x: x**2, x_range=[-3, 3], color=BLUE)
#         parabola_label = MathTex(r'y = x^2').next_to(parabola, UP, buff=0.5)
#         self.play(Create(parabola))
#         self.play(Write(parabola_label))
#         self.wait(2)

#         # Focus and directrix
#         focus = Dot(color=RED).move_to(axes.coords_to_point(0, 1, 0))
#         focus_label = MathTex(r'Focus').next_to(focus, RIGHT)
#         directrix = Line(start=axes.coords_to_point(-5, -1, 0), end=axes.coords_to_point(5, -1, 0)).set_color(YELLOW)
#         directrix_label = MathTex(r'Directrix').next_to(directrix, DOWN)
#         self.play(Create(focus))
#         self.play(Write(focus_label))
#         self.wait(2)
#         self.play(Create(directrix))
#         self.play(Write(directrix_label))
#         self.wait(2)

#         # Show right angle
#         point = axes.coords_to_point(2, 4, 0)
#         line_to_focus = Line(point, focus).set_color(GREEN)
#         line_to_directrix = Line(point, [point[0], -1, 0]).set_color(GREEN)
#         right_angle = RightAngle(line_to_focus, line_to_directrix, length=0.2).set_color(GREEN)
#         self.play(Create(line_to_focus))
#         self.play(Create(line_to_directrix))
#         self.play(Create(right_angle))
#         self.wait(2)

#         # Fade out elements
#         self.play(FadeOut(right_angle), FadeOut(line_to_focus), FadeOut(line_to_directrix), FadeOut(parabola), FadeOut(parabola_label), FadeOut(focus), FadeOut(focus_label), FadeOut(directrix), FadeOut(directrix_label))
#         self.wait(1)
# "
# }
# content_copy
# Use code with caution.
# Json

# I've made the script more concise and focused on the visual elements in the animation. Let me know what you think!

# '''

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
    output_video(speed)
    
    return {"prompt": prompt}
