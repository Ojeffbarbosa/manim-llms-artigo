from manim import *

class PythagorasDecomposition(Scene):
    def construct(self):
        # --- Configuração Inicial e Geometria ---
        
        # Dimensões do triângulo: cateto a=4, cateto b=3, hipotenusa c=5
        # Coordenadas baseadas em um ângulo reto na origem para facilitar, depois transladamos
        # A (4,0), B (0,3), C (0,0) -> C é o ângulo reto
        p_C = ORIGIN
        p_A = RIGHT * 4
        p_B = UP * 3
        
        # Grupo para conter todo o diagrama inicial e centralizá-lo
        diagram = VGroup()
        
        # 1. Triângulo Retângulo
        triangle = Polygon(p_C, p_A, p_B, color=WHITE, fill_opacity=0.5, stroke_width=2)
        diagram.add(triangle)
        
        # 2. Quadrado sobre o cateto 'a' (4 unidades, horizontal)
        # Vértices: (0,0), (4,0), (4,-4), (0,-4)
        square_a = Square(side_length=4, color=BLUE, fill_opacity=0.5)
        square_a.move_to(p_C + RIGHT*2 + DOWN*2) # Centro em (2, -2)
        diagram.add(square_a)
        
        # 3. Quadrado sobre o cateto 'b' (3 unidades, vertical)
        # Vértices: (0,0), (0,3), (-3,3), (-3,0)
        square_b = Square(side_length=3, color=RED, fill_opacity=0.5)
        square_b.move_to(p_C + LEFT*1.5 + UP*1.5) # Centro em (-1.5, 1.5)
        diagram.add(square_b)
        
        # 4. Quadrado sobre a hipotenusa 'c' (5 unidades)
        # Calculado por rotação e posicionamento
        # Centro da hipotenusa é (2, 1.5). Vetor normal aponta para (3.5, 3.5)
        hypotenuse_center = (p_A + p_B) / 2
        vector_ab = p_B - p_A
        angle_hyp = vector_ab_angle = np.arctan2(vector_ab[1], vector_ab[0])
        
        square_c_outline = Square(side_length=5, color=YELLOW, fill_opacity=0, stroke_width=3)
        # Rotação para alinhar com a hipotenusa. O quadrado padrão é axis-aligned.
        # Precisamos rotacionar para combinar com a inclinação AB.
        square_c_outline.rotate(angle_hyp)
        # Mover para que o lado inferior do quadrado coincida com a hipotenusa
        # O quadrado gira em torno do centro. Movemos o lado inferior para o centro da hipotenusa.
        square_c_outline.move_to(hypotenuse_center + UP * 2.5 * np.sin(angle_hyp + PI/2) + RIGHT * 2.5 * np.cos(angle_hyp + PI/2))
        
        # Centralizar tudo na tela
        total_group = VGroup(diagram, square_c_outline)
        total_group.move_to(ORIGIN)
        # Ajustar um pouco para baixo para caber melhor
        total_group.shift(DOWN * 0.5 + LEFT * 0.5)

        # --- Criação das Peças (Decomposição de Perigal) ---
        
        # Ponto central do Quadrado A (agora ajustado pela translação do grupo)
        center_a = square_a.get_center()
        
        # Definindo as linhas de corte baseadas na geometria de Perigal
        # Os cortes passam pelo centro de A e têm inclinação paralela e perpendicular à hipotenusa.
        # Hipotenusa vector: (-4, 3). Slope = -0.75.
        # Cut 1 (Paralelo): Slope -0.75.
        # Cut 2 (Perpendicular): Slope 4/3.
        
        # Vamos criar as 4 peças recortando o quadrado A.
        # Vértices locais de A em relação ao seu centro (2, -2):
        # TL(-2, 2), TR(2, 2), BR(2, -2), BL(-2, -2)
        # Pontos de interseção dos cortes nas bordas (calculados geometricamente):
        # Slope 4/3 intercepta x=2 (direita) em y=8/3=2.66 (fora) -> intercepta y=2 (topo) em x=1.5
        # Interseções relativas ao centro do quadrado A:
        # Corte 1 (Perp): (1.5, 2) e (-1.5, -2)
        # Corte 2 (Parallel): (2, -1.5) e (-2, 1.5)
        
        # Vértices das 4 peças (relativos ao centro_a):
        # Peça 1 (Top-Left): (0,0) -> (1.5, 2) -> (-2, 2) -> (-2, 1.5)
        v_p1 = [ORIGIN, RIGHT*1.5 + UP*2, LEFT*2 + UP*2, LEFT*2 + UP*1.5]
        # Peça 2 (Top-Right): (0,0) -> (2, -1.5) -> (2, 2) -> (1.5, 2)
        v_p2 = [ORIGIN, RIGHT*2 + DOWN*1.5, RIGHT*2 + UP*2, RIGHT*1.5 + UP*2]
        # Peça 3 (Bottom-Right): (0,0) -> (-1.5, -2) -> (2, -2) -> (2, -1.5)
        v_p3 = [ORIGIN, LEFT*1.5 + DOWN*2, RIGHT*2 + DOWN*2, RIGHT*2 + DOWN*1.5]
        # Peça 4 (Bottom-Left): (0,0) -> (-2, 1.5) -> (-2, -2) -> (-1.5, -2)
        v_p4 = [ORIGIN, LEFT*2 + UP*1.5, LEFT*2 + DOWN*2, LEFT*1.5 + DOWN*2]
        
        pieces_a = VGroup()
        colors = [TEAL, TEAL_D, BLUE_D, BLUE_E]
        
        for vertices, col in zip([v_p1, v_p2, v_p3, v_p4], colors):
            # Transformar vértices locais para globais
            global_pts = [center_a + v for v in vertices]
            poly = Polygon(*global_pts, color=WHITE, fill_color=col, fill_opacity=0.8, stroke_width=2)
            pieces_a.add(poly)

        # Peça do Quadrado B (inteira)
        piece_b = square_b.copy().set_fill(RED, 0.8).set_color(WHITE).set_stroke(width=2)
        
        # --- Definição dos Destinos (Preenchendo o Quadrado C) ---
        
        # O Quadrado C é preenchido colocando o Quadrado B no centro (rotacionado)
        # e as 4 peças de A nos cantos.
        
        center_c = square_c_outline.get_center()
        
        # Destino B: No centro de C, rotacionado para alinhar com C
        target_b = Square(side_length=3).set_fill(RED, 0.8).set_stroke(WHITE, 2)
        target_b.rotate(angle_hyp) # Alinha com a hipotenusa/quadrado C
        target_b.move_to(center_c)
        
        # Destino das Peças de A:
        # Geometricamente, as peças de A se encaixam conectando os cantos de C 
        # aos cantos do quadrado interno B e aos pontos médios dos lados de C.
        
        # Pegamos os vértices de C e de B_target para construir os polígonos alvo
        vertices_c = square_c_outline.get_vertices() # [UL, DL, DR, UR] (ordem depende da rotação)
        # Ordenar vértices de C para garantir consistência (UL, DL, DR, UR não é garantido pelo Manim)
        # Vamos usar a lógica geométrica: vértices de C e pontos médios.
        
        # Calcular vetores de direção do quadrado C
        # corner_ul é o topo esquerdo visualmente se angulo for pequeno
        # Vamos definir alvos específicos para cada peça baseada na forma.
        
        # Peça 1 (v_p1): Lados curtos 2 e 0.5 nas bordas originais, cortes 2.5 e 2.5.
        # No alvo, os cortes (2.5) formam metade do lado de C (que é 5).
        # Então as peças se encontram nos pontos médios dos lados de C.
        
        # Criar os 4 polígonos alvo manualmente para garantir a geometria perfeita
        # Usaremos as posições relativas.
        # Vetores base do quadrado C:
        v_right = (vertices_c[1] - vertices_c[0]) / 5 * 2.5 # Meio lado
        v_down = (vertices_c[3] - vertices_c[0]) / 5 * 2.5 # Meio lado? Cuidado com índices
        # Método mais seguro: calcular pontos médios e cantos
        
        pts_c = list(vertices_c) # 4 cantos
        mid_c = [(pts_c[i] + pts_c[(i+1)%4])/2 for i in range(4)] # 4 pontos médios
        pts_b = list(target_b.get_vertices()) # 4 cantos internos
        
        # Precisamos associar cada peça ao seu canto correspondente.
        # P1 (TL em A) -> Vai para um canto de C.
        # Visualmente, P1 tem o ângulo reto original. Esse ângulo reto vai para o canto de B ou C?
        # Na dissecção de Perigal, o centro de A (onde os cortes se cruzam em 90 graus) mapeia para os CANTOS de C.
        # O ângulo reto original dos cantos de A mapeia para os cantos de B (o buraco).
        
        # Logo:
        # Peça 1 (Top-Left de A):
        #   - O vértice do centro de A (90deg) vai para um canto de C.
        #   - O vértice do canto de A (90deg) vai para um canto de B.
        #   - Os outros dois vértices são os pontos médios dos lados de C adjacentes.
        
        # Vamos organizar os alvos.
        targets_a = VGroup()
        
        # Precisamos corresponder a rotação.
        # Peça 1 (Top-Left): Centro A é canto Bottom-Right da peça. Canto A é Top-Left da peça.
        # Essa peça deve ir para o canto onde ela se encaixe.
        # Vamos criar os 4 polígonos alvo e depois usar .match_points ou transform manual.
        
        # Target Polygons genéricos (Cantos de C conectando a B)
        # Um polígono alvo é formado por: [Canto_C, Mid_C_Adjacente1, Canto_B_Correspondente, Mid_C_Adjacente2]
        
        # Para garantir a ordem correta, vamos usar Transform combinando vértices.
        # Mas visualmente é melhor definir a posição final exata.
        
        # Assumindo a ordem padrão de vertices do Square (UL, DL, DR, UR) ou (UR, UL, DL, DR)...
        # Vamos criar uma lista de polígonos alvo girando ao redor de C.
        
        target_polys = []
        for i in range(4):
            # Canto de C, Mid, Canto de B, Mid_prev
            # A ordem dos vértices deve ser horária ou anti-horária consistente
            poly_pts = [
                pts_c[i],          # Canto externo
                mid_c[i],          # Ponto médio seguinte
                pts_b[i],          # Canto interno correspondente (B está alinhado)
                mid_c[(i-1)%4]     # Ponto médio anterior
            ]
            t_poly = Polygon(*poly_pts, color=WHITE, fill_opacity=0.8, stroke_width=2)
            target_polys.append(t_poly)

        # Agora precisamos mapear P1..P4 para os Target_Polys corretos.
        # P1 (TL de A): Vértice do centro é o BR local. Vértice do canto é TL local.
        # Target: Vértice externo é canto de C. Vértice interno é canto de B.
        # Geometricamente, P1 se move por translação pura no Perigal clássico.
        # Vamos tentar aplicar a translação vetor(Center_C - Center_A) e ver onde cai.
        # Se cair certo, ótimo. Se não, ajustamos.
        
        vec_trans = center_c - center_a
        
        # Grupo final de peças alvo
        final_pieces = VGroup()
        
        # Mapeamento manual para garantir visual limpo
        # P1 (TL) -> Translada para Top-Left de C?
        # A translação move o CENTRO de A para o CENTRO de C.
        # Mas no Perigal, o centro de A vira os CANTOS de C.
        # Então a translação não é única. As peças se separam.
        
        # Vamos usar a correspondência de área/forma.
        # A peça P1 tem lado 3.5 e 0.5 nos cortes? Não, cortes são hipotenusas dos triângulos menores.
        # Vamos simplificar: Usar ReplacementTransform para os targets construídos geometricamente.
        # Precisamos apenas colorir os targets com as cores das peças originais correspondentes.
        
        # Associar P1..P4 aos Targets T0..T3
        # P1 é "Top Left" -> Target Top Left (no referencial de C)
        # Precisamos identificar qual target é qual.
        # pts_c geralmente começa em UR ou UL.
        # Vamos identificar pelo vetor em relação ao centro.
        
        sorted_targets = sorted(target_polys, key=lambda m: m.get_center()[1], reverse=True)
        # Top targets primeiro. Depois left/right sort.
        # Isso é arriscado.
        
        # Vamos definir os targets explicitamente:
        # T_UL: Canto Superior Esquerdo de C.
        # T_UR: Canto Superior Direito.
        # T_BR: Canto Inferior Direito.
        # T_BL: Canto Inferior Esquerdo.
        
        def get_closest_corner_index(point, corners):
            dists = [np.linalg.norm(point - c) for c in corners]
            return np.argmin(dists)

        # Canto TL de C (maior Y, menor X) -> corresponde a P1 (TL de A)?
        # P1 tem canto A em (-2, 2) relativo ao centro. É TL.
        # Vamos assumir mapeamento direto de quadrantes.
        # P1(TL) -> Target(TL de C)
        # P2(TR) -> Target(TR de C)
        # P3(BR) -> Target(BR de C)
        # P4(BL) -> Target(BL de C)
        
        # Função auxiliar para encontrar o target correto para uma peça
        ordered_targets = [None] * 4
        
        # Vetores direcionais de C
        c_up = (pts_c[0] + pts_c[3]) / 2 - center_c # Aprox
        c_right = (pts_c[3] + pts_c[2]) / 2 - center_c # Aprox
        
        for tp in target_polys:
            mc = tp.get_center() - center_c
            # Projetar na base de C
            # Produto escalar grosseiro para determinar quadrante
            is_up = np.dot(mc, UP) > 0
            is_right = np.dot(mc, RIGHT) > 0
            
            # Ajuste fino devido à rotação
            # A rotação de C é aprox 37 graus (3-4-5).
            # Vamos usar coordenadas rotacionadas de volta para checar quadrante.
            mc_rot = rotate_vector(mc, -angle_hyp)
            
            if mc_rot[0] < 0 and mc_rot[1] > 0: ordered_targets[0] = tp # TL (P1)
            elif mc_rot[0] > 0 and mc_rot[1] > 0: ordered_targets[1] = tp # TR (P2)
            elif mc_rot[0] > 0 and mc_rot[1] < 0: ordered_targets[2] = tp # BR (P3)
            elif mc_rot[0] < 0 and mc_rot[1] < 0: ordered_targets[3] = tp # BL (P4)

        # Aplicar cores e estilos
        for i, tp in enumerate(ordered_targets):
            if tp is not None:
                tp.set_fill(colors[i], 0.8).set_stroke(WHITE, 2)
            else:
                # Fallback se a lógica de quadrante falhar (não deve ocorrer)
                ordered_targets[i] = target_polys[i].set_fill(colors[i], 0.8)

        # --- Sequência de Animação ---

        # 1. Mostrar diagrama inicial
        self.play(DrawBorderThenFill(triangle), run_time=1)
        self.play(FadeIn(square_a), FadeIn(square_b), run_time=1)
        self.wait(0.5)
        
        # 2. Desenhar o quadrado da hipotenusa (outline)
        self.play(Create(square_c_outline), run_time=1)
        self.wait(0.5)
        
        # 3. Mostrar os cortes no quadrado A (substituir o quadrado pelas peças)
        self.remove(square_a)
        self.add(pieces_a)
        self.play(LaggedStart(*[FadeIn(p, scale=0.9) for p in pieces_a], lag_ratio=0.1), run_time=1)
        self.wait(0.5)
        
        # 4. Animação de Decomposição e Reorganização
        # Mover Peça B para o centro de C
        # Mover Peças de A para os cantos de C
        
        # Grupo de animações
        animations = []
        
        # Animar B
        animations.append(Transform(piece_b, target_b))
        
        # Animar Peças A
        # P1 -> ordered_targets[0], etc.
        for source, target in zip(pieces_a, ordered_targets):
            animations.append(Transform(source, target))
            
        self.play(*animations, run_time=3, path_arc=0.5) # path_arc dá um efeito de arco no movimento
        
        self.wait(1)
        
        # 5. Finalização e destaque
        # Piscar o quadrado C completo para confirmar que a área é igual
        c_filled = Square(side_length=5).rotate(angle_hyp).move_to(center_c).set_fill(YELLOW, 0.2).set_stroke(YELLOW, 3)
        self.play(FadeIn(c_filled), run_time=1)
        self.wait(2)
