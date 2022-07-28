from manim import *


class Intro(Scene):
    def construct(self):
        circ = Circle().move_to(2 * LEFT)
        g = NumberPlane()

        self.play(Create(g))
        self.wait()
        self.play(Create(circ, run_time=2))

        arr = Arrow().scale(0.75).move_to(2 * RIGHT).next_to(circ, RIGHT, buff=0.5)
        txt = Text('This is a circle!').scale(0.5).next_to(arr, RIGHT, buff=0.5)

        self.play(Create(arr, run_time=2))
        self.play(Write(txt))
        self.wait()
        self.play(FadeOut(g))
        self.wait(2)
        self.play(circ.animate.shift(RIGHT))
        self.play(circ.animate.shift(2 * LEFT))
        self.play(circ.animate.shift(RIGHT))
        self.wait(2)

        rect = Square().move_to(2 * LEFT)
        newtxt = Text("Now a square!").scale(0.5).next_to(arr, RIGHT, buff=0.5)

        self.play(ReplacementTransform(circ, rect))
        self.play(ReplacementTransform(txt, newtxt))

        framebox1 = SurroundingRectangle(rect, buff = .1)
        framebox2 = SurroundingRectangle(arr, buff = .1)
        framebox3 = SurroundingRectangle(newtxt, buff = .1)
        self.play(Create(framebox1))
        self.wait()
        self.play(ReplacementTransform(framebox1,framebox2))
        self.wait()
        self.play(ReplacementTransform(framebox2,framebox3))
        self.wait()

        self.play(FadeOut(rect), FadeOut(arr), FadeOut(newtxt), FadeOut(framebox3))

        self.wait()

        self.play(GrowFromCenter(Text("The END!")))
