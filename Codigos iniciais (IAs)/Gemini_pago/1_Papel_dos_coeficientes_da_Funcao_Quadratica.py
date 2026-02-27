from manim import *

class QuadraticCoefficients(Scene):
    def construct(self):
        # --- Configuração Inicial ---
        # Criação dos eixos cartesianos
        axes = Axes(
            x_range=[-6, 6, 1],
            y_range=[-6, 6, 1],
            x_length=10,
            y_length=7,
            axis_config={"color": WHITE},
            tips=False
        ).add_coordinates()

        # Labels dos eixos
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

        # --- Variáveis de Controle (Trackers) ---
        # Inicialmente f(x) = 1x^2 + 0x + 0
        a = ValueTracker(1)
        b = ValueTracker(0)
        c = ValueTracker(0)

        # --- Gráfico da Função ---
        # always_redraw garante que o gráfico atualize frame a frame
        graph = always_redraw(
            lambda: axes.plot(
                lambda x: a.get_value() * x**2 + b.get_value() * x + c.get_value(),
                color=YELLOW,
                x_range=[-6, 6]  # Limita o desenho ao alcance dos eixos
            )
        )

        # --- Display da Equação ---
        # Função auxiliar para formatar o texto da equação
        def get_equation_tex():
            val_a = a.get_value()
            val_b = b.get_value()
            val_c = c.get_value()
            
            # Formatação para lidar com sinais de forma mais limpa
            sign_b = "+" if val_b >= 0 else "-"
            sign_c = "+" if val_c >= 0 else "-"
            
            # Cria a string LaTeX
            # f(x) = ax^2 + bx + c
            return MathTex(
                f"f(x) = {val_a:.1f}x^2 {sign_b} {abs(val_b):.1f}x {sign_c} {abs(val_c):.1f}",
                font_size=36
            ).to_corner(UL)

        equation_display = always_redraw(get_equation_tex)

        # --- Textos Explicativos ---
        # Título principal
        title = Text("Função Quadrática: Papel dos Coeficientes", font_size=32).to_edge(UP)
        
        # Legendas para cada fase
        label_a = Text("Coeficiente 'a': Abertura e Concavidade", font_size=24, color=RED).next_to(equation_display, DOWN)
        label_b = Text("Coeficiente 'b': Deslocamento Horizontal/Vértice", font_size=24, color=GREEN).next_to(equation_display, DOWN)
        label_c = Text("Coeficiente 'c': Deslocamento Vertical", font_size=24, color=BLUE).next_to(equation_display, DOWN)

        # --- Animação ---

        # 1. Introdução
        self.play(Create(axes), Write(labels))
        self.play(Write(title))
        self.play(Create(graph), Write(equation_display))
        self.wait(1)

        # 2. Variando o coeficiente 'a'
        # Destaque visual na equação para 'a' (conceitual, aqui via legenda)
        self.play(FadeIn(label_a))
        
        # a aumenta (mais estreita)
        self.play(a.animate.set_value(3), run_time=2)
        self.wait(0.5)
        # a inverte (concavidade para baixo)
        self.play(a.animate.set_value(-3), run_time=3)
        self.wait(0.5)
        # a volta ao normal
        self.play(a.animate.set_value(1), run_time=2)
        
        self.play(FadeOut(label_a))
        self.wait(0.5)

        # 3. Variando o coeficiente 'b'
        self.play(FadeIn(label_b))

        # b muda para positivo (vértice move para esquerda/baixo neste caso pois a=1)
        self.play(b.animate.set_value(4), run_time=2)
        self.wait(0.5)
        # b muda para negativo (vértice move para direita/baixo)
        self.play(b.animate.set_value(-4), run_time=3)
        self.wait(0.5)
        # b volta a zero
        self.play(b.animate.set_value(0), run_time=2)

        self.play(FadeOut(label_b))
        self.wait(0.5)

        # 4. Variando o coeficiente 'c'
        self.play(FadeIn(label_c))

        # c aumenta (sobe o gráfico)
        self.play(c.animate.set_value(3), run_time=2)
        self.wait(0.5)
        # c diminui (desce o gráfico)
        self.play(c.animate.set_value(-3), run_time=3)
        self.wait(0.5)
        # c volta a zero
        self.play(c.animate.set_value(0), run_time=2)

        self.play(FadeOut(label_c))
        
        # 5. Finalização
        self.wait(2)
        self.play(FadeOut(graph), FadeOut(axes), FadeOut(labels), FadeOut(equation_display), FadeOut(title))
