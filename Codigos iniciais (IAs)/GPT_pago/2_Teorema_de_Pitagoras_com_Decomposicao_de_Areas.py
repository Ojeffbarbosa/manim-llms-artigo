from manim import *
import numpy as np


class TeoremaDePitagorasComDecomposicaoDeAreas(Scene):
    def construct(self):
        # Título
        title = Text("Teorema de Pitágoras", font_size=48).to_edge(UP)
        self.play(Write(title))

        # Pontos do triângulo retângulo (3-4-5), deslocado para caber bem na cena
        A = np.array([0.0, -3.0, 0.0])
        B = np.array([4.0, -3.0, 0.0])
        C = np.array([0.0, 0.0, 0.0])

        # Lados do triângulo
        side_ab = Line(A, B)
        side_bc = Line(B, C)
        side_ca = Line(C, A)
        triangle = VGroup(side_ab, side_bc, side_ca).set_stroke(WHITE, width=3)

        # Marca de ângulo reto em A
        right_angle = RightAngle(side_ab, side_ca, length=0.2, quadrant=(1, 1), stroke_width=2)

        # Pontos (opcionais, para clareza visual)
        dot_A = Dot(A, color=WHITE)
        dot_B = Dot(B, color=WHITE)
        dot_C = Dot(C, color=WHITE)
        label_A = Text("A", font_size=24).next_to(dot_A, DOWN + LEFT, buff=0.1)
        label_B = Text("B", font_size=24).next_to(dot_B, DOWN + RIGHT, buff=0.1)
        label_C = Text("C", font_size=24).next_to(dot_C, UP + LEFT, buff=0.1)

        # Animação do triângulo
        self.play(Create(triangle), FadeIn(dot_A, dot_B, dot_C), FadeIn(label_A, label_B, label_C))
        self.play(Create(right_angle))
        self.wait(0.5)

        # Quadrado sobre o cateto AB (comprimento 4, para cima)
        square_ab = Polygon(
            A,
            B,
            B + UP * 4,
            A + UP * 4,
        )
        square_ab.set_stroke(color=BLUE, width=3)

        # Quadrado sobre o cateto AC (comprimento 3, para a esquerda)
        square_ac = Polygon(
            A,
            C,
            C + LEFT * 3,
            A + LEFT * 3,
        )
        square_ac.set_stroke(color=GREEN, width=3)

        # Quadrado sobre a hipotenusa BC
        # Vetor base ao longo de BC (de C para B)
        v_bc = B - C
        length_bc = np.linalg.norm(v_bc)
        u_base = v_bc / length_bc  # direção ao longo da hipotenusa (C -> B), tamanho 1
        # Vetor perpendicular externo ao triângulo (comprimento 1)
        perp_unit = np.array([3.0, 4.0, 0.0]) / 5.0  # (3,4,0)/5

        square_bc = Polygon(
            C,
            B,
            B + 5 * perp_unit,
            C + 5 * perp_unit,
        )
        square_bc.set_stroke(color=YELLOW, width=3)

        # Labels dos lados (opcionais)
        label_ab_len = Text("4", font_size=24).next_to(side_ab, DOWN, buff=0.2)
        label_ac_len = Text("3", font_size=24).next_to(side_ca, LEFT, buff=0.2)
        label_bc_len = Text("5", font_size=24).next_to(side_bc, RIGHT, buff=0.2)

        # Animação de criação dos quadrados
        self.play(Create(square_ab), Create(square_ac))
        self.play(Create(square_bc))
        self.play(FadeIn(label_ab_len, label_ac_len, label_bc_len))
        self.wait(0.5)

        # Decomposição dos quadrados dos catetos em pequenos quadrados (áreas unitárias)

        # Quadrado de área 4^2 = 16: grade 4x4
        ab_cells = VGroup()
        for j in range(4):  # vertical
            for i in range(4):  # horizontal
                center = np.array([
                    0.5 + i,          # x entre 0 e 4
                    -3.0 + 0.5 + j,   # y entre -3 e 1
                    0.0,
                ])
                cell = Square(
                    side_length=1.0,
                    stroke_width=1.0,
                    stroke_color=BLUE_D,
                    fill_color=BLUE_E,
                    fill_opacity=0.8,
                )
                cell.move_to(center)
                ab_cells.add(cell)

        # Quadrado de área 3^2 = 9: grade 3x3
        ac_cells = VGroup()
        for j in range(3):
            for i in range(3):
                center = np.array([
                    -3.0 + 0.5 + i,   # x entre -3 e 0
                    -3.0 + 0.5 + j,   # y entre -3 e 0
                    0.0,
                ])
                cell = Square(
                    side_length=1.0,
                    stroke_width=1.0,
                    stroke_color=GREEN_D,
                    fill_color=GREEN_E,
                    fill_opacity=0.8,
                )
                cell.move_to(center)
                ac_cells.add(cell)

        # Mostrar a decomposição dos quadrados dos catetos
        self.play(
            FadeIn(ab_cells, lag_ratio=0.05, run_time=2),
            FadeIn(ac_cells, lag_ratio=0.05, run_time=2),
        )
        self.wait(0.5)

        # Destacar o quadrado da hipotenusa
        self.play(square_bc.animate.set_stroke(color=YELLOW, width=5))
        self.wait(0.5)

        # Preparar animação de reorganização das áreas para dentro do quadrado da hipotenusa

        # Ângulo de rotação para alinhar as células aos lados do quadrado sobre a hipotenusa
        angle_bc = np.arctan2(u_base[1], u_base[0])

        # Função que fornece o centro da célula (i, j) na grade 5x5 do quadrado sobre BC
        def target_center(i, j):
            return (
                C
                + (i + 0.5) * u_base
                + (j + 0.5) * perp_unit
            )

        # Mapear as 16 células de ab_cells para as primeiras 16 posições da grade 5x5
        animations_ab = []
        for idx, cell in enumerate(ab_cells):
            t_idx = idx  # 0 a 15
            i = t_idx % 5
            j = t_idx // 5
            center = target_center(i, j)
            animations_ab.append(
                cell.animate.rotate(angle_bc, about_point=cell.get_center()).move_to(center)
            )

        # Mapear as 9 células de ac_cells para as últimas 9 posições da grade 5x5
        animations_ac = []
        for idx, cell in enumerate(ac_cells):
            t_idx = 16 + idx  # 16 a 24
            i = t_idx % 5
            j = t_idx // 5
            center = target_center(i, j)
            animations_ac.append(
                cell.animate.rotate(angle_bc, about_point=cell.get_center()).move_to(center)
            )

        # Animação: primeiro as células do quadrado maior (cateto de comprimento 4)
        self.play(
            AnimationGroup(*animations_ab, lag_ratio=0.05),
            run_time=4,
        )
        self.wait(0.5)

        # Depois as células do quadrado menor (cateto de comprimento 3)
        self.play(
            AnimationGroup(*animations_ac, lag_ratio=0.05),
            run_time=4,
        )
        self.wait(0.5)

        # Desvanecer os quadrados dos catetos, destacando o quadrado da hipotenusa preenchido
        self.play(
            FadeOut(square_ab),
            FadeOut(square_ac),
            FadeOut(label_ab_len),
            FadeOut(label_ac_len),
        )

        # Texto de conclusão
        conclusion = Text(
            "As áreas dos quadrados dos catetos\n"
            "se reorganizam para preencher o quadrado da hipotenusa.",
            font_size=30,
        ).to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(3)