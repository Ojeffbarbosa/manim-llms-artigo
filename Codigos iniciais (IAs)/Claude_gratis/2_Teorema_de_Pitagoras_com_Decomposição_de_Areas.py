from manim import *

class TeoremaDepitagorasComDecomposicaoDeAreas(Scene):
    def construct(self):
        # Definição do triângulo retângulo
        cateto_a = 3
        cateto_b = 4
        hipotenusa = 5
        
        # Criar triângulo retângulo
        triangulo = Polygon(
            ORIGIN,
            RIGHT * cateto_a,
            RIGHT * cateto_a + UP * cateto_b,
            color=WHITE,
            fill_opacity=0.3,
            fill_color=BLUE
        )
        triangulo.move_to(ORIGIN)
        
        # Criar quadrados sobre cada lado
        quadrado_a = Square(side_length=cateto_a, color=RED, fill_opacity=0.6)
        quadrado_a.next_to(triangulo, DOWN, buff=0)
        quadrado_a.align_to(triangulo, LEFT)
        
        quadrado_b = Square(side_length=cateto_b, color=GREEN, fill_opacity=0.6)
        quadrado_b.next_to(triangulo, LEFT, buff=0)
        quadrado_b.align_to(triangulo, UP)
        
        quadrado_c = Square(side_length=hipotenusa, color=YELLOW, fill_opacity=0.3)
        vertices_triangulo = triangulo.get_vertices()
        quadrado_c.rotate(np.arctan(cateto_b / cateto_a))
        quadrado_c.move_to(vertices_triangulo[1])
        direction = (vertices_triangulo[2] - vertices_triangulo[1]) / hipotenusa
        quadrado_c.shift(direction * hipotenusa / 2)
        perpendicular = np.array([-direction[1], direction[0], 0])
        quadrado_c.shift(perpendicular * hipotenusa / 2)
        
        # Labels
        label_a = MathTex("a", color=RED).scale(1.2).next_to(quadrado_a, DOWN)
        label_b = MathTex("b", color=GREEN).scale(1.2).next_to(quadrado_b, LEFT)
        label_c = MathTex("c", color=YELLOW).scale(1.2).next_to(quadrado_c, RIGHT, buff=0.5)
        
        # Animar criação do triângulo e quadrados
        self.play(Create(triangulo))
        self.wait(0.5)
        self.play(
            Create(quadrado_a),
            Create(quadrado_b),
            Create(quadrado_c),
            Write(label_a),
            Write(label_b),
            Write(label_c)
        )
        self.wait()
        
        # Fórmula do teorema
        formula = MathTex("a^2", "+", "b^2", "=", "c^2").scale(1.2).to_edge(UP)
        formula[0].set_color(RED)
        formula[2].set_color(GREEN)
        formula[4].set_color(YELLOW)
        self.play(Write(formula))
        self.wait()
        
        # Decomposição do quadrado vermelho (cateto a)
        num_subdivisoes_a = 9
        pecas_a = VGroup()
        for i in range(num_subdivisoes_a):
            peca = Square(side_length=cateto_a/3, color=RED, fill_opacity=0.7, stroke_width=1)
            peca.move_to(quadrado_a.get_corner(DL) + RIGHT * (cateto_a/6 + (i%3) * cateto_a/3) + UP * (cateto_a/6 + (i//3) * cateto_a/3))
            pecas_a.add(peca)
        
        # Decomposição do quadrado verde (cateto b)
        num_subdivisoes_b = 16
        pecas_b = VGroup()
        for i in range(num_subdivisoes_b):
            peca = Square(side_length=cateto_b/4, color=GREEN, fill_opacity=0.7, stroke_width=1)
            peca.move_to(quadrado_b.get_corner(DL) + RIGHT * (cateto_b/8 + (i%4) * cateto_b/4) + UP * (cateto_b/8 + (i//4) * cateto_b/4))
            pecas_b.add(peca)
        
        self.play(
            FadeOut(quadrado_a),
            FadeOut(quadrado_b),
            FadeIn(pecas_a),
            FadeIn(pecas_b)
        )
        self.wait()
        
        # Reorganizar peças no quadrado da hipotenusa
        pecas_destino = VGroup()
        angulo = np.arctan(cateto_b / cateto_a)
        centro_c = quadrado_c.get_center()
        
        for i, peca in enumerate(pecas_a):
            nova_peca = peca.copy()
            row = i // 3
            col = i % 3
            offset_x = -hipotenusa/2 + (col * cateto_a/3 + cateto_a/6)
            offset_y = -hipotenusa/2 + (row * cateto_a/3 + cateto_a/6)
            nova_peca.rotate(angulo)
            nova_peca.move_to(centro_c + RIGHT * offset_x + UP * offset_y)
            pecas_destino.add(nova_peca)
        
        for i, peca in enumerate(pecas_b):
            nova_peca = peca.copy()
            row = i // 4
            col = i % 4
            offset_x = -hipotenusa/2 + (col * cateto_b/4 + cateto_b/8 + cateto_a)
            offset_y = -hipotenusa/2 + (row * cateto_b/4 + cateto_b/8)
            nova_peca.rotate(angulo)
            nova_peca.move_to(centro_c + RIGHT * offset_x + UP * offset_y)
            pecas_destino.add(nova_peca)
        
        self.play(
            *[Transform(pecas_a[i], pecas_destino[i]) for i in range(len(pecas_a))],
            *[Transform(pecas_b[i], pecas_destino[i + len(pecas_a)]) for i in range(len(pecas_b))],
            run_time=3
        )
        self.wait()
        
        # Destacar resultado
        self.play(
            quadrado_c.animate.set_fill(opacity=0.8),
            formula.animate.scale(1.2)
        )
        self.wait(2)
