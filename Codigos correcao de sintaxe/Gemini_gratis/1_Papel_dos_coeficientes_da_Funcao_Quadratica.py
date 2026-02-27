from manim import *

class PapelDosCoeficientesQuadraticas(Scene):
    def construct(self):
        # 1. Configuração Inicial da Cena
        # Título da animação
        title = Text(
            "Papel dos Coeficientes da Função Quadrática",
            font_size=40,
            weight=BOLD
        ).to_edge(UP)
        self.play(FadeIn(title, shift=UP))
        self.wait(0.5)

        # Definição dos eixos cartesianos

        # CORREÇÃO HUMANA: BLUE_GREY não existe, alterado para BLUE
        self.axes = Axes(
            x_range=[-7, 7, 1],
            y_range=[-7, 7, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": BLUE, "stroke_width": 2}, #alterado para BLUE
            x_axis_config={"include_numbers": True},
            y_axis_config={"include_numbers": True},
        )
        self.axes.add_coordinates()
        self.play(Create(self.axes), run_time=1.5)

        # Trackers para os coeficientes a, b, c
        self.a_tracker = ValueTracker(1.0)
        self.b_tracker = ValueTracker(0.0)
        self.c_tracker = ValueTracker(0.0)

        # Função quadrática que se atualiza com os trackers
        def get_quadratic_function(x):
            return self.a_tracker.get_value() * x**2 + \
                   self.b_tracker.get_value() * x + \
                   self.c_tracker.get_value()

        # Parábola que se atualiza automaticamente sempre que os trackers mudam
        # CORREÇÃO HUMANA: O método 'get_graph' gerou erro com o argumento 'color'. Substituído por '.plot()', que é o padrão correto
        self.parabola = always_redraw(
            lambda: self.axes.plot(get_quadratic_function, x_range=[-6, 6], color=YELLOW)
        )

        # Texto da equação geral f(x) = ax^2 + bx + c
        self.equation_tex = MathTex("f(x) = ax^2 + bx + c", font_size=36)
        self.equation_tex.to_corner(UL)

        # Textos para os valores atuais de a, b, c, que se atualizam automaticamente
        self.a_value_tex = always_redraw(
            lambda: MathTex(f"a = {self.a_tracker.get_value():.2f}", font_size=30)
            .next_to(self.equation_tex, DOWN, aligned_edge=LEFT)
        )
        self.b_value_tex = always_redraw(
            lambda: MathTex(f"b = {self.b_tracker.get_value():.2f}", font_size=30)
            .next_to(self.a_value_tex, DOWN, aligned_edge=LEFT)
        )
        self.c_value_tex = always_redraw(
            lambda: MathTex(f"c = {self.c_tracker.get_value():.2f}", font_size=30)
            .next_to(self.b_value_tex, DOWN, aligned_edge=LEFT)
        )
        
        # Exibir a parábola inicial e os detalhes da função
        self.play(
            Create(self.parabola),
            FadeIn(self.equation_tex),
            FadeIn(self.a_value_tex),
            FadeIn(self.b_value_tex),
            FadeIn(self.c_value_tex),
            run_time=2
        )
        self.wait(1)

        # Funções auxiliares para destacar/desdestacar coeficientes
        def highlight_coeff(coeff_char, color):
            return self.equation_tex.get_part_by_tex(coeff_char).animate.set_color(color)

        def unhighlight_coeff(coeff_char):
            return self.equation_tex.get_part_by_tex(coeff_char).animate.set_color(WHITE)


        # 2. Variando 'a': Concavidade e Abertura
        description_a = Text(
            "1. Variando 'a': Concavidade e Abertura",
            font_size=32
        ).to_corner(UR)
        self.play(FadeIn(description_a, shift=UP))
        self.wait(0.5)

        # Destacar 'a' na equação e seu valor numérico
        self.play(
            highlight_coeff('a', RED),
            self.a_value_tex.animate.set_color(RED)
        )
        self.wait(0.5)

        # Animações de 'a' (positivo e negativo, e variação de magnitude)
        self.play(self.a_tracker.animate.set_value(2.0), run_time=2)   # Mais fechada
        self.play(self.a_tracker.animate.set_value(0.5), run_time=2)   # Mais aberta
        
        self.play(self.a_tracker.animate.set_value(-1.0), run_time=3)  # Concavidade para baixo
        self.play(self.a_tracker.animate.set_value(-2.0), run_time=2)  # Concavidade para baixo e mais fechada
        
        # Resetar 'a' para o valor padrão
        self.play(self.a_tracker.animate.set_value(1.0), run_time=3)
        self.wait(0.5)

        # Desdestacar 'a' e remover descrição
        self.play(
            unhighlight_coeff('a'),
            self.a_value_tex.animate.set_color(WHITE),
            FadeOut(description_a, shift=DOWN)
        )
        self.wait(1)

        # 3. Variando 'b': Deslocamento Horizontal e Vértice
        description_b = Text(
            "2. Variando 'b': Deslocamento Horizontal e Vértice",
            font_size=32
        ).to_corner(UR)
        self.play(FadeIn(description_b, shift=UP))
        self.wait(0.5)

        # Destacar 'b' na equação e seu valor numérico
        self.play(
            highlight_coeff('b', RED),
            self.b_value_tex.animate.set_color(RED)
        )
        self.wait(0.5)

        # Animações de 'b' (deslocamento horizontal)
        self.play(self.b_tracker.animate.set_value(3.0), run_time=3)  # Desloca a parábola para a esquerda
        self.play(self.b_tracker.animate.set_value(-3.0), run_time=3) # Desloca a parábola para a direita
        
        # Resetar 'b'
        self.play(self.b_tracker.animate.set_value(0.0), run_time=2)
        self.wait(0.5)

        # Desdestacar 'b' e remover descrição
        self.play(
            unhighlight_coeff('b'),
            self.b_value_tex.animate.set_color(WHITE),
            FadeOut(description_b, shift=DOWN)
        )
        self.wait(1)

        # 4. Variando 'c': Deslocamento Vertical
        description_c = Text(
            "3. Variando 'c': Deslocamento Vertical",
            font_size=32
        ).to_corner(UR)
        self.play(FadeIn(description_c, shift=UP))
        self.wait(0.5)

        # Destacar 'c' na equação e seu valor numérico
        self.play(
            highlight_coeff('c', RED),
            self.c_value_tex.animate.set_color(RED)
        )
        self.wait(0.5)

        # Animações de 'c' (deslocamento vertical)
        self.play(self.c_tracker.animate.set_value(2.0), run_time=3)  # Desloca a parábola para cima
        self.play(self.c_tracker.animate.set_value(-2.0), run_time=3) # Desloca a parábola para baixo
        
        # Resetar 'c'
        self.play(self.c_tracker.animate.set_value(0.0), run_time=2)
        self.wait(0.5)

        # Desdestacar 'c' e remover descrição
        self.play(
            unhighlight_coeff('c'),
            self.c_value_tex.animate.set_color(WHITE),
            FadeOut(description_c, shift=DOWN)
        )
        self.wait(2)

        # Finalização da Cena
        self.play(
            FadeOut(self.axes),
            FadeOut(self.parabola),
            FadeOut(self.equation_tex),
            FadeOut(self.a_value_tex),
            FadeOut(self.b_value_tex),
            FadeOut(self.c_value_tex),
            FadeOut(title)
        )
