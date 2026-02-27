from manim import *


class PoliedrosDePlataoEuler(ThreeDScene):
    def construct(self):
        # Título inicial
        title = Tex("Poliedros de Platão e a Fórmula de Euler", font_size=48)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES, distance=10)

        # Tetraedro
        self.show_polyhedron(
            nome="Tetraedro",
            poly_class=Tetrahedron,
            V=4,
            A=6,
            F=4,
            color=TEAL,
        )

        # Cubo
        self.show_polyhedron(
            nome="Cubo",
            poly_class=Cube,
            V=8,
            A=12,
            F=6,
            color=BLUE,
        )

        # Octaedro
        self.show_polyhedron(
            nome="Octaedro",
            poly_class=Octahedron,
            V=6,
            A=12,
            F=8,
            color=GREEN,
        )

        # Dodecaedro
        self.show_polyhedron(
            nome="Dodecaedro",
            poly_class=Dodecahedron,
            V=20,
            A=30,
            F=12,
            color=ORANGE,
        )

        # Icosaedro
        self.show_polyhedron(
            nome="Icosaedro",
            poly_class=Icosahedron,
            V=12,
            A=30,
            F=20,
            color=PURPLE,
        )

        # Síntese final da fórmula de Euler
        self.set_camera_orientation(phi=70 * DEGREES, theta=45 * DEGREES, distance=12)

        euler_formula = MathTex(
            "V - A + F = 2",
            font_size=60,
            tex_to_color_map={"V": YELLOW, "A": RED, "F": GREEN, "2": BLUE},
        )
        self.add_fixed_in_frame_mobjects(euler_formula)
        self.play(Write(euler_formula))
        self.wait(0.5)

        # Pequenos poliedros ao redor para a síntese
        tetra = Tetrahedron()
        cube = Cube()
        octa = Octahedron()
        dodeca = Dodecahedron()
        icosa = Icosahedron()

        small_scale = 0.7
        for poly, color in [
            (tetra, TEAL),
            (cube, BLUE),
            (octa, GREEN),
            (dodeca, ORANGE),
            (icosa, PURPLE),
        ]:
            poly.set_fill(color, opacity=0.8)
            poly.set_stroke(WHITE, width=1)
            poly.scale(small_scale)

        # Disposição em linha abaixo da fórmula
        tetra.shift(LEFT * 6 + DOWN * 2)
        cube.shift(LEFT * 3 + DOWN * 2)
        octa.shift(DOWN * 2)
        dodeca.shift(RIGHT * 3 + DOWN * 2)
        icosa.shift(RIGHT * 6 + DOWN * 2)

        poly_group = VGroup(tetra, cube, octa, dodeca, icosa)
        self.play(FadeIn(poly_group, shift=UP))
        self.wait(0.5)

        self.begin_ambient_camera_rotation(rate=0.15)
        self.play(
            LaggedStart(
                Rotate(tetra, angle=PI / 3, axis=UP),
                Rotate(cube, angle=PI / 3, axis=UP),
                Rotate(octa, angle=PI / 3, axis=UP),
                Rotate(dodeca, angle=PI / 3, axis=UP),
                Rotate(icosa, angle=PI / 3, axis=UP),
                lag_ratio=0.2,
            ),
            run_time=4,
        )
        self.stop_ambient_camera_rotation()

        self.play(Indicate(euler_formula, scale_factor=1.1), run_time=2)
        self.wait(2)

        self.play(FadeOut(poly_group), FadeOut(euler_formula))
        self.wait(1)

    def show_polyhedron(self, nome, poly_class, V, A, F, color):
        poly = poly_class()
        poly.set_fill(color, opacity=0.8)
        poly.set_stroke(WHITE, width=1)
        poly.scale(1.8)

        nome_tex = Tex(nome, font_size=40)
        nome_tex.to_corner(UL).shift(DOWN * 0.3)

        V_tex = MathTex(f"V = {V}", font_size=36)
        A_tex = MathTex(f"A = {A}", font_size=36)
        F_tex = MathTex(f"F = {F}", font_size=36)

        V_tex.next_to(nome_tex, DOWN, aligned_edge=LEFT)
        A_tex.next_to(V_tex, DOWN, aligned_edge=LEFT)
        F_tex.next_to(A_tex, DOWN, aligned_edge=LEFT)

        self.add_fixed_in_frame_mobjects(nome_tex, V_tex, A_tex, F_tex)

        self.begin_ambient_camera_rotation(rate=0.2)

        self.play(FadeIn(poly, scale=0.5), Write(nome_tex))
        self.play(Write(V_tex), Write(A_tex), Write(F_tex))
        self.wait(0.5)

        self.play(Rotate(poly, angle=PI / 4, axis=UP), run_time=2)
        self.play(Rotate(poly, angle=PI / 6, axis=RIGHT), run_time=2)

        expr_symbolic = MathTex("V - A + F", font_size=40)
        expr_symbolic.to_edge(DOWN)
        self.add_fixed_in_frame_mobjects(expr_symbolic)
        self.play(Write(expr_symbolic))
        self.wait(0.5)

        expr_numeric = MathTex(f"{V} - {A} + {F}", font_size=40)
        expr_numeric.move_to(expr_symbolic)
        self.add_fixed_in_frame_mobjects(expr_numeric)
        self.play(TransformMatchingTex(expr_symbolic, expr_numeric))
        self.wait(0.5)

        expr_result = MathTex(f"{V} - {A} + {F} = 2", font_size=40)
        expr_result.move_to(expr_numeric)
        self.add_fixed_in_frame_mobjects(expr_result)
        self.play(TransformMatchingTex(expr_numeric, expr_result))
        self.play(expr_result.animate.set_color(YELLOW))
        self.wait(1.5)

        self.stop_ambient_camera_rotation()

        self.play(
            FadeOut(expr_result),
            FadeOut(nome_tex, V_tex, A_tex, F_tex),
            FadeOut(poly),
        )
        self.wait(0.5)