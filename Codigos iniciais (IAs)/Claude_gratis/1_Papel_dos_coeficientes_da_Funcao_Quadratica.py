from manim import *

class PapelCoeficientesFuncaoQuadratica(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-8, 8, 1],
            x_length=7,
            y_length=6,
            axis_config={"color": BLUE_D, "include_numbers": True, "font_size": 24},
            tips=False,
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        
        self.play(Create(axes), Write(axes_labels))
        self.wait(0.5)
        
        titulo = Text("Papel dos Coeficientes", font_size=36).to_edge(UP)
        self.play(Write(titulo))
        self.wait(0.5)
        
        a_inicial, b_inicial, c_inicial = 1, 0, 0
        
        formula = MathTex(
            "f(x) = ", "a", "x^2 + ", "b", "x + ", "c",
            font_size=40
        ).next_to(titulo, DOWN)
        self.play(Write(formula))
        self.wait(0.5)
        
        valores = MathTex(
            f"a = {a_inicial}", f"\\quad b = {b_inicial}", f"\\quad c = {c_inicial}",
            font_size=32
        ).next_to(formula, DOWN)
        self.play(Write(valores))
        self.wait(0.5)
        
        def criar_parabola(a, b, c):
            return axes.plot(
                lambda x: a * x**2 + b * x + c,
                x_range=[-5, 5],
                color=YELLOW
            )
        
        parabola = criar_parabola(a_inicial, b_inicial, c_inicial)
        self.play(Create(parabola))
        self.wait(1)
        
        texto_a = Text("Variando 'a': abertura e concavidade", font_size=28, color=RED).to_edge(DOWN)
        self.play(Write(texto_a))
        self.wait(0.5)
        
        valores_a = [0.5, 2, -1, -0.5, 1]
        a_atual = a_inicial
        
        for novo_a in valores_a:
            nova_parabola = criar_parabola(novo_a, b_inicial, c_inicial)
            novos_valores = MathTex(
                f"a = {novo_a}", f"\\quad b = {b_inicial}", f"\\quad c = {c_inicial}",
                font_size=32
            ).next_to(formula, DOWN)
            
            self.play(
                Transform(parabola, nova_parabola),
                Transform(valores, novos_valores),
                run_time=1.5
            )
            self.wait(0.8)
            a_atual = novo_a
        
        self.play(FadeOut(texto_a))
        self.wait(0.5)
        
        texto_b = Text("Variando 'b': deslocamento horizontal e vértice", font_size=28, color=GREEN).to_edge(DOWN)
        self.play(Write(texto_b))
        self.wait(0.5)
        
        valores_b = [-3, 2, -2, 0]
        b_atual = b_inicial
        
        for novo_b in valores_b:
            nova_parabola = criar_parabola(a_atual, novo_b, c_inicial)
            novos_valores = MathTex(
                f"a = {a_atual}", f"\\quad b = {novo_b}", f"\\quad c = {c_inicial}",
                font_size=32
            ).next_to(formula, DOWN)
            
            self.play(
                Transform(parabola, nova_parabola),
                Transform(valores, novos_valores),
                run_time=1.5
            )
            self.wait(0.8)
            b_atual = novo_b
        
        self.play(FadeOut(texto_b))
        self.wait(0.5)
        
        texto_c = Text("Variando 'c': deslocamento vertical", font_size=28, color=BLUE).to_edge(DOWN)
        self.play(Write(texto_c))
        self.wait(0.5)
        
        valores_c = [2, -3, 4, 0]
        
        for novo_c in valores_c:
            nova_parabola = criar_parabola(a_atual, b_atual, novo_c)
            novos_valores = MathTex(
                f"a = {a_atual}", f"\\quad b = {b_atual}", f"\\quad c = {novo_c}",
                font_size=32
            ).next_to(formula, DOWN)
            
            self.play(
                Transform(parabola, nova_parabola),
                Transform(valores, novos_valores),
                run_time=1.5
            )
            self.wait(0.8)
        
        self.play(FadeOut(texto_c))
        self.wait(1)
        
        self.play(
            FadeOut(parabola),
            FadeOut(valores),
            FadeOut(formula),
            FadeOut(titulo),
            FadeOut(axes),
            FadeOut(axes_labels)
        )
        self.wait(0.5)
