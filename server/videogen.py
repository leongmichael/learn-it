from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Title
        title = Text("Parabolas: A Curve of Elegance and Function").scale(1.2)
        self.play(Write(title))
        self.wait(1)
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
