from manim import *

class PlatonicSolidsEuler(ThreeDScene):
    def construct(self):
        # 1. Configuração inicial da cena 3D e câmera
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES, distance=10)
        self.camera.background_color = BLACK

        # Título da animação
        title = Text("Poliedros de Platão e a Fórmula de Euler", font_size=50, color=WHITE).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Dados dos Poliedros de Platão (Nome, chave para vértices/faces, V, A, F)
        # CORRECAO HUMANA: Removemos a chave 'solid_key' que era usada para buscar dados globais inexistentes
        # e usamos classes diretas do Manim para criar os sólidos, armazenando os objetos diretamente no dicionário
        solids_data = {
            "Tetraedro": {"obj": Tetrahedron(), "V": 4, "A": 6, "F": 4},
            "Cubo": {"obj": Cube(side_length=2), "V": 8, "A": 12, "F": 6},
            "Octaedro": {"obj": Octahedron(), "V": 6, "A": 12, "F": 8},
            "Dodecaedro": {"obj": Dodecahedron(), "V": 20, "A": 30, "F": 12},
            "Icosaedro": {"obj": Icosahedron(), "V": 12, "A": 30, "F": 20},
        }

        # Grupo para armazenar as fórmulas de Euler de cada sólido para a síntese final
        euler_formula_results = VGroup()

        # Loop para construir e analisar cada poliedro
        for solid_name, data in solids_data.items():
            V, A, F = data["V"], data["A"], data["F"]
            # solid_key = data["solid_key"] # REMOVIDO

            # Exibir o nome do poliedro atual
            solid_title = Text(solid_name, font_size=40, color=WHITE).to_edge(UL).shift(RIGHT*2)
            self.play(FadeIn(solid_title, shift=UP))
            self.wait(0.5)

            # Criar o objeto 3D do poliedro
            # CORRECAO HUMANA: Instanciamos diretamente o objeto salvo no dicionario
            solid_mobject = data["obj"]
            
            solid_mobject.scale(1.2).move_to(ORIGIN) # Ajusta tamanho e posição
            solid_mobject.set_color(BLUE_D) # Define uma cor para o sólido

            # Animação de criação e rotação do sólido
            self.play(Create(solid_mobject), run_time=1.5)
            # CORREÇÃO HUMANA: O método 'always_rotate' não existe no objeto. Substituído por um updater padrão
            solid_mobject.add_updater(lambda m, dt: m.rotate(dt * PI / 5, axis=UP))
            self.add(solid_mobject)
            self.wait(1)

            # Exibir o número de Vértices (V), Arestas (A) e Faces (F)
            v_text = MathTex(f"V = {V}", color=YELLOW).to_edge(UL).shift(DOWN*0.5 + RIGHT*2)
            a_text = MathTex(f"A = {A}", color=BLUE).next_to(v_text, DOWN, buff=0.2)
            f_text = MathTex(f"F = {F}", color=GREEN).next_to(a_text, DOWN, buff=0.2)
            vaf_group = VGroup(v_text, a_text, f_text)

            self.play(Write(vaf_group, lag_ratio=0.3))
            self.wait(1)

            # Animar a expressão V - A + F = 2 para o poliedro atual

            # Cria placeholders para os símbolos V, A, F, operadores e o ponto de interrogação
            v_expr = MathTex("V", color=YELLOW)
            op1_expr = MathTex("-")
            a_expr = MathTex("A", color=BLUE)
            op2_expr = MathTex("+")
            f_expr = MathTex("F", color=GREEN)
            eq_expr = MathTex("=")
            q_expr = MathTex("?", color=RED) 

            # Agrupa e posiciona a expressão na tela
            euler_expression_group = VGroup(
                v_expr, op1_expr, a_expr, op2_expr, f_expr, eq_expr, q_expr
            ).arrange(RIGHT, buff=0.1).next_to(f_text, DOWN, buff=0.5).shift(RIGHT * 0.5)

            # Escreve os símbolos e operadores
            self.play(
                Write(VGroup(v_expr, op1_expr, a_expr, op2_expr, f_expr, eq_expr)),
                FadeIn(q_expr)
            )
            self.wait(0.5)

            # Transforma os valores de V, A, F para as posições na expressão
            v_val_text = MathTex(str(V)).set_color(YELLOW).move_to(v_expr)
            a_val_text = MathTex(str(A)).set_color(BLUE).move_to(a_expr)
            f_val_text = MathTex(str(F)).set_color(GREEN).move_to(f_expr)

            self.play(
                TransformFromCopy(v_text[2:], v_val_text), # Copia o valor de V=X para X na expressão
                TransformFromCopy(a_text[2:], a_val_text), # Copia o valor de A=Y para Y na expressão
                TransformFromCopy(f_text[2:], f_val_text), # Copia o valor de F=Z para Z na expressão
                FadeOut(v_expr, a_expr, f_expr), # Esconde os símbolos originais V, A, F
            )
            self.wait(0.5)

            # Anima a transformação do '?' para '2'
            result_2 = MathTex("2").move_to(q_expr).set_color(WHITE)
            self.play(Transform(q_expr, result_2)) # 'q_expr' agora se refere ao mobject 'result_2'
            self.wait(1)

            # Armazena uma cópia da expressão V - A + F = 2 para a síntese final
            # Este VGroup representa o estado final da fórmula na tela para este sólido
            current_solid_euler_expression_mobjects = VGroup(
                v_val_text, op1_expr, a_val_text, op2_expr, f_val_text, eq_expr, q_expr
            )
            
            # Adiciona uma cópia ao grupo de resultados para a síntese final
            euler_formula_results.add(current_solid_euler_expression_mobjects.copy())

            # Fade out de todos os elementos relacionados ao poliedro atual
            self.play(
                FadeOut(solid_mobject, shift=DOWN),
                FadeOut(solid_title, shift=UP),
                FadeOut(vaf_group, shift=LEFT),
                FadeOut(current_solid_euler_expression_mobjects, shift=RIGHT),
            )
            self.remove(solid_mobject) # Remove o sólido da cena, parando sua rotação
            self.wait(0.5)

        # 3. Síntese final da Fórmula de Euler
        self.play(FadeOut(title)) # Esconde o título inicial
        final_formula_title = Text("Fórmula de Euler para Poliedros Convexos:", font_size=45, color=WHITE).to_edge(UP)
        self.play(Write(final_formula_title))

        # Organiza e exibe todas as fórmulas de Euler dos poliedros apresentados
        euler_formula_results.arrange(DOWN, buff=0.4).move_to(ORIGIN)
        self.play(FadeIn(euler_formula_results, shift=DOWN, lag_ratio=0.5))
        self.wait(1)

        # Exibe e destaca a fórmula geral V - A + F = 2
        general_formula = MathTex("V - A + F = 2", font_size=70, color=WHITE).move_to(DOWN*2.5)
        general_formula.set_color_by_tex_to_color_map({"V": YELLOW, "A": BLUE, "F": GREEN})
        self.play(Write(general_formula))
        self.wait(3)

        # Finaliza a animação
        self.play(FadeOut(final_formula_title, general_formula, euler_formula_results))
        self.wait(1)
