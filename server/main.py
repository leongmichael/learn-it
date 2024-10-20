from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import re

from gemini import enter_prompt
from tts import tts


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
    # response = enter_prompt(prompt)
    response = '''
{
"script": "Parabolas! They're those smooth, U-shaped curves you see all around.  From the arc of a basketball shot to the shape of a satellite dish, parabolas are everywhere.

What makes parabolas so special?  It all comes down to a simple but powerful relationship:  every point on a parabola is the same distance from a special point called the focus as it is from a line called the directrix. 

Imagine a satellite dish. The focus is at the center of the dish, and the directrix is a line parallel to the opening of the dish. The curve of the dish itself is the parabola.  Signals from all directions hit the dish and are reflected towards the focus, where they are collected. This is because of that unique property of parabolas - the right angle formed by lines drawn from the focus to a point on the parabola and then down to the directrix.

Parabolas also appear in the equations we use in math. The simplest parabola is described by the equation y = x^2. If you flip the sign to y = -x^2, the parabola flips downwards. 

So, next time you see a U-shaped curve, remember it might be a parabola, a hidden world of elegant math and real-world applications waiting to be explored!",
"code": "from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Title
        title = Text("Parabolas:  Curves with a Purpose").scale(1.2)
        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))

        # Axes
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-2, 10, 2],
            x_length=10,
            y_length=8,
            axis_config={"include_numbers": True, "label_direction": UP},
        )
        axes.add_coordinates()
        self.play(Create(axes))
        self.wait(2)

        # Parabola
        parabola = axes.plot(lambda x: x**2, x_range=[-3, 3], color=BLUE)
        parabola_label = MathTex(r'y = x^2').next_to(parabola, UP, buff=0.5)
        self.play(Create(parabola))
        self.play(Write(parabola_label))
        self.wait(2)

        # Focus and directrix
        focus = Dot(color=RED).move_to(axes.coords_to_point(0, 1, 0))
        focus_label = MathTex(r'Focus').next_to(focus, RIGHT)
        directrix = Line(start=axes.coords_to_point(-5, -1, 0), end=axes.coords_to_point(5, -1, 0)).set_color(YELLOW)
        directrix_label = MathTex(r'Directrix').next_to(directrix, DOWN)
        self.play(Create(focus))
        self.play(Write(focus_label))
        self.wait(2)
        self.play(Create(directrix))
        self.play(Write(directrix_label))
        self.wait(2)

        # Show right angle
        point = axes.coords_to_point(2, 4, 0)
        line_to_focus = Line(point, focus).set_color(GREEN)
        line_to_directrix = Line(point, [point[0], -1, 0]).set_color(GREEN)
        right_angle = RightAngle(line_to_focus, line_to_directrix, length=0.2).set_color(GREEN)
        self.play(Create(line_to_focus))
        self.play(Create(line_to_directrix))
        self.play(Create(right_angle))
        self.wait(2)

        # Fade out elements
        self.play(FadeOut(right_angle), FadeOut(line_to_focus), FadeOut(line_to_directrix), FadeOut(parabola), FadeOut(parabola_label), FadeOut(focus), FadeOut(focus_label), FadeOut(directrix), FadeOut(directrix_label))
        self.wait(1)
"
}
content_copy
Use code with caution.
Json

I've worked on making the script a little more concise and engaging, and I've adjusted the timing. The code remains the same, as the visual elements are still relevant.

Let me know if the timing is closer to 28 seconds this time!
'''
    
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

    
    print(script)



    return {"prompt": prompt}
