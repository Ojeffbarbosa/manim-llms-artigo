from manim import *

class PythagoreanTheoremDecomposition(Scene):
    def construct(self):
        # 1. Configuração do triângulo e dos quadrados
        a_len = 4  # Comprimento do cateto 'a' (horizontal)
        b_len = 3  # Comprimento do cateto 'b' (vertical)
        c_len = np.sqrt(a_len**2 + b_len**2) # Comprimento da hipotenusa 'c'

        # Define os vértices para o triângulo retângulo
        # Coloca o ângulo reto na ORIGEM para facilitar a construção dos quadrados
        # Move o setup ligeiramente para a esquerda e para baixo para centralizar o quadrado da hipotenusa
        base_offset = LEFT * 3.5 + DOWN * 1.5
        triangle_v1 = ORIGIN + base_offset # Vértice do ângulo reto
        triangle_v2 = RIGHT * a_len + base_offset # Vértice ao longo do cateto 'a'
        triangle_v3 = UP * b_len + base_offset # Vértice ao longo do cateto 'b'

        triangle = Polygon(triangle_v1, triangle_v2, triangle_v3,
                           color=WHITE, fill_opacity=0.3, z_index=1)

        # Quadrado sobre o cateto 'a' (horizontal), construído para baixo
        sq_a = Polygon(triangle_v1, triangle_v2,
                       triangle_v2 + DOWN * a_len,
                       triangle_v1 + DOWN * a_len,
                       color=BLUE_A, fill_opacity=0.8)

        # Quadrado sobre o cateto 'b' (vertical), construído para a esquerda
        sq_b = Polygon(triangle_v1, triangle_v3,
                       triangle_v3 + LEFT * b_len,
                       triangle_v1 + LEFT * b_len,
                       color=YELLOW_A, fill_opacity=0.8)

        # Quadrado sobre a hipotenusa
        # Vetor de triangle_v2 para triangle_v3
        hyp_vec = triangle_v3 - triangle_v2
        # Vetor perpendicular para construir o quadrado para fora (rotação no sentido horário por -PI/2)
        perp_hyp_vec = rotate_vector(hyp_vec, -PI/2)
        sq_c = Polygon(triangle_v2, triangle_v3,
                       triangle_v3 + perp_hyp_vec,
                       triangle_v2 + perp_hyp_vec,
                       color=GREY_B, fill_opacity=0.4, stroke_color=WHITE, stroke_width=2)

        # 2. Desenho inicial
        self.play(Create(triangle), run_time=1.5)
        self.play(Create(sq_a), Create(sq_b), Create(sq_c), run_time=2)
        self.wait(1)

        # 3. Decomposição usando a Dissecação de Perigal
        # Assumimos a_len > b_len (4 > 3). Então sq_a (azul) é cortado em 4 peças, sq_b (amarelo) é uma peça.

        # Define as 5 peças
        piece_b = sq_b.copy().set_z_index(2) # O próprio quadrado amarelo é uma peça

        # Calcula o centro de sq_a para os cortes
        sq_a_center = sq_a.get_center()

        # Calcula as direções das linhas de corte (paralelas e perpendiculares à hipotenusa)
        unit_hyp_dir = normalize(hyp_vec)
        # Vetor unitário perpendicular (rotacionado no sentido anti-horário de unit_hyp_dir)
        unit_perp_dir = rotate_vector(unit_hyp_dir, PI/2)

        # Estende as linhas de corte além do quadrado para garantir interseções limpas
        cut_line_len = a_len * 1.5 # Comprimento arbitrário, apenas precisa ser longo o suficiente

        # Cria as duas linhas de corte
        cut_line1 = Line(sq_a_center - unit_hyp_dir * cut_line_len / 2,
                         sq_a_center + unit_hyp_dir * cut_line_len / 2,
                         stroke_color=RED, stroke_width=2, z_index=3)
        cut_line2 = Line(sq_a_center - unit_perp_dir * cut_line_len / 2,
                         sq_a_center + unit_perp_dir * cut_line_len / 2,
                         stroke_color=RED, stroke_width=2, z_index=3)

        self.play(Create(cut_line1), Create(cut_line2))
        self.wait(0.5)

        # Pega os vértices de sq_a para definições de polígonos mais claras
        sq_a_vtx = sq_a.get_vertices()
        # Ordem dos vértices: TL, TR, BR, BL para sq_a conforme definido
        sq_a_tl, sq_a_tr, sq_a_br, sq_a_bl = sq_a_vtx[0], sq_a_vtx[1], sq_a_vtx[2], sq_a_vtx[3]

        # Calcula manualmente os 4 pontos de interseção específicos na borda de sq_a
        # Estes cálculos são sensíveis a `a_len`, `b_len` e `base_offset` iniciais
        # Eles foram derivados para a_len=4, b_len=3 e sq_a construído para baixo a partir da origem.
        # Coordenadas globais (x,y,z) para esses pontos:
        p_top_cut = np.array([3.5, 0, 0]) + base_offset # Interseção de cut_line2 com a borda superior de sq_a
        p_right_cut = np.array([4, -3.5, 0]) + base_offset # Interseção de cut_line1 com a borda direita de sq_a
        p_bottom_cut = np.array([0.5, -4, 0]) + base_offset # Interseção de cut_line2 com a borda inferior de sq_a
        p_left_cut = np.array([0, -0.5, 0]) + base_offset # Interseção de cut_line1 com a borda esquerda de sq_a
        
        # Cria as 4 peças de sq_a (quadriláteros ao redor do centro `sq_a_center`)
        piece_a1 = Polygon(sq_a_tl, p_top_cut, sq_a_center, p_left_cut, color=BLUE_A, fill_opacity=0.8, z_index=2)
        piece_a2 = Polygon(p_top_cut, sq_a_tr, p_right_cut, sq_a_center, color=BLUE_A, fill_opacity=0.8, z_index=2)
        piece_a3 = Polygon(p_right_cut, sq_a_br, p_bottom_cut, sq_a_center, color=BLUE_A, fill_opacity=0.8, z_index=2)
        piece_a4 = Polygon(p_bottom_cut, sq_a_bl, p_left_cut, sq_a_center, color=BLUE_A, fill_opacity=0.8, z_index=2)

        pieces_a_group = VGroup(piece_a1, piece_a2, piece_a3, piece_a4)
        all_pieces = VGroup(piece_a1, piece_a2, piece_a3, piece_a4, piece_b)

        # Esconde os quadrados originais e o triângulo, mostrando as peças cortadas
        self.play(FadeOut(sq_a, target_opacity=0), FadeOut(sq_b, target_opacity=0), FadeOut(triangle, target_opacity=0),
                  AnimationGroup(
                      Create(piece_a1), Create(piece_a2), Create(piece_a3), Create(piece_a4), Create(piece_b),
                      run_time=2, lag_ratio=0.1
                  ))
        self.play(FadeOut(cut_line1), FadeOut(cut_line2))
        self.wait(0.5)

        # 4. Anima a reorganização para preencher sq_c
        # Move toda a composição (peças e sq_c) para o centro da cena para melhor visualização
        center_sq_c_target_position = ORIGIN + UP*0.5 
        offset_to_scene_center = center_sq_c_target_position - sq_c.get_center()

        self.play(
            all_pieces.animate.shift(offset_to_scene_center),
            sq_c.animate.shift(offset_to_scene_center)
        )
        self.wait(1)

        # Determina o ângulo de rotação alvo para todas as peças se alinharem com sq_c
        # sq_a (peças azuis) era originalmente horizontal (ângulo 0). sq_b (peça amarela) era vertical (ângulo PI/2).
        # A orientação de sq_c é `Line(triangle_v2, triangle_v3).get_angle() - PI/2`.
        target_orientation_angle = Line(triangle_v2, triangle_v3).get_angle() - PI/2

        # Cria versões alvo das peças para animar `become`
        # Alvo para piece_b (quadrado amarelo)
        target_piece_b_for_anim = piece_b.copy()
        target_piece_b_for_anim.rotate(target_orientation_angle - piece_b.get_angle())
        target_piece_b_for_anim.move_to(sq_c.get_center())

        # Alvos para as 4 peças de sq_a (azul)
        # O vértice interno delas (que era `sq_a_center` em sua forma inicial) se alinhará
        # com os respectivos cantos de `target_piece_b_for_anim`.
        
        # Cria as animações para cada peça
        animations = [
            piece_b.animate.become(target_piece_b_for_anim)
        ]

        # Anima cada piece_a para sua posição alvo ao redor do quadrado amarelo central
        # Para cada piece_a, rotaciona-a em torno de seu próprio vértice `sq_a_center`, depois a move.
        # O ponto `sq_a_center` da peça é efetivamente seu pivô interno para transformação.
        
        # O ponto `sq_a_center` (onde as 4 peças se encontram) está agora em `sq_a_center + offset_to_scene_center`.
        # Os alvos para este ponto são os 4 cantos do `target_piece_b_for_anim`.
        target_corners_for_a_pieces = [
            target_piece_b_for_anim.get_corner(UR), # sq_a_center da piece_a1 vai aqui
            target_piece_b_for_anim.get_corner(UL), # sq_a_center da piece_a2 vai aqui
            target_piece_b_for_anim.get_corner(DR), # sq_a_center da piece_a3 vai aqui
            target_piece_b_for_anim.get_corner(DL)  # sq_a_center da piece_a4 vai aqui
        ]

        # Iterar sobre as peças do grupo 'a' e criar suas animações
        for i, p_a in enumerate(pieces_a_group):
            # Cria uma cópia da peça para a animação `become`
            target_p_a = p_a.copy()
            
            # Ponto de rotação atual da peça (seu `sq_a_center` original, mas transladado para o centro da cena)
            current_sq_a_center_global = sq_a_center + offset_to_scene_center
            
            # Aplica a rotação ao redor deste ponto
            target_p_a.rotate(target_orientation_angle, about_point=current_sq_a_center_global)
            
            # Calcula o vetor de translação: do ponto de rotação (que já foi transladado)
            # até o canto alvo correspondente da `target_piece_b_for_anim`
            shift_vector = target_corners_for_a_pieces[i] - current_sq_a_center_global
            target_p_a.shift(shift_vector)
            
            animations.append(p_a.animate.become(target_p_a))

        self.play(AnimationGroup(*animations, lag_ratio=0.1, run_time=3))
        self.wait(1)

        # Adiciona texto para confirmar o teorema
        theorem_text = MathTex("a^2 + b^2 = c^2").to_edge(UP).shift(LEFT * 2)
        self.play(Write(theorem_text))
        self.wait(2)
