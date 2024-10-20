from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Title
        title = Text("Even and Odd Numbers").scale(1.2)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Even numbers
        even_numbers = VGroup(
            *[Integer(i).scale(0.8) for i in range(2, 12, 2)]
        ).arrange(RIGHT, buff=1.5)
        even_label = Text("Even Numbers").scale(0.8).next_to(even_numbers, UP)
        self.play(FadeIn(even_numbers))
        self.play(Write(even_label))
        self.wait(2)

        # Odd numbers
        odd_numbers = VGroup(
            *[Integer(i).scale(0.8) for i in range(1, 11, 2)]
        ).arrange(RIGHT, buff=1.5).next_to(even_numbers, DOWN, buff=1.5)
        odd_label = Text("Odd Numbers").scale(0.8).next_to(odd_numbers, UP)
        self.play(FadeIn(odd_numbers))
        self.play(Write(odd_label))
        self.wait(2)

        # Formulas
        even_formula = MathTex("2n").scale(0.8).next_to(even_numbers, DOWN, buff=1.5)
        odd_formula = MathTex("2n + 1").scale(0.8).next_to(odd_numbers, DOWN, buff=1.5)
        self.play(FadeIn(even_formula))
        self.wait(2)
        self.play(FadeIn(odd_formula))
        self.wait(2)

        # Fade out everything
        self.play(
            FadeOut(even_numbers),
            FadeOut(even_label),
            FadeOut(odd_numbers),
            FadeOut(odd_label),
            FadeOut(even_formula),
            FadeOut(odd_formula),
        )
        self.wait(1)
