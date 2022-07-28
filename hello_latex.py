from manim import *


class HelloLatex(Scene):
    def construct(self):
        hw = MathTex(r"Hell^{o}   Lat_{ex}   \alpha   \beta   \frac{\partial f}{\partial m}")
        self.play(Write(hw))
        self.wait(2)
