from manim import *

class PapelCoeficientesQuadratica(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            tips=False
        )
        labels = axes.get_axis_labels("x", "y")
        self.play(Create(axes), Write(labels))

        a_tracker = ValueTracker(1)
        b_tracker = ValueTracker(0)
        c_tracker = ValueTracker(0)

        def quadratica(x):
            return a_tracker.get_value() * x**2 + b_tracker.get_value() * x + c_tracker.get_value()

        graph = always_redraw(lambda: axes.plot(quadratica, color=YELLOW))

        titulo = always_redraw(
            lambda: Text(
                f"f(x) = {a_tracker.get_value():.1f}x² + {b_tracker.get_value():.1f}x + {c_tracker.get_value():.1f}",
                font_size=32
            ).to_edge(UP)
        )

        self.play(Create(graph), FadeIn(titulo))
        self.wait(1)

        # Variando 'a'
        self.play(a_tracker.animate.set_value(2), run_time=2)
        self.wait(0.5)
        self.play(a_tracker.animate.set_value(-1), run_time=2)
        self.wait(0.5)
        self.play(a_tracker.animate.set_value(1), run_time=2)
        self.wait(1)

        # Variando 'b'
        self.play(b_tracker.animate.set_value(2), run_time=2)
        self.wait(0.5)
        self.play(b_tracker.animate.set_value(-2), run_time=2)
        self.wait(0.5)
        self.play(b_tracker.animate.set_value(0), run_time=2)
        self.wait(1)

        # Variando 'c'
        self.play(c_tracker.animate.set_value(2), run_time=2)
        self.wait(0.5)
        self.play(c_tracker.animate.set_value(-2), run_time=2)
        self.wait(0.5)
        self.play(c_tracker.animate.set_value(0), run_time=2)
        self.wait(1)

        self.play(FadeOut(graph), FadeOut(titulo), FadeOut(axes), FadeOut(labels))