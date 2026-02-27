from manim import *


class PoliedrosDePlataoEuler(ThreeDScene):
    def construct(self):
        # Título inicial
        titulo = Text("Poliedros de Platão", font_size=48)
        subtitulo = Text("e a Fórmula de Euler", font_size=36, color=BLUE)
        grupo_titulo = VGroup(titulo, subtitulo).arrange(DOWN, buff=0.3)
        
        self.play(Write(titulo))
        self.play(FadeIn(subtitulo, shift=UP * 0.3))
        self.wait(1)
        self.play(FadeOut(grupo_titulo))
        
        # Configurar câmera 3D
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES)
        
        # Dados dos poliedros de Platão
        poliedros = [
            {"nome": "Tetraedro", "V": 4, "A": 6, "F": 4, "cor": RED},
            {"nome": "Cubo", "V": 8, "A": 12, "F": 6, "cor": BLUE},
            {"nome": "Octaedro", "V": 6, "A": 12, "F": 8, "cor": GREEN},
            {"nome": "Dodecaedro", "V": 20, "A": 30, "F": 12, "cor": ORANGE},
            {"nome": "Icosaedro", "V": 12, "A": 30, "F": 20, "cor": PURPLE},
        ]
        
        for dados in poliedros:
            self.mostrar_poliedro(dados)
        
        self.mostrar_sintese(poliedros)
    
    def criar_poliedro(self, nome):
        if nome == "Tetraedro":
            return Tetrahedron()
        elif nome == "Cubo":
            return Cube()
        elif nome == "Octaedro":
            return Octahedron()
        elif nome == "Dodecaedro":
            return Dodecahedron()
        elif nome == "Icosaedro":
            return Icosahedron()
    
    def mostrar_poliedro(self, dados):
        nome = dados["nome"]
        V, A, F = dados["V"], dados["A"], dados["F"]
        cor = dados["cor"]
        
        poliedro = self.criar_poliedro(nome)
        poliedro.set_color(cor)
        poliedro.set_fill(cor, opacity=0.7)
        poliedro.scale(1.3)
        
        # Nome do poliedro
        label_nome = Text(nome, font_size=42, color=cor)
        label_nome.to_edge(UP)
        self.add_fixed_in_frame_mobjects(label_nome)
        
        self.play(Create(poliedro), Write(label_nome), run_time=1.5)
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(1)
        
        # Informações V, A, F
        texto_v = MathTex("V", "=", str(V), font_size=44)
        texto_v[0].set_color(RED)
        texto_v[2].set_color(RED)
        
        texto_a = MathTex("A", "=", str(A), font_size=44)
        texto_a[0].set_color(GREEN)
        texto_a[2].set_color(GREEN)
        
        texto_f = MathTex("F", "=", str(F), font_size=44)
        texto_f[0].set_color(YELLOW)
        texto_f[2].set_color(YELLOW)
        
        grupo_info = VGroup(texto_v, texto_a, texto_f).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        grupo_info.to_corner(UL).shift(DOWN * 0.7 + RIGHT * 0.2)
        
        self.add_fixed_in_frame_mobjects(grupo_info)
        
        # Destacar vértices
        self.play(Write(texto_v), poliedro.animate.set_stroke(RED, width=2), run_time=0.8)
        self.wait(0.3)
        
        # Destacar arestas
        self.play(Write(texto_a), poliedro.animate.set_stroke(GREEN, width=3), run_time=0.8)
        self.wait(0.3)
        
        # Destacar faces
        self.play(Write(texto_f), poliedro.animate.set_stroke(YELLOW, width=2), run_time=0.8)
        self.wait(0.5)
        
        # Restaurar cor original
        self.play(poliedro.animate.set_stroke(cor, width=1), run_time=0.5)
        
        # Fórmula de Euler com animação
        euler_texto = MathTex("V", "-", "A", "+", "F", "=", font_size=52)
        euler_texto[0].set_color(RED)
        euler_texto[2].set_color(GREEN)
        euler_texto[4].set_color(YELLOW)
        euler_texto.to_edge(DOWN, buff=0.8).shift(LEFT * 1.5)
        
        self.add_fixed_in_frame_mobjects(euler_texto)
        self.play(Write(euler_texto), run_time=1)
        
        # Mostrar cálculo
        calculo = MathTex(str(V), "-", str(A), "+", str(F), font_size=52)
        calculo[0].set_color(RED)
        calculo[2].set_color(GREEN)
        calculo[4].set_color(YELLOW)
        calculo.next_to(euler_texto, RIGHT, buff=0.2)
        
        self.add_fixed_in_frame_mobjects(calculo)
        self.play(TransformFromCopy(texto_v[2], calculo[0]), run_time=0.5)
        self.play(Write(calculo[1]), run_time=0.2)
        self.play(TransformFromCopy(texto_a[2], calculo[2]), run_time=0.5)
        self.play(Write(calculo[3]), run_time=0.2)
        self.play(TransformFromCopy(texto_f[2], calculo[4]), run_time=0.5)
        
        # Resultado
        igual_resultado = MathTex("=", "2", font_size=52)
        igual_resultado[1].set_color(BLUE_A)
        igual_resultado.next_to(calculo, RIGHT, buff=0.2)
        
        self.add_fixed_in_frame_mobjects(igual_resultado)
        self.play(Write(igual_resultado), run_time=0.8)
        
        # Destacar resultado
        caixa = SurroundingRectangle(igual_resultado[1], color=BLUE, buff=0.15, stroke_width=3)
        self.add_fixed_in_frame_mobjects(caixa)
        self.play(Create(caixa), Flash(igual_resultado[1], color=BLUE, flash_radius=0.5))
        self.wait(1.5)
        
        # Limpar tela
        self.stop_ambient_camera_rotation()
        self.play(
            FadeOut(poliedro),
            FadeOut(label_nome),
            FadeOut(grupo_info),
            FadeOut(euler_texto),
            FadeOut(calculo),
            FadeOut(igual_resultado),
            FadeOut(caixa)
        )
        self.wait(0.3)
    
    def mostrar_sintese(self, poliedros):
        # Transição para visão 2D
        self.move_camera(phi=0, theta=-90 * DEGREES, run_time=1.5)
        
        # Título da síntese
        titulo = Text("Fórmula de Euler para Poliedros Convexos", font_size=38, color=GOLD)
        titulo.to_edge(UP, buff=0.5)
        self.add_fixed_in_frame_mobjects(titulo)
        self.play(Write(titulo), run_time=1.5)
        
        # Fórmula principal
        formula = MathTex("V", "-", "A", "+", "F", "=", "2", font_size=80)
        formula[0].set_color(RED)
        formula[2].set_color(GREEN)
        formula[4].set_color(YELLOW)
        formula[6].set_color(BLUE)
        formula.move_to(UP * 1.3)
        
        self.add_fixed_in_frame_mobjects(formula)
        self.play(Write(formula), run_time=2)
        
        # Caixa de destaque
        caixa_formula = SurroundingRectangle(formula, color=GOLD, buff=0.25, stroke_width=3)
        self.add_fixed_in_frame_mobjects(caixa_formula)
        self.play(Create(caixa_formula))
        self.wait(1)
        
        # Legenda
        legenda_v = MathTex("V", "= \\text{Vértices}", font_size=28)
        legenda_v[0].set_color(RED)
        legenda_a = MathTex("A", "= \\text{Arestas}", font_size=28)
        legenda_a[0].set_color(GREEN)
        legenda_f = MathTex("F", "= \\text{Faces}", font_size=28)
        legenda_f[0].set_color(YELLOW)
        
        legenda = VGroup(legenda_v, legenda_a, legenda_f).arrange(RIGHT, buff=0.8)
        legenda.next_to(caixa_formula, DOWN, buff=0.4)
        
        self.add_fixed_in_frame_mobjects(legenda)
        self.play(FadeIn(legenda, shift=UP * 0.3))
        self.wait(0.5)
        
        # Tabela resumo
        dados_tabela = [
            [p["nome"], str(p["V"]), str(p["A"]), str(p["F"]), "2"]
            for p in poliedros
        ]
        
        tabela = Table(
            dados_tabela,
            col_labels=[
                Text("Poliedro", font_size=20),
                MathTex("V", color=RED, font_size=26),
                MathTex("A", color=GREEN, font_size=26),
                MathTex("F", color=YELLOW, font_size=26),
                MathTex("V-A+F", color=BLUE, font_size=26)
            ],
            include_outer_lines=True,
            line_config={"stroke_width": 1, "color": WHITE},
            element_to_mobject_config={"font_size": 22}
        )
        tabela.scale(0.48)
        tabela.to_edge(DOWN, buff=0.4)
        
        self.add_fixed_in_frame_mobjects(tabela)
        self.play(Create(tabela), run_time=2)
        self.wait(1)
        
        # Destacar cada linha da tabela mostrando que V-A+F = 2
        for i in range(len(poliedros)):
            linha = i + 2
            celula_resultado = tabela.get_cell((linha, 5))
            destaque = SurroundingRectangle(celula_resultado, color=BLUE, buff=0.05, stroke_width=2)
            self.add_fixed_in_frame_mobjects(destaque)
            self.play(Create(destaque), run_time=0.3)
        
        self.wait(1)
        
        # Mensagem final
        mensagem = VGroup(
            Text("Leonhard Euler (1707-1783)", font_size=22, color=GRAY),
            Text("descobriu que para todo poliedro convexo:", font_size=24),
            MathTex("V - A + F = 2", font_size=36, color=GOLD)
        ).arrange(DOWN, buff=0.15)
        mensagem.to_edge(DOWN, buff=0.15)
        
        self.add_fixed_in_frame_mobjects(mensagem)
        self.play(
            FadeOut(tabela),
            *[FadeOut(mob) for mob in self.mobjects if isinstance(mob, SurroundingRectangle) and mob != caixa_formula],
            run_time=0.5
        )
        self.play(FadeIn(mensagem, shift=UP * 0.3))
        self.wait(1)
        
        # Animação final com todos os poliedros pequenos
        mini_poliedros = VGroup()
        cores = [RED, BLUE, GREEN, ORANGE, PURPLE]
        nomes = ["Tetraedro", "Cubo", "Octaedro", "Dodecaedro", "Icosaedro"]
        
        for i, nome in enumerate(nomes):
            mini = self.criar_poliedro(nome)
            mini.set_color(cores[i])
            mini.set_fill(cores[i], opacity=0.6)
            mini.scale(0.4)
            mini_poliedros.add(mini)
        
        mini_poliedros.arrange(RIGHT, buff=0.6)
        mini_poliedros.move_to(DOWN * 2.5)
        
        self.play(
            FadeOut(mensagem),
            *[Create(p) for p in mini_poliedros],
            run_time=1.5
        )
        
        # Rotacionar os mini poliedros
        self.play(
            *[Rotate(p, angle=2*PI, axis=UP) for p in mini_poliedros],
            run_time=3,
            rate_func=smooth
        )
        
        # Texto final
        texto_final = Text("Todos obedecem: V - A + F = 2", font_size=30, color=WHITE)
        texto_final.to_edge(DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(texto_final)
        self.play(Write(texto_final))
        
        self.wait(3)
