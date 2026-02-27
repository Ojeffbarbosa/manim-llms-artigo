from manim import *
import numpy as np


class TeoremaDepitagorasDecomposicao(Scene):
    def construct(self):
        # Título
        titulo = Text("Teorema de Pitágoras", font_size=44, color=WHITE)
        titulo.to_edge(UP, buff=0.5)
        self.play(Write(titulo))
        self.wait(0.5)

        # Parâmetros do triângulo retângulo (3-4-5)
        escala = 0.55
        cateto_a = 3 * escala
        cateto_b = 4 * escala
        hipotenusa_c = 5 * escala

        # Vértices do triângulo retângulo
        ponto_A = ORIGIN
        ponto_B = RIGHT * cateto_b
        ponto_C = UP * cateto_a

        # Criar o triângulo retângulo
        triangulo = Polygon(
            ponto_A, ponto_B, ponto_C,
            color=WHITE,
            fill_color=GRAY,
            fill_opacity=0.3,
            stroke_width=3
        )
        triangulo.move_to(ORIGIN)

        # Posicionar o triângulo
        deslocamento_triangulo = LEFT * 3.5 + DOWN * 0.5
        triangulo.shift(deslocamento_triangulo)

        # Atualizar vértices após deslocamento
        ponto_A = triangulo.get_vertices()[0]
        ponto_B = triangulo.get_vertices()[1]
        ponto_C = triangulo.get_vertices()[2]

        # Labels dos lados
        label_a = MathTex("a", font_size=36, color=GREEN)
        label_b = MathTex("b", font_size=36, color=BLUE)
        label_c = MathTex("c", font_size=36, color=RED)

        # Posicionar labels
        label_a.next_to((ponto_A + ponto_C) / 2, LEFT, buff=0.2)
        label_b.next_to((ponto_A + ponto_B) / 2, DOWN, buff=0.2)
        label_c.next_to((ponto_B + ponto_C) / 2, UR, buff=0.15)

        # Ângulo reto
        angulo_reto = RightAngle(
            Line(ponto_A, ponto_B),
            Line(ponto_A, ponto_C),
            length=0.25,
            color=YELLOW
        )

        # Mostrar triângulo
        self.play(Create(triangulo))
        self.play(
            Create(angulo_reto),
            Write(label_a),
            Write(label_b),
            Write(label_c)
        )
        self.wait(0.5)

        # Criar quadrados sobre os catetos
        # Quadrado sobre cateto a (vertical, à esquerda)
        quadrado_a = Square(
            side_length=cateto_a,
            color=GREEN,
            fill_color=GREEN,
            fill_opacity=0.5,
            stroke_width=2
        )
        quadrado_a.next_to(triangulo, LEFT, buff=0)
        quadrado_a.align_to(ponto_A, DOWN)

        # Quadrado sobre cateto b (horizontal, abaixo)
        quadrado_b = Square(
            side_length=cateto_b,
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=0.5,
            stroke_width=2
        )
        quadrado_b.next_to(triangulo, DOWN, buff=0)
        quadrado_b.align_to(ponto_A, LEFT)

        # Quadrado sobre a hipotenusa
        angulo_hip = np.arctan(cateto_a / cateto_b)
        quadrado_c = Square(
            side_length=hipotenusa_c,
            color=RED,
            fill_color=RED,
            fill_opacity=0.3,
            stroke_width=2
        )
        quadrado_c.rotate(angulo_hip)
        centro_hip = (ponto_B + ponto_C) / 2
        direcao_externa = np.array([cateto_a, cateto_b, 0]) / hipotenusa_c
        quadrado_c.move_to(centro_hip + direcao_externa * hipotenusa_c / 2)

        # Labels dos quadrados
        label_a2 = MathTex("a^2", font_size=32, color=GREEN)
        label_a2.move_to(quadrado_a.get_center())

        label_b2 = MathTex("b^2", font_size=32, color=BLUE)
        label_b2.move_to(quadrado_b.get_center())

        label_c2 = MathTex("c^2", font_size=32, color=RED)
        label_c2.move_to(quadrado_c.get_center())

        # Animar criação dos quadrados
        self.play(Create(quadrado_a), Write(label_a2))
        self.play(Create(quadrado_b), Write(label_b2))
        self.play(Create(quadrado_c), Write(label_c2))
        self.wait()

        # Equação do teorema
        equacao = MathTex("a^2", "+", "b^2", "=", "c^2", font_size=48)
        equacao[0].set_color(GREEN)
        equacao[2].set_color(BLUE)
        equacao[4].set_color(RED)
        equacao.to_edge(DOWN, buff=0.8)

        self.play(Write(equacao))
        self.wait()

        # Preparar para decomposição
        self.play(
            FadeOut(label_a2),
            FadeOut(label_b2),
            FadeOut(label_c2),
            FadeOut(label_a),
            FadeOut(label_b),
            FadeOut(label_c),
            FadeOut(angulo_reto),
            triangulo.animate.set_opacity(0.2)
        )
        self.wait(0.5)

        # Dividir quadrado a em 9 partes (3x3)
        pecas_a = VGroup()
        lado_peca_a = cateto_a / 3
        canto_a = quadrado_a.get_corner(DL)
        
        for i in range(3):
            for j in range(3):
                peca = Square(
                    side_length=lado_peca_a,
                    color=GREEN,
                    fill_color=GREEN,
                    fill_opacity=0.7,
                    stroke_width=1.5
                )
                peca.move_to(
                    canto_a + RIGHT * (i + 0.5) * lado_peca_a + UP * (j + 0.5) * lado_peca_a
                )
                pecas_a.add(peca)

        # Dividir quadrado b em 16 partes (4x4)
        pecas_b = VGroup()
        lado_peca_b = cateto_b / 4
        canto_b = quadrado_b.get_corner(DL)
        
        for i in range(4):
            for j in range(4):
                peca = Square(
                    side_length=lado_peca_b,
                    color=BLUE,
                    fill_color=BLUE,
                    fill_opacity=0.7,
                    stroke_width=1.5
                )
                peca.move_to(
                    canto_b + RIGHT * (i + 0.5) * lado_peca_b + UP * (j + 0.5) * lado_peca_b
                )
                pecas_b.add(peca)

        # Mostrar divisão dos quadrados
        self.play(
            FadeOut(quadrado_a),
            FadeIn(pecas_a),
            run_time=1
        )
        self.play(
            FadeOut(quadrado_b),
            FadeIn(pecas_b),
            run_time=1
        )
        self.wait(0.5)

        # Posição do quadrado c para receber as peças
        quadrado_c_destino = Square(
            side_length=hipotenusa_c,
            color=RED,
            fill_color=RED,
            fill_opacity=0.1,
            stroke_width=3
        )
        quadrado_c_destino.move_to(RIGHT * 2.5)

        # Mover quadrado c para nova posição
        self.play(
            ReplacementTransform(quadrado_c, quadrado_c_destino),
            run_time=1.5
        )
        self.wait(0.5)

        # Criar grade 5x5 dentro do quadrado c
        lado_unidade = hipotenusa_c / 5
        canto_c = quadrado_c_destino.get_corner(DL)

        # Posições destino para as peças de a (9 unidades)
        posicoes_a = []
        for pos in [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]:
            i, j = pos
            posicoes_a.append(
                canto_c + RIGHT * (i + 0.5) * lado_unidade + UP * (j + 0.5) * lado_unidade
            )

        # Posições destino para as peças de b (16 unidades)
        posicoes_b = []
        todas_posicoes = []
        for i in range(5):
            for j in range(5):
                todas_posicoes.append((i, j))
        
        # Remover posições já usadas por a
        posicoes_usadas_a = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
        posicoes_restantes = [p for p in todas_posicoes if p not in posicoes_usadas_a]
        
        for pos in posicoes_restantes:
            i, j = pos
            posicoes_b.append(
                canto_c + RIGHT * (i + 0.5) * lado_unidade + UP * (j + 0.5) * lado_unidade
            )

        # Criar peças transformadas para encaixar na grade 5x5
        pecas_a_destino = VGroup()
        for idx, peca in enumerate(pecas_a):
            nova_peca = Square(
                side_length=lado_unidade,
                color=GREEN,
                fill_color=GREEN,
                fill_opacity=0.7,
                stroke_width=1
            )
            nova_peca.move_to(posicoes_a[idx])
            pecas_a_destino.add(nova_peca)

        pecas_b_destino = VGroup()
        for idx, peca in enumerate(pecas_b):
            nova_peca = Square(
                side_length=lado_unidade,
                color=BLUE,
                fill_color=BLUE,
                fill_opacity=0.7,
                stroke_width=1
            )
            nova_peca.move_to(posicoes_b[idx])
            pecas_b_destino.add(nova_peca)

        # Texto explicativo
        texto_decomp = Text(
            "Reorganizando as áreas...",
            font_size=28,
            color=YELLOW
        )
        texto_decomp.next_to(quadrado_c_destino, UP, buff=0.5)
        self.play(Write(texto_decomp))

        # Animar movimento das peças de a
        self.play(
            *[
                ReplacementTransform(pecas_a[i], pecas_a_destino[i])
                for i in range(len(pecas_a))
            ],
            run_time=2
        )
        self.wait(0.3)

        # Animar movimento das peças de b
        self.play(
            *[
                ReplacementTransform(pecas_b[i], pecas_b_destino[i])
                for i in range(len(pecas_b))
            ],
            run_time=2
        )
        self.wait(0.5)

        # Atualizar texto
        self.play(FadeOut(texto_decomp))
        
        texto_final = MathTex(
            "a^2 + b^2 = c^2",
            font_size=42,
            color=WHITE
        )
        texto_final.next_to(quadrado_c_destino, UP, buff=0.5)
        
        # Destacar resultado
        caixa_equacao = SurroundingRectangle(equacao, color=YELLOW, buff=0.15)
        
        self.play(
            Write(texto_final),
            Create(caixa_equacao)
        )
        self.wait()

        # Contagem visual
        contador_a = MathTex("9", color=GREEN, font_size=36)
        contador_b = MathTex("16", color=BLUE, font_size=36)
        contador_total = MathTex("25", color=RED, font_size=36)
        
        sinal_mais = MathTex("+", font_size=36)
        sinal_igual = MathTex("=", font_size=36)
        
        contagem = VGroup(contador_a, sinal_mais, contador_b, sinal_igual, contador_total)
        contagem.arrange(RIGHT, buff=0.3)
        contagem.next_to(quadrado_c_destino, DOWN, buff=0.5)
        
        self.play(Write(contagem))
        self.wait()

        # Pulsar o resultado final
        self.play(
            pecas_a_destino.animate.set_fill(opacity=0.9),
            pecas_b_destino.animate.set_fill(opacity=0.9),
            rate_func=there_and_back,
            run_time=1
        )
        self.wait(2)

        # Finalização
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )

        # Conclusão
        conclusao = VGroup(
            Text("Teorema de Pitágoras", font_size=40, color=WHITE),
            MathTex("a^2 + b^2 = c^2", font_size=52, color=YELLOW)
        )
        conclusao.arrange(DOWN, buff=0.5)
        
        self.play(FadeIn(conclusao, scale=0.8))
        self.wait(2)
