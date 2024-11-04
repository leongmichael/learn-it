from manim import *

class GeneratedScene(Scene):
    def construct(self):
        # Title
        title = Text("Optimization: Finding the Best").scale(1.2)
        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title))

        # Mountain graphic
        mountain = SVGMobject("mountain.svg").scale(0.8)
        self.play(FadeIn(mountain))
        self.wait(2)

        # Highlight peak
        peak = Dot(color=RED).move_to(mountain.get_top())
        self.play(Create(peak))
        self.wait(2)

        # Fade out mountain
        self.play(FadeOut(mountain), FadeOut(peak))
        self.wait(1)

        # Route graphic
        route = SVGMobject("route.svg").scale(0.7)
        self.play(FadeIn(route))
        self.wait(2)

        # Highlight fastest path
        fastest_path = Line(route.get_corner(DL), route.get_corner(UR), color=GREEN).set_stroke(width=4)
        self.play(Create(fastest_path))
        self.wait(2)

        # Fade out route
        self.play(FadeOut(route), FadeOut(fastest_path))
        self.wait(1)
