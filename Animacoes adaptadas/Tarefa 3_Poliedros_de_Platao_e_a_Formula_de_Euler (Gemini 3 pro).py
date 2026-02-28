from manim import *

class HexaedroRegular(Polyhedron):
    #criando um cubo regular via Polyhedron para possuir vertex_coords compatíveis com as demais
    def __init__(self, **kwargs):
        super().__init__(
            vertex_coords=[
                [1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1],
                [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]
            ],
            faces_list=[
                [0, 1, 3, 2], [4, 5, 7, 6], [0, 1, 5, 4], 
                [2, 3, 7, 6], [0, 2, 6, 4], [1, 3, 7, 5]
            ],
            **kwargs
        )

class PoliedrosDePlataoEuler(ThreeDScene):
    def construct(self):
        # Configuração inicial da câmera
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        
        # Título de Introdução
        titulo = Text("Poliedros de Platão e a Fórmula de Euler", font_size=40)
        self.add_fixed_in_frame_mobjects(titulo)
        self.play(Write(titulo))
        self.wait(1.5)
        self.play(FadeOut(titulo))

        # Dados dos Poliedros: (Nome, ClasseManim, Vértices, Arestas, Faces, Cor)
        dados_poliedros = [
            ("Tetraedro", Tetrahedron, 4, 6, 4, RED),
            ("Hexaedro (Cubo)", HexaedroRegular, 8, 12, 6, BLUE),
            ("Octaedro", Octahedron, 6, 12, 8, GREEN),
            ("Dodecaedro", Dodecahedron, 20, 30, 12, PURPLE),
            ("Icosaedro", Icosahedron, 12, 30, 20, GOLD),
        ]

        # Loop para apresentar cada poliedro
        for nome, classe_solido, v, a, f, cor in dados_poliedros:
            self.apresentar_solido(nome, classe_solido, v, a, f, cor)

        # Síntese Final
        self.apresentar_conclusao()

    def apresentar_solido(self, nome, classe_solido, v, a, f, cor):
        # 1. Criação do objeto 3D
        solido = classe_solido()  # sem argumentos!
        solido.set_fill(cor, opacity=0.6)
        solido.set_stroke(color=WHITE, width=2)
    
        vert_group = VGroup(*[Dot3D(point=v_pos, radius=0.06, color=YELLOW) for v_pos in solido.vertex_coords])
        solido.add(vert_group)

        solido.scale(1.2)  # reduzido
        solido.shift(LEFT * 1.5)  

        # 2. Elementos de Texto (HUD - fixos na tela)
        # Título do sólido
        texto_nome = Text(nome, font_size=36).to_corner(UL).shift(RIGHT)
        
        # Estatísticas: V, A, F
        stats_group = VGroup()
        texto_v = MathTex(f"V = {v}", color=YELLOW)
        texto_a = MathTex(f"A = {a}", color=WHITE)
        texto_f = MathTex(f"F = {f}", color=cor)
        
        # Organizar verticalmente
        stats_group.add(texto_v, texto_a, texto_f)
        stats_group.arrange(DOWN, aligned_edge=LEFT)
        stats_group.next_to(texto_nome, DOWN, aligned_edge=LEFT)

        # Grupo completo de informações
        info_hud = VGroup(texto_nome, stats_group)
        self.add_fixed_in_frame_mobjects(info_hud)

        # 3. Animação de entrada
        self.play(
            Create(solido),
            Write(info_hud),
            run_time=1.5
        )

        # Rotação para visualização 3D
        self.play(
            Rotate(solido, angle=2*PI, axis=UP),
            run_time=4,
            rate_func=linear
        )

        # Animação da Fórmula de Euler: V - A + F = 2
        #construção visual da equação no lado direito da tela
        #estrutura: [V_val] - [A_val] + [F_val] = 2
        
        eq_texto = MathTex(
            str(v), "-", str(a), "+", str(f), "=", "2",
            font_size=48
        )
        # Cores correspondentes aos valores
        eq_texto[0].set_color(YELLOW) # V
        eq_texto[2].set_color(WHITE)  # A
        eq_texto[4].set_color(cor)    # F

        eq_texto.to_corner(UR).shift(DOWN + LEFT)
        self.add_fixed_in_frame_mobjects(eq_texto)

        # Transformar os valores da lista lateral para a equação
        self.play(
            TransformFromCopy(texto_v[0][2:], eq_texto[0]), # Copia o numero de V
            TransformFromCopy(texto_a[0][2:], eq_texto[2]), # Copia o numero de A
            TransformFromCopy(texto_f[0][2:], eq_texto[4]), # Copia o numero de F
            Write(eq_texto[1]), # -
            Write(eq_texto[3]), # +
            Write(eq_texto[5]), # =
            run_time=1.5
        )
        
        # Revelar o resultado
        self.play(Write(eq_texto[6])) # 2
        
        # Destacar o resultado
        box = SurroundingRectangle(eq_texto, color=YELLOW)
        self.add_fixed_in_frame_mobjects(box)
        self.play(Create(box))
        
        self.wait(1)

        # Limpeza para o próximo
        # Pega as cópias geradas pelo TransformFromCopy para apagar junto
        partes_copiadas = VGroup(eq_texto[0], eq_texto[2], eq_texto[4])
        self.remove(partes_copiadas, box) # remove as instâncias residuais da tela pra não sobrepor o canto
        
        self.play(
            FadeOut(solido),
            FadeOut(info_hud),
            FadeOut(eq_texto),
            FadeOut(box)
        )

    def apresentar_conclusao(self):
        # Resetar câmera para dar sensação de "lousa" 2D, embora ainda em ThreeDScene
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=1.5)

        titulo_final = Text("Relação de Euler para Poliedros Convexos", font_size=36)
        titulo_final.to_edge(UP)

        # Fórmula Grande
        formula = MathTex("V", "-", "A", "+", "F", "=", "2", font_size=96)

        formula[0].set_color(YELLOW) # V
        formula[2].set_color(GRAY)   # A (Branco/Cinza)
        formula[4].set_color(BLUE)   # F (Cor genérica para destaque)
        
        # Explicação dos termos
        # Explicação dos termos (Separados para entrada didática)
        legenda_v = Tex("V = Vértices", color=YELLOW)
        legenda_a = Tex("A = Arestas", color=GRAY)
        legenda_f = Tex("F = Faces", color=BLUE)
        
        legenda = VGroup(legenda_v, legenda_a, legenda_f).arrange(DOWN, buff=0.5).scale(0.8).to_edge(DOWN)

        
        self.play(Write(titulo_final))
        self.play(Write(formula))
        
        #entrada didatica sincronizada
        self.play(FadeIn(legenda_v, shift=UP), Indicate(formula[0], color=YELLOW, scale_factor=1.5))
        self.play(FadeIn(legenda_a, shift=UP), Indicate(formula[2], color=WHITE, scale_factor=1.5))
        self.play(FadeIn(legenda_f, shift=UP), Indicate(formula[4], color=BLUE, scale_factor=1.5))
        
        #destaque final envolvente
        box_final = SurroundingRectangle(formula, color=ORANGE, buff=0.25)
        self.play(Create(box_final))
        self.wait(3)
