from manim import *

class MyScene(Scene):
    def construct(self):
        circle = Circle(radius=1)
        self.play(GrowFromPoint(circle, ORIGIN), run_time=1)
        self.play(FadeOut(circle), run_time=0.5)
