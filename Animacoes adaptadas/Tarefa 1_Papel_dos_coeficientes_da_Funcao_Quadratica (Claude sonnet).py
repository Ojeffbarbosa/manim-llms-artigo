from manim import *

class PapelCoeficientesFuncaoQuadratica(Scene):
    def construct(self):
        # 1. Criação dos eixos ajustados e reposicionados à esquerda
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-8, 12, 2],
            x_length=6,
            y_length=6,
            axis_config={"color": WHITE, "include_numbers": True, "font_size": 24},
            tips=True,
        ).to_edge(LEFT, buff=0.8)
        
        # Reposicionando rótulos dos eixos manualmente conforme solicitado
        x_label = MathTex("x").next_to(axes.x_axis.get_end(), DOWN, buff=0.2)
        y_label = MathTex("f(x)").next_to(axes.y_axis.get_end(), LEFT, buff=0.2)
        axes_labels = VGroup(x_label, y_label)
        
        self.play(Create(axes), Write(axes_labels))
        self.wait(0.5)
        
        # 2. Textos e fórmulas posicionados à direita em coluna
        grupo_textos = VGroup()
        titulo = Text("Papel dos Coeficientes", font_size=32).set_color(YELLOW)
        
        formula = MathTex(
            "f(x) = a x^2 + b x + c",
            font_size=40
        )
        
        a_inicial, b_inicial, c_inicial = 1, 0, 0
        valores = MathTex(
            f"a = {a_inicial}", f"\\quad b = {b_inicial}", f"\\quad c = {c_inicial}",
            font_size=32
        )
        
        grupo_textos.add(titulo, formula, valores).arrange(DOWN, buff=0.8)
        # Posicionamos para que o titulo e o bloco fiquem ancorados na parte superior direita
        grupo_textos.to_edge(RIGHT, buff=1).to_edge(UP, buff=1)
        
        self.play(Write(titulo))
        self.wait(0.5)
        self.play(Write(formula))
        self.wait(0.5)
        self.play(Write(valores))
        self.wait(0.5)
        
        # Função para criar a parábola, limitando as bordas de plot nas dimensões adequadas
        def criar_parabola(a, b, c):
            return axes.plot(
                lambda x: a * x**2 + b * x + c,
                x_range=[-5, 5],
                color=YELLOW
            )
        
        parabola = criar_parabola(a_inicial, b_inicial, c_inicial)
        self.play(Create(parabola))
        self.wait(1)
        
        # === VARIANDO A ===
        texto_a = Text("Variando 'a':\nabertura e concavidade", font_size=28, color=RED)
        texto_a.next_to(grupo_textos, DOWN, buff=1)
        self.play(Write(texto_a))
        self.wait(0.5)
        
        explicacao_a = MathTex("a > 0: \\text{ concavidade para cima}", font_size=28, color=RED).next_to(texto_a, DOWN, buff=0.5)
        self.play(Write(explicacao_a))
        
        valores_a = [0.5, 2, -1, -0.5, 1]
        a_atual = a_inicial
        
        for novo_a in valores_a:
            nova_parabola = criar_parabola(novo_a, b_inicial, c_inicial)
            novos_valores = MathTex(
                f"a = {novo_a}", f"\\quad b = {b_inicial}", f"\\quad c = {c_inicial}",
                font_size=32
            ).next_to(formula, DOWN, buff=0.8)
            
            if novo_a > 0:
                novo_explicacao_a = MathTex("a > 0: \\text{ concavidade para cima}", font_size=28, color=RED).move_to(explicacao_a)
            else:
                novo_explicacao_a = MathTex("a < 0: \\text{ concavidade para baixo}", font_size=28, color=RED).move_to(explicacao_a)
            
            self.play(
                Transform(parabola, nova_parabola),
                Transform(valores, novos_valores),
                Transform(explicacao_a, novo_explicacao_a),
                run_time=1.5
            )
            self.wait(0.8)
            a_atual = novo_a
        
        self.play(FadeOut(texto_a), FadeOut(explicacao_a))
        self.wait(0.5)
        
        # === VARIANDO B ===
        texto_b = Text("Variando 'b':\ninclinação no eixo y\ne posição do vértice", font_size=28, color=GREEN)
        texto_b.next_to(grupo_textos, DOWN, buff=1)
        self.play(Write(texto_b))
        self.wait(0.5)
        
        explicacao_b = MathTex("b = 0: \\text{ vértice no eixo } y", font_size=28, color=GREEN).next_to(texto_b, DOWN, buff=0.5)
        self.play(Write(explicacao_b))
        
        #tracker para manter a parabola vértice e tangente sincronizados a cada frame
        b_tracker = ValueTracker(b_inicial)

        tangente = always_redraw(lambda: axes.plot(
            lambda x: b_tracker.get_value() * x + c_inicial,
            x_range=[-3, 3],
            color=ORANGE
        ))
        
        parabola_b = always_redraw(lambda: axes.plot(
            lambda x: a_atual * x**2 + b_tracker.get_value() * x + c_inicial,
            x_range=[-5, 5],
            color=YELLOW
        ))
        
        vertice = always_redraw(lambda: VGroup(
            Dot(axes.c2p(-b_tracker.get_value() / (2 * a_atual), a_atual * (-b_tracker.get_value() / (2 * a_atual))**2 + b_tracker.get_value() * (-b_tracker.get_value() / (2 * a_atual)) + c_inicial), color=WHITE),
            MathTex("V", font_size=24).next_to(axes.c2p(-b_tracker.get_value() / (2 * a_atual), a_atual * (-b_tracker.get_value() / (2 * a_atual))**2 + b_tracker.get_value() * (-b_tracker.get_value() / (2 * a_atual)) + c_inicial), DOWN, buff=0.1)
        ))
        
        #substitui a parabola estatica pela ancorada ao tracker
        self.add(parabola_b)
        self.remove(parabola)
        
        self.play(Create(tangente))
        self.play(FadeIn(vertice))
        
        valores_b = [-3, 2, -2, 0]
        
        for novo_b in valores_b:            
            novos_valores = MathTex(
                f"a = {a_atual}", f"\\quad b = {novo_b}", f"\\quad c = {c_inicial}",
                font_size=32
            ).next_to(formula, DOWN, buff=0.8)
            
            if novo_b > 0:
                novo_explicacao_b = MathTex("b > 0: \\text{ corta o eixo y subindo}", font_size=28, color=GREEN).move_to(explicacao_b)
            elif novo_b < 0:
                novo_explicacao_b = MathTex("b < 0: \\text{ corta o eixo y descendo}", font_size=28, color=GREEN).move_to(explicacao_b)
            else:
                novo_explicacao_b = MathTex("b = 0: \\text{ vértice no eixo } y", font_size=28, color=GREEN).move_to(explicacao_b)
            
            self.play(
                b_tracker.animate.set_value(novo_b),
                Transform(valores, novos_valores),
                Transform(explicacao_b, novo_explicacao_b),
                run_time=1.5
            )
            self.wait(0.8)
            
        b_atual = b_tracker.get_value()

        parabola = axes.plot(lambda x: a_atual * x**2 + b_atual * x + c_inicial, x_range=[-5, 5], color=YELLOW)
        self.add(parabola)
        self.remove(parabola_b)
        
        self.play(FadeOut(texto_b), FadeOut(tangente), FadeOut(vertice), FadeOut(explicacao_b))
        self.wait(0.5)
        
        # === VARIANDO C ===
        texto_c = Text("Variando 'c':\ndeslocamento vertical", font_size=28, color=BLUE)
        texto_c.next_to(grupo_textos, DOWN, buff=1)
        self.play(Write(texto_c))
        self.wait(0.5)
        
        explicacao_c = MathTex("c = 0: \\text{ passa pela origem}", font_size=28, color=BLUE).next_to(texto_c, DOWN, buff=0.5)
        self.play(Write(explicacao_c))
        
        valores_c = [2, -3, 4, 0]
        
        for novo_c in valores_c:
            nova_parabola = criar_parabola(a_atual, b_atual, novo_c)
            novos_valores = MathTex(
                f"a = {a_atual}", f"\\quad b = {b_atual}", f"\\quad c = {novo_c}",
                font_size=32
            ).next_to(formula, DOWN, buff=0.8)
            
            if novo_c > 0:
                novo_explicacao_c = MathTex("c > 0: \\text{ corta eixo y acima da origem}", font_size=28, color=BLUE).move_to(explicacao_c)
            elif novo_c < 0:
                novo_explicacao_c = MathTex("c < 0: \\text{ corta eixo y abaixo da origem}", font_size=28, color=BLUE).move_to(explicacao_c)
            else:
                novo_explicacao_c = MathTex("c = 0: \\text{ passa pela origem}", font_size=28, color=BLUE).move_to(explicacao_c)
                
            self.play(
                Transform(parabola, nova_parabola),
                Transform(valores, novos_valores),
                Transform(explicacao_c, novo_explicacao_c),
                run_time=1.5
            )
            self.wait(0.8)
        
        self.play(FadeOut(texto_c), FadeOut(explicacao_c))
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
