from manim import *
#CORRECAO HUMANA: foi removido um import que nao existe na versao atual do Manim. Em vez disso, usamos as classes de sólidos diretamente (Tetrahedron, Cube, etc.) que estão disponíveis no Manim

class PoliedrosEuler(ThreeDScene):
    def construct(self):
        poliedros = [
            ("Tetraedro", Tetrahedron(), 4, 6, 4),
            ("Cubo", Cube(), 8, 12, 6),
            ("Octaedro", Octahedron(), 6, 12, 8),
            ("Dodecaedro", Dodecahedron(), 20, 30, 12),
            ("Icosaedro", Icosahedron(), 12, 30, 12),
        ]

        self.set_camera_orientation(phi=65 * DEGREES, theta=30 * DEGREES)

        for nome, objeto, V, A, F in poliedros:
            titulo = Text(nome, font_size=40).to_edge(UP)
            self.play(FadeIn(titulo))

            self.play(Create(objeto))
            self.play(Rotate(objeto, angle=TAU, run_time=3))

            valores = VGroup(
                Text(f"V = {V}", color=YELLOW).to_corner(UL),
                Text(f"A = {A}", color=BLUE).next_to(ORIGIN, LEFT).shift(UP * 2),
                Text(f"F = {F}", color=RED).to_corner(UR),
            )

            self.play(FadeIn(valores))

            expressao = Text(f"{V} - {A} + {F}", font_size=50).to_edge(DOWN)
            resultado = Text("= 2", font_size=50, color=GREEN).next_to(expressao, RIGHT)

            self.play(Write(expressao))
            self.play(TransformMatchingShapes(expressao.copy(), resultado))
            self.wait(1)

            self.play(FadeOut(objeto), FadeOut(valores), FadeOut(titulo), FadeOut(expressao), FadeOut(resultado))

        formula_final = Text("Fórmula de Euler: V - A + F = 2", font_size=60, color=GREEN)
        self.play(Write(formula_final))
        self.wait(2)
        self.play(FadeOut(formula_final))
