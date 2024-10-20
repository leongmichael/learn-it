from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Title
        title = Text("One-Variable Equations:  Finding 'x'").scale(1.2)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Equation 1
        equation1 = MathTex("2x + 5 = 11")
        self.play(Write(equation1))
        self.wait(2)

        # Equation 2
        equation2 = MathTex("2x = 6").next_to(equation1, DOWN)
        self.play(Transform(equation1, equation2))
        self.wait(2)

        # Equation 3
        equation3 = MathTex("x = 3").next_to(equation2, DOWN)
        self.play(Transform(equation2, equation3))
        self.wait(2)

        self.play(FadeOut(equation3))
        self.wait(1)
