from manim import *


class ShadowTesseract(ThreeDScene):
    config.background_color = YELLOW_C

    def construct(self):

        g = NumberPlane()
        # self.add(g)

        axes = ThreeDAxes().set_color(BLACK)
        s1 = Square().set_color(BLACK).scale(1.5).move_to(1 * LEFT + 1 * DOWN)
        s2 = Square().set_color(BLACK).scale(1.5).move_to(1 * RIGHT + 1 * UP)

        l1 = Line(start=0.5 * UP + 2.5 * LEFT, end=0.5 * LEFT + 2.5 * UP).set_color(
            BLACK
        )
        l2 = Line(start=2.5 * DOWN + 2.5 * LEFT, end=0.5 * LEFT + 0.5 * DOWN).set_color(
            BLACK
        )
        l3 = Line(end=2.5 * UP + 2.5 * RIGHT, start=0.5 * RIGHT + 0.5 * UP).set_color(
            BLACK
        )
        l4 = Line(
            start=0.5 * RIGHT + 2.5 * DOWN, end=0.5 * DOWN + 2.5 * RIGHT
        ).set_color(BLACK)

        c = Cube().set_color(BLACK)

        c1 = Cube().move_to(2 * DOWN)
        c2 = Cube().move_to(2.5 * UP)
        c1.set_z(-1)
        c2.set_z(2)

        line3d1 = Line3D(start=np.array([-1, -1, 0]), end=np.array([-1, 3.5, 3]))
        line3d2 = Line3D(start=np.array([-1, -3, 0]), end=np.array([-1, 1.5, 3]))
        line3d3 = Line3D(start=np.array([1, -1, 0]), end=np.array([1, 3.5, 3]))
        line3d4 = Line3D(start=np.array([1, -3, 0]), end=np.array([1, 1.5, 3]))
        line3d5 = Line3D(start=np.array([-1, -1, -2]), end=np.array([-1, 3.5, 1]))
        line3d6 = Line3D(start=np.array([-1, -3, -2]), end=np.array([-1, 1.5, 1]))
        line3d7 = Line3D(start=np.array([1, -1, -2]), end=np.array([1, 3.5, 1]))
        line3d8 = Line3D(start=np.array([1, -3, -2]), end=np.array([1, 1.5, 1]))

        self.play(Write(s1))
        self.play(Write(s2))
        self.wait(2)
        self.play(
            Write(l1),
            Write(l2),
            Write(l3),
            Write(l4),
        )
        self.wait(2)

        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(4)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.play(Create(axes))
        self.wait(4)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(4)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.wait(2)
        self.play(
            FadeOut(axes),
            FadeOut(s1),
            FadeOut(s2),
            FadeOut(l1),
            FadeOut(l2),
            FadeOut(l3),
            FadeOut(l4),
        )
        self.wait()
        self.play(Create(c))
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(4)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.play(Create(axes))
        self.wait(4)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(4)
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        self.wait(2)
        self.play(
            FadeOut(c),
        )
        self.wait(2)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(2)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.play(Create(c1), Create(c2))
        self.wait(5)
        self.play(
            Write(line3d1, run_time=2),
            Write(line3d2, run_time=2),
            Write(line3d3, run_time=2),
            Write(line3d4, run_time=2),
            # Write(c2),
            Write(line3d5, run_time=2),
            Write(line3d6, run_time=2),
            Write(line3d7, run_time=2),
            Write(line3d8, run_time=2),
            # Write(c2)
        )
        self.wait(10)


class BuildingTesseract(Scene):
    config.background_color = YELLOW_C

    def construct(self):

        d1 = Dot().move_to(2 * LEFT).set_color(BLACK)
        d2 = Dot().move_to(2 * RIGHT).set_color(BLACK)

        l1 = Line(start=2 * LEFT, end=2 * RIGHT).set_color(BLACK)
        l2 = Line(start=2 * LEFT, end=2 * RIGHT).move_to(2 * UP).set_color(BLACK)
        l3 = Line(start=2 * DOWN, end=2 * UP).move_to(2 * RIGHT).set_color(BLACK)
        l4 = Line(start=2 * DOWN, end=2 * UP).move_to(2 * LEFT).set_color(BLACK)
        l5 = Line(start=2 * LEFT, end=2 * RIGHT).move_to(2 * DOWN).set_color(BLACK)

        s1 = Square().set_color(BLACK).scale(1.5).move_to(1 * LEFT + 1 * DOWN)
        s2 = Square().set_color(BLACK).scale(1.5).move_to(1 * RIGHT + 1 * UP)

        l21 = Line(start=0.5 * UP + 2.5 * LEFT, end=0.5 * LEFT + 2.5 * UP).set_color(
            BLACK
        )
        l22 = Line(
            start=2.5 * DOWN + 2.5 * LEFT, end=0.5 * LEFT + 0.5 * DOWN
        ).set_color(BLACK)
        l23 = Line(end=2.5 * UP + 2.5 * RIGHT, start=0.5 * RIGHT + 0.5 * UP).set_color(
            BLACK
        )
        l24 = Line(
            start=0.5 * RIGHT + 2.5 * DOWN, end=0.5 * DOWN + 2.5 * RIGHT
        ).set_color(BLACK)

        self.play(Write(d1), Write(d2))
        self.wait(2)
        self.play(Write(l1), FadeOut(d1), FadeOut(d2))
        self.wait(2)
        self.play(ReplacementTransform(l1, l2))
        self.play(Write(l3), Write(l4), Write(l5))
        self.wait(2)
        self.play(FadeOut(l2), FadeOut(l3), FadeOut(l4), FadeOut(l5))
        self.play(Write(s1))
        self.play(Write(s2))
        self.wait(2)
        self.play(
            Write(l21),
            Write(l22),
            Write(l23),
            Write(l24),
        )
        self.wait(2)


class Tess(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes().set_color(BLACK)
        self.play(Create(axes))
        self.wait(2)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.play(Write(Cube(fill_opacity=0, stroke_width=2).scale(2).set_color(BLACK)))
        self.wait(5)
        self.play(Write(Cube(fill_opacity=0, stroke_width=2).set_color(BLACK)))
        self.wait(5)
        l1 = Line3D(start=np.array([-2, -2, -2]), end=np.array([-1, -1, -1]))
        l2 = Line3D(start=np.array([2, 2, 2]), end=np.array([1, 1, 1]))
        l3 = Line3D(start=np.array([-2, -2, 2]), end=np.array([-1, -1, 1]))
        l4 = Line3D(start=np.array([-2, 2, -2]), end=np.array([-1, 1, -1]))
        l5 = Line3D(start=np.array([2, -2, -2]), end=np.array([1, -1, -1]))
        l6 = Line3D(start=np.array([2, 2, -2]), end=np.array([1, 1, -1]))
        l7 = Line3D(start=np.array([-2, 2, 2]), end=np.array([-1, 1, 1]))
        l8 = Line3D(start=np.array([2, -2, 2]), end=np.array([1, -1, 1]))
        self.play(
            Write(l1),
            Write(l2),
            Write(l3),
            Write(l4),
            Write(l5),
            Write(l6),
            Write(l7),
            Write(l8),
        )
        self.wait(5)


class TwoDCreature(ThreeDScene):
    config.background_color = YELLOW_C

    def construct(self):

        axes = ThreeDAxes().set_color(BLACK)

        l1 = Line().scale(2).set_color(BLACK).rotate(PI / 2).move_to(4 * LEFT)
        l2 = Line().scale(2).set_color(BLACK).move_to(2 * UP + 2 * LEFT)
        l3 = Line().scale(2).set_color(BLACK).move_to(2 * DOWN + 2 * LEFT)
        l4 = (
            Line()
            .scale(2)
            .set_color(BLACK)
            .rotate(PI / 4)
            .move_to(1.4 * RIGHT + 0.6 * DOWN)
        )

        home = Tex("Home").move_to(2 * LEFT).set_color(BLACK)
        you = Tex("You").move_to(RIGHT + 2 * UP).set_color(BLACK)
        circ = Circle(radius=0.25).set_color(BLACK).move_to(RIGHT + UP)

        sph = Sphere().move_to(RIGHT + UP).set_z(2)

        self.play(
            Write(l1),
            Write(l2),
            Write(l3),
            Write(l4),
        )

        self.play(Write(home))
        self.wait(2)
        self.play(Write(circ), Write(you))
        self.play(circ.animate.shift(UP))
        self.wait()
        self.play(circ.animate.shift(2 * DOWN))
        self.wait()
        self.play(circ.animate.shift(UP))
        self.wait()
        self.play(circ.animate.shift(LEFT))
        self.wait()
        self.play(circ.animate.shift(2 * RIGHT))
        self.wait()
        self.play(circ.animate.shift(LEFT))
        self.wait(2)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(2)
        self.play(Create(axes))
        self.wait(2)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(3)
        self.play(Write(sph))
        self.wait(2)
        self.play(sph.animate.set_z(1))
        self.wait(4)
        self.play(sph.animate.set_z(2), circ.animate.set_z(1))
        self.wait(4)
        self.play(circ.animate.set_z(0))
        self.wait(3)


class WAxis(ThreeDScene):
    config.background_color = YELLOW_C

    def construct(self):

        axes = ThreeDAxes().set_color(BLACK)
        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.wait(2)
        self.play(Create(axes))
        self.wait(2)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.play(Write(Line3D(start=np.array([-3, -3, -3]), end=np.array([3, 3, 3]))))
        self.wait(8)
