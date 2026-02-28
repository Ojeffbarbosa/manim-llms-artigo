from manim import *
import numpy as np


class TeoremaDePitagorasComDecomposicaoDeAreas(Scene):
    def construct(self):
        # ── Título ──
        title = Text("Teorema de Pitágoras", font_size=48).to_edge(UP)
        self.play(Write(title))


        S = 0.55
        OFFSET = np.array([-1.0, -1.0, 0.0])

        A = np.array([0.0, 0.0, 0.0]) * S + OFFSET
        B = np.array([4.0, 0.0, 0.0]) * S + OFFSET
        C = np.array([0.0, 3.0, 0.0]) * S + OFFSET

        # Lados do triângulo
        side_ab = Line(A, B)
        side_bc = Line(B, C)
        side_ca = Line(C, A)
        triangle = VGroup(side_ab, side_bc, side_ca).set_stroke(WHITE, width=3)

        # Marca de ângulo reto em A
        right_angle = RightAngle(side_ab, side_ca, length=0.2, quadrant=(1, -1), stroke_width=2)

        # Vértices
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_C = Dot(C, color=WHITE)
        label_A = Text("A", font_size=24).next_to(dot_A, DOWN + LEFT, buff=0.1)
        label_B = Text("B", font_size=24).next_to(dot_B, DOWN + RIGHT, buff=0.1)
        label_C = Text("C", font_size=24).next_to(dot_C, UP + LEFT, buff=0.1)

        # Labels genéricos dos lados (a, b, c) — posicionados FORA do triângulo
        label_a = MathTex("a", font_size=36, color=GREEN).next_to(side_ca, LEFT, buff=0.15)
        label_b = MathTex("b", font_size=36, color=BLUE).next_to(side_ab, DOWN, buff=0.15)
        label_c = MathTex("c", font_size=36, color=YELLOW).move_to(
            side_bc.get_center() + np.array([0.25, 0.2, 0])
        )

        # ── PASSO 0: Apresentar o triângulo retângulo ──
        self.play(
            Create(triangle),
            FadeIn(dot_A, dot_B, dot_C),
            FadeIn(label_A, label_B, label_C),
        )
        self.play(Create(right_angle))
        self.play(FadeIn(label_a, label_b, label_c))
        self.wait(1.5)

        # Quadrado sobre cateto AB 
        square_ab = Polygon(
            A, B,
            B + DOWN * 4 * S,
            A + DOWN * 4 * S,
        )
        square_ab.set_stroke(color=BLUE, width=3)
        square_ab.set_fill(color=BLUE, opacity=0.25)

        # Quadrado sobre cateto AC 
        square_ac = Polygon(
            A, C,
            C + LEFT * 3 * S,
            A + LEFT * 3 * S,
        )
        square_ac.set_stroke(color=GREEN, width=3)
        square_ac.set_fill(color=GREEN, opacity=0.25)

        #quadrado sobre a hipotenusa BC
        v_bc = B - C
        length_bc = np.linalg.norm(v_bc)
        u_base = v_bc / length_bc
        perp_unit = np.array([3.0, 4.0, 0.0]) / 5.0

        square_bc = Polygon(
            C, B,
            B + 5 * S * perp_unit,
            C + 5 * S * perp_unit,
        )
        square_bc.set_stroke(color=YELLOW, width=3)
        square_bc.set_fill(color=YELLOW, opacity=0.25)

        # ── PASSO 1: Elevação ao quadrado
        texto_passo1 = Text(
            "1. Elevamos cada lado ao quadrado",
            font_size=28,
        ).to_edge(UP)
        self.play(Transform(title, texto_passo1))
        self.wait(0.5)



        eq_a2 = MathTex("a^2", font_size=48, color=GREEN).move_to(square_ac.get_center())
        eq_b2 = MathTex("b^2", font_size=48, color=BLUE).move_to(square_ab.get_center())
        eq_c2 = MathTex("c^2", font_size=48, color=YELLOW).move_to(square_bc.get_center())

        self.play(
            Transform(label_a, eq_a2),
            Transform(label_b, eq_b2),
        )
        self.wait(0.5)
        self.play(Transform(label_c, eq_c2))
        self.wait(1.5)

        #PASSO 2: Formar os quadrados visuais com preenchimento 
        texto_passo2 = Text(
            "2. O lado do quadrado é o próprio cateto",
            font_size=28,
        ).to_edge(UP)
        self.play(Transform(title, texto_passo2))
        self.wait(0.5)

        self.play(
            DrawBorderThenFill(square_ac),
            DrawBorderThenFill(square_ab),
        )
        self.wait(0.5)
        self.play(DrawBorderThenFill(square_bc))
        self.wait(1.5)

        # ── PASSO 3: Decompor as áreas em quadradinhos
        texto_passo3 = Text(
            "3. Decompomos as áreas dos catetos",
            font_size=28,
        ).to_edge(UP)
        self.play(Transform(title, texto_passo3))
        self.wait(0.5)

        # rade 4×4 (quadrado sobre AB)
        ab_cells = VGroup()
        for j in range(4):
            for i in range(4):
                center = np.array([
                    (i + 0.5) * S,
                    (-j - 0.5) * S,
                    0.0,
                ]) + OFFSET
                cell = Square(
                    side_length=1.0 * S,
                    stroke_width=1.0,
                    stroke_color=BLUE_D,
                    fill_color=BLUE_E,
                    fill_opacity=0.8,
                )
                cell.move_to(center)
                ab_cells.add(cell)

        #grade 3×3 (quadrado sobre AC)
        ac_cells = VGroup()
        for j in range(3):
            for i in range(3):
                center = np.array([
                    (-i - 0.5) * S,
                    (j + 0.5) * S,
                    0.0,
                ]) + OFFSET
                cell = Square(
                    side_length=1.0 * S,
                    stroke_width=1.0,
                    stroke_color=GREEN_D,
                    fill_color=GREEN_E,
                    fill_opacity=0.8,
                )
                cell.move_to(center)
                ac_cells.add(cell)

        #animar o preenchimento dos quadradinhos
        self.play(
            FadeOut(label_a), FadeOut(label_b),
            FadeIn(ab_cells, lag_ratio=0.05, run_time=2),
            FadeIn(ac_cells, lag_ratio=0.05, run_time=2),
        )
        self.wait(1)

        #destacar o quadrado da hipotenusa
        self.play(square_bc.animate.set_stroke(width=5))
        self.wait(0.5)

        #PASSO 4: Mover os quadradinhos para dentro da hipotenusa 
        texto_passo4 = Text(
            "4. E reorganizamos dentro da hipotenusa!",
            font_size=28,
        ).to_edge(UP)
        self.play(Transform(title, texto_passo4))
        self.wait(0.5)

        # angulo de rotação para alinhar ao quadrado da hipotenusa
        angle_bc = np.arctan2(u_base[1], u_base[0])

        # centro de cada célula-alvo na grade 5×5 sobre a hipotenusa
        def target_center(i, j):
            return (
                C
                + (i + 0.5) * S * u_base
                + (j + 0.5) * S * perp_unit
            )

        # Mapear 16 células de ab_cells → primeiras 16 posições da grade 5×5
        animations_ab = []
        for idx, cell in enumerate(ab_cells):
            i = idx % 5
            j = idx // 5
            center = target_center(i, j)
            animations_ab.append(
                cell.animate.rotate(angle_bc, about_point=cell.get_center()).move_to(center)
            )

        # Mapear 9 células de ac_cells → últimas 9 posições da grade 5×5
        animations_ac = []
        for idx, cell in enumerate(ac_cells):
            t_idx = 16 + idx
            i = t_idx % 5
            j = t_idx // 5
            center = target_center(i, j)
            animations_ac.append(
                cell.animate.rotate(angle_bc, about_point=cell.get_center()).move_to(center)
            )

        # Animar migração das células azuis
        self.play(
            AnimationGroup(*animations_ab, lag_ratio=0.05),
            run_time=4,
        )
        self.wait(0.5)

        # Animar migração das células verdes
        self.play(
            AnimationGroup(*animations_ac, lag_ratio=0.05),
            run_time=4,
        )
        self.wait(0.5)

        # Limpar quadrados dos catetos
        self.play(
            FadeOut(square_ab),
            FadeOut(square_ac),
        )
        self.wait(0.5)

        # ── PASSO 5: Equação Final Destacada ──
        texto_passo5 = Text(
            "Portanto:",
            font_size=28,
        ).to_edge(UP)
        self.play(Transform(title, texto_passo5))
        self.wait(0.5)

        # Limpar toda a geometria da cena para dar destaque total à fórmula
        self.play(
            FadeOut(triangle),
            FadeOut(dot_A), FadeOut(dot_B), FadeOut(dot_C),
            FadeOut(label_A), FadeOut(label_B), FadeOut(label_C),
            FadeOut(label_c),
            FadeOut(right_angle),
            FadeOut(square_bc),
            FadeOut(ab_cells), FadeOut(ac_cells),
        )
        self.wait(0.5)

        # Fórmula centralizada na tela limpa
        teorema = MathTex(
            "a^2", "+", "b^2", "=", "c^2",
            font_size=96,
        )
        teorema.set_color_by_tex("a^2", GREEN)
        teorema.set_color_by_tex("b^2", BLUE)
        teorema.set_color_by_tex("c^2", YELLOW)
        teorema.move_to(ORIGIN)

        # Moldura brilhante
        box = SurroundingRectangle(
            teorema, color=WHITE, buff=0.4,
            stroke_width=3, corner_radius=0.15,
        )


        self.play(Write(teorema, run_time=2))
        self.play(Create(box))
        self.wait(0.5)

        # Pulso de destaque
        self.play(
            teorema.animate.scale(1.15),
            box.animate.scale(1.15),
            rate_func=there_and_back,
            run_time=1,
        )

        # Texto de conclusão — posicionado bem abaixo da fórmula
        conclusion = Text(
            "Teorema de Pitágoras\n"
            "demonstrado visualmente por decomposição de áreas.",
            font_size=24,
        ).next_to(box, DOWN, buff=0.6)
        self.play(FadeIn(conclusion, shift=UP * 0.3))
        self.wait(3)