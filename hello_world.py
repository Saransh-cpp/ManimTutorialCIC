from manim import *


class HelloWorld(Scene):
    def construct(self):
        hw = Text('Hello World!')
        self.play(Write(hw)) # run_time in Write
        self.wait(2)
