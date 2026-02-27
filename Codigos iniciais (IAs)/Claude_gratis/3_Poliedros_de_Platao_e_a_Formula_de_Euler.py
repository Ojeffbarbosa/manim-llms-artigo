from manim import *

class PoliedrosPlataoEuler(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=70 * DEGREES, theta=30 * DEGREES)
        
        titulo = Text("Poliedros de Platão", font_size=48, color=BLUE)
        titulo.to_edge(UP)
        self.add_fixed_in_frame_mobjects(titulo)
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))
        
        poliedros_data = [
            ("Tetraedro", Tetrahedron(), 4, 6, 4, YELLOW),
            ("Cubo", Cube(), 8, 12, 6, BLUE),
            ("Octaedro", Octahedron(), 6, 12, 8, GREEN),
            ("Dodecaedro", Dodecahedron(), 20, 30, 12, RED),
            ("Icosaedro", Icosahedron(), 12, 30, 20, PURPLE)
        ]
        
        for nome, poliedro, V, A, F, cor in poliedros_data:
            self.animar_poliedro(nome, poliedro, V, A, F, cor)
        
        self.animar_formula_euler()
    
    def animar_poliedro(self, nome, poliedro, V, A, F, cor):
        poliedro.set_fill(cor, opacity=0.7)
        poliedro.set_stroke(WHITE, width=2)
        poliedro.scale(1.5)
        
        nome_text = Text(nome, font_size=40, color=cor)
        nome_text.to_edge(UP)
        self.add_fixed_in_frame_mobjects(nome_text)
        
        self.play(Write(nome_text), Create(poliedro), run_time=2)
        self.begin_ambient_camera_rotation(rate=0.3)
        self.wait(1)
        self.stop_ambient_camera_rotation()
        
        vertices_text = MathTex(f"V = {V}", font_size=36, color=YELLOW)
        arestas_text = MathTex(f"A = {A}", font_size=36, color=GREEN)
        faces_text = MathTex(f"F = {F}", font_size=36, color=BLUE)
        
        info_group = VGroup(vertices_text, arestas_text, faces_text)
        info_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        info_group.to_corner(UL, buff=0.5)
        info_group.shift(DOWN * 0.8)
        
        self.add_fixed_in_frame_mobjects(vertices_text, arestas_text, faces_text)
        
        self.play(Write(vertices_text))
        self.wait(0.5)
        self.play(Write(arestas_text))
        self.wait(0.5)
        self.play(Write(faces_text))
        self.wait(1)
        
        formula = MathTex(f"{V}", "-", f"{A}", "+", f"{F}", "=", font_size=40)
        formula.to_edge(DOWN, buff=1)
        self.add_fixed_in_frame_mobjects(formula)
        self.play(Write(formula))
        self.wait(0.5)
        
        resultado = V - A + F
        resultado_text = MathTex(f"{resultado}", font_size=40, color=RED)
        resultado_text.next_to(formula, RIGHT, buff=0.2)
        self.add_fixed_in_frame_mobjects(resultado_text)
        
        self.play(Write(resultado_text))
        destaque = SurroundingRectangle(resultado_text, color=RED, buff=0.15)
        self.add_fixed_in_frame_mobjects(destaque)
        self.play(Create(destaque))
        self.wait(2)
        
        self.play(
            FadeOut(poliedro),
            FadeOut(nome_text),
            FadeOut(vertices_text),
            FadeOut(arestas_text),
            FadeOut(faces_text),
            FadeOut(formula),
            FadeOut(resultado_text),
            FadeOut(destaque)
        )
        self.wait(0.5)
    
    def animar_formula_euler(self):
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
        self.wait(0.5)
        
        titulo_final = Text("Fórmula de Euler", font_size=48, color=GOLD)
        titulo_final.to_edge(UP, buff=0.8)
        self.add_fixed_in_frame_mobjects(titulo_final)
        self.play(Write(titulo_final))
        self.wait()
        
        formula_euler = MathTex("V", "-", "A", "+", "F", "=", "2", font_size=72)
        formula_euler[0].set_color(YELLOW)
        formula_euler[2].set_color(GREEN)
        formula_euler[4].set_color(BLUE)
        formula_euler[6].set_color(RED)
        
        self.add_fixed_in_frame_mobjects(formula_euler)
        self.play(Write(formula_euler))
        self.wait(1)
        
        caixa = SurroundingRectangle(formula_euler, color=GOLD, buff=0.3, stroke_width=6)
        self.add_fixed_in_frame_mobjects(caixa)
        self.play(Create(caixa))
        self.wait(1)
        
        descricao = Text("Para todo poliedro convexo", font_size=32, color=WHITE)
        descricao.next_to(formula_euler, DOWN, buff=0.8)
        self.add_fixed_in_frame_mobjects(descricao)
        self.play(FadeIn(descricao))
        self.wait(2)
        
        self.play(
            FadeOut(titulo_final),
            FadeOut(formula_euler),
            FadeOut(caixa),
            FadeOut(descricao)
        )
        self.wait()
