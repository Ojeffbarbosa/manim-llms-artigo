from manim import *


class PapelDosCoeficientesDaFuncaoQuadratica(Scene):
    def construct(self):
        # Configuração dos eixos
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-4, 10, 1],
            x_length=10,
            y_length=6,
            axis_config={"include_numbers": True},
        )
        axes.to_edge(DOWN)
        axis_labels = axes.get_axis_labels(
            x_label=MathTex("x"),
            y_label=MathTex("f(x)")
        )

        self.play(Create(axes), run_time=2)
        self.play(Write(axis_labels))
        self.wait(0.5)

        # Trackers dos coeficientes
        a_tracker = ValueTracker(1.0)
        b_tracker = ValueTracker(0.0)
        c_tracker = ValueTracker(0.0)

        # Gráfico da função quadrática
        def get_quadratic_graph():
            a = a_tracker.get_value()
            b = b_tracker.get_value()
            c = c_tracker.get_value()
            return axes.plot(
                lambda x: a * x**2 + b * x + c,
                x_range=[-6, 6],
                color=RED,
            )

        quadratic_graph = always_redraw(get_quadratic_graph)

        # Fórmula geral f(x) = ax^2 + bx + c
        formula = MathTex(
            "f(x) = ",
            "a",
            "x^2",
            "+",
            "b",
            "x",
            "+",
            "c",
        )
        formula.to_edge(UP)
        formula[1].set_color(YELLOW)  # a
        formula[4].set_color(BLUE)    # b
        formula[7].set_color(GREEN)   # c

        # Valores numéricos dos coeficientes
        a_label = MathTex("a = ").set_color(YELLOW)
        a_value = always_redraw(
            lambda: DecimalNumber(
                a_tracker.get_value(),
                num_decimal_places=1,
                include_sign=True,
                color=YELLOW,
            )
        )
        a_group = VGroup(a_label, a_value).arrange(RIGHT, buff=0.1)
        a_group.next_to(formula, DOWN, aligned_edge=LEFT, buff=0.3)

        b_label = MathTex("b = ").set_color(BLUE)
        b_value = always_redraw(
            lambda: DecimalNumber(
                b_tracker.get_value(),
                num_decimal_places=1,
                include_sign=True,
                color=BLUE,
            )
        )
        b_group = VGroup(b_label, b_value).arrange(RIGHT, buff=0.1)
        b_group.next_to(a_group, DOWN, aligned_edge=LEFT)

        c_label = MathTex("c = ").set_color(GREEN)
        c_value = always_redraw(
            lambda: DecimalNumber(
                c_tracker.get_value(),
                num_decimal_places=1,
                include_sign=True,
                color=GREEN,
            )
        )
        c_group = VGroup(c_label, c_value).arrange(RIGHT, buff=0.1)
        c_group.next_to(b_group, DOWN, aligned_edge=LEFT)

        # Vértice da parábola
        def get_vertex_point():
            a = a_tracker.get_value()
            b = b_tracker.get_value()
            c = c_tracker.get_value()
            if abs(a) < 1e-6:
                x_v = 0
            else:
                x_v = -b / (2 * a)
            y_v = a * x_v**2 + b * x_v + c
            return axes.c2p(x_v, y_v)

        vertex_dot = always_redraw(
            lambda: Dot(
                get_vertex_point(),
                color=ORANGE,
                radius=0.06,
            )
        )
        vertex_label = always_redraw(
            lambda: MathTex("V", color=ORANGE)
            .scale(0.6)
            .next_to(vertex_dot, UP, buff=0.1)
        )

        # Introdução do gráfico e textos
        self.play(Create(quadratic_graph), run_time=2)
        self.play(
            Write(formula),
            FadeIn(a_group, shift=UP * 0.2),
            FadeIn(b_group, shift=UP * 0.2),
            FadeIn(c_group, shift=UP * 0.2),
            run_time=2,
        )
        self.play(
            FadeIn(vertex_dot, scale=0.5),
            FadeIn(vertex_label, shift=UP * 0.1),
        )
        self.wait(1)

        # VARIAÇÃO DO COEFICIENTE a (abertura e concavidade)
        self.play(
            Indicate(formula[1], scale_factor=1.2),
            Indicate(a_group, scale_factor=1.05),
            run_time=1.5,
        )

        # a maior: parábola mais "fechada"
        self.play(a_tracker.animate.set_value(2.5), run_time=3)
        self.wait(0.5)

        # a menor (entre 0 e 1): parábola mais "aberta"
        self.play(a_tracker.animate.set_value(0.5), run_time=3)
        self.wait(0.5)

        # a negativo: concavidade para baixo
        self.play(a_tracker.animate.set_value(-1.5), run_time=3)
        self.wait(1)

        # Volta para a = 1
        self.play(a_tracker.animate.set_value(1.0), run_time=2)
        self.wait(1)

        # VARIAÇÃO DO COEFICIENTE b (deslocamento horizontal e vértice)
        self.play(
            Indicate(formula[4], scale_factor=1.2),
            Indicate(b_group, scale_factor=1.05),
            Indicate(vertex_dot, scale_factor=1.3),
            run_time=1.5,
        )

        # b positivo: vértice se desloca horizontalmente (e a parábola "inclina")
        self.play(b_tracker.animate.set_value(4.0), run_time=3)
        self.wait(0.5)

        # b negativo: vértice vai para o outro lado
        self.play(b_tracker.animate.set_value(-4.0), run_time=3)
        self.wait(0.5)

        # Volta para b = 0
        self.play(b_tracker.animate.set_value(0.0), run_time=3)
        self.wait(1)

        # VARIAÇÃO DO COEFICIENTE c (deslocamento vertical)
        self.play(
            Indicate(formula[7], scale_factor=1.2),
            Indicate(c_group, scale_factor=1.05),
            run_time=1.5,
        )

        # c positivo: parábola sobe
        self.play(c_tracker.animate.set_value(3.0), run_time=3)
        self.wait(0.5)

        # c negativo: parábola desce
        self.play(c_tracker.animate.set_value(-2.0), run_time=3)
        self.wait(0.5)

        # Volta para c = 0
        self.play(c_tracker.animate.set_value(0.0), run_time=3)
        self.wait(1)

        # Encerramento
        self.wait(2)