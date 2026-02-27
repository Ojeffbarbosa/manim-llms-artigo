from manim import *


class PapelCoeficientesFuncaoQuadratica(Scene):
    def construct(self):
        # Configuração dos eixos
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 7, 1],
            x_length=9,
            y_length=6,
            axis_config={"include_numbers": True, "font_size": 20},
            tips=True,
        ).shift(DOWN * 0.5)
        
        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")
        
        # Value trackers para os coeficientes
        a_val = ValueTracker(1)
        b_val = ValueTracker(0)
        c_val = ValueTracker(0)
        
        # Parábola dinâmica
        def get_parabola():
            a = a_val.get_value()
            b = b_val.get_value()
            c = c_val.get_value()
            
            return axes.plot(
                lambda x: a * x**2 + b * x + c,
                color=BLUE,
                x_range=[-4.5, 4.5],
                stroke_width=3,
            )
        
        parabola = always_redraw(get_parabola)
        
        # Ponto do vértice dinâmico
        def get_vertex_dot():
            a = a_val.get_value()
            b = b_val.get_value()
            c = c_val.get_value()
            
            if a != 0:
                x_v = -b / (2 * a)
                y_v = a * x_v**2 + b * x_v + c
            else:
                x_v, y_v = 0, c
            
            return Dot(axes.c2p(x_v, y_v), color=ORANGE, radius=0.08)
        
        vertex_dot = always_redraw(get_vertex_dot)
        
        # Display dinâmico dos coeficientes
        def get_coef_display():
            a = a_val.get_value()
            b = b_val.get_value()
            c = c_val.get_value()
            
            a_label = MathTex(f"a = {a:.1f}", color=YELLOW, font_size=30)
            b_label = MathTex(f"b = {b:.1f}", color=GREEN, font_size=30)
            c_label = MathTex(f"c = {c:.1f}", color=RED, font_size=30)
            
            group = VGroup(a_label, b_label, c_label)
            group.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
            group.to_corner(UR).shift(DOWN * 0.5 + LEFT * 0.2)
            
            return group
        
        coef_display = always_redraw(get_coef_display)
        
        # Título
        titulo = Text("Papel dos Coeficientes da Função Quadrática", font_size=30)
        titulo.to_edge(UP)
        
        # Fórmula geral com coeficientes coloridos
        formula_geral = MathTex(
            "f(x) = ", "a", "x^2 + ", "b", "x + ", "c",
            font_size=36
        )
        formula_geral[1].set_color(YELLOW)
        formula_geral[3].set_color(GREEN)
        formula_geral[5].set_color(RED)
        formula_geral.next_to(titulo, DOWN)
        
        # Animações de introdução
        self.play(Write(titulo))
        self.wait(0.5)
        self.play(Write(formula_geral))
        self.wait()
        
        # Move fórmula para o canto
        self.play(
            formula_geral.animate.scale(0.8).to_corner(UL).shift(DOWN * 0.3)
        )
        
        # Cria eixos e parábola
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(parabola), FadeIn(vertex_dot))
        self.add(coef_display)
        self.wait()
        
        # ========== PARTE 1: Coeficiente 'a' ==========
        texto_a = Text(
            "Coeficiente a: controla abertura e concavidade",
            font_size=22,
            color=YELLOW
        ).to_edge(DOWN)
        
        self.play(Write(texto_a))
        self.wait(0.5)
        
        # Aumenta a - parábola mais fechada
        self.play(a_val.animate.set_value(2), run_time=1.5)
        self.wait(0.5)
        
        # Diminui a - parábola mais aberta
        self.play(a_val.animate.set_value(0.5), run_time=1.5)
        self.wait(0.5)
        
        # a negativo - concavidade para baixo
        self.play(a_val.animate.set_value(-1), run_time=1.5)
        self.wait(0.5)
        
        # a negativo menor em módulo
        self.play(a_val.animate.set_value(-0.5), run_time=1)
        self.wait(0.5)
        
        # Retorna a = 1
        self.play(a_val.animate.set_value(1), run_time=1)
        self.play(FadeOut(texto_a))
        self.wait(0.5)
        
        # ========== PARTE 2: Coeficiente 'b' ==========
        texto_b = Text(
            "Coeficiente b: desloca o vértice horizontalmente",
            font_size=22,
            color=GREEN
        ).to_edge(DOWN)
        
        self.play(Write(texto_b))
        self.wait(0.5)
        
        # b positivo - vértice move para esquerda
        self.play(b_val.animate.set_value(4), run_time=1.5)
        self.wait(0.5)
        
        # b negativo - vértice move para direita
        self.play(b_val.animate.set_value(-4), run_time=2)
        self.wait(0.5)
        
        # Retorna b = 0
        self.play(b_val.animate.set_value(0), run_time=1)
        self.play(FadeOut(texto_b))
        self.wait(0.5)
        
        # ========== PARTE 3: Coeficiente 'c' ==========
        texto_c = Text(
            "Coeficiente c: desloca a parábola verticalmente",
            font_size=22,
            color=RED
        ).to_edge(DOWN)
        
        self.play(Write(texto_c))
        self.wait(0.5)
        
        # c positivo - move para cima
        self.play(c_val.animate.set_value(4), run_time=1.5)
        self.wait(0.5)
        
        # c negativo - move para baixo
        self.play(c_val.animate.set_value(-3), run_time=2)
        self.wait(0.5)
        
        # Retorna c = 0
        self.play(c_val.animate.set_value(0), run_time=1)
        self.play(FadeOut(texto_c))
        self.wait()
        
        # Finalização
        texto_final = Text(
            "Cada coeficiente tem um papel específico na forma da parábola",
            font_size=24,
            color=WHITE
        ).to_edge(DOWN)
        
        self.play(Write(texto_final))
        self.wait(2)
        
        self.play(
            FadeOut(parabola),
            FadeOut(vertex_dot),
            FadeOut(axes),
            FadeOut(axes_labels),
            FadeOut(coef_display),
            FadeOut(formula_geral),
            FadeOut(texto_final),
        )
        self.wait(0.5)
