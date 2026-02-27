from manim import *

class TeoremaPitagorasDecomposicao(Scene):
    def construct(self):
        A = LEFT * 3 + DOWN * 2
        B = LEFT * 3 + UP * 2
        C = RIGHT * 2 + DOWN * 2

        tri = Polygon(A, B, C, color=WHITE)
        a_len = B.distance(C)
        b_len = A.distance(C)
        c_len = A.distance(B)

        square_a = Square(side_length=a_len, color=BLUE, fill_opacity=0.5)
        square_a.move_to((B + C) / 2)
        square_a.rotate(angle=Line(B, C).angle())

        square_b = Square(side_length=b_len, color=GREEN, fill_opacity=0.5)
        square_b.move_to((A + C) / 2)
        square_b.rotate(angle=Line(C, A).angle())

        square_c = Square(side_length=c_len, color=YELLOW, fill_opacity=0.5)
        square_c.move_to((A + B) / 2)
        square_c.rotate(angle=Line(A, B).angle())

        self.play(Create(tri))
        self.play(FadeIn(square_a), FadeIn(square_b), FadeIn(square_c))

        n = 8
        small_squares_a = VGroup()
        for i in range(n):
            for j in range(n):
                sq = Square(side_length=a_len / n, color=BLUE, fill_opacity=0.5)
                sq.move_to(
                    square_a.get_corner(DL)
                    + RIGHT * (j + 0.5) * a_len / n
                    + UP * (i + 0.5) * a_len / n
                )
                small_squares_a.add(sq)

        small_squares_b = VGroup()
        for i in range(n):
            for j in range(n):
                sq = Square(side_length=b_len / n, color=GREEN, fill_opacity=0.5)
                sq.move_to(
                    square_b.get_corner(DL)
                    + RIGHT * (j + 0.5) * b_len / n
                    + UP * (i + 0.5) * b_len / n
                )
                small_squares_b.add(sq)

        target_positions = []
        for i in range(2 * n):
            for j in range(2 * n):
                if i * 2 * n + j < len(small_squares_a) + len(small_squares_b):
                    pos = (
                        square_c.get_corner(DL)
                        + RIGHT * (j + 0.5) * (c_len / (2 * n))
                        + UP * (i + 0.5) * (c_len / (2 * n))
                    )
                    target_positions.append(pos)

        self.play(
            *[
                Transform(small_squares_a[i], small_squares_a[i].copy().move_to(target_positions[i]))
                for i in range(len(small_squares_a))
            ],
            *[
                Transform(
                    small_squares_b[i],
                    small_squares_b[i].copy().move_to(
                        target_positions[i + len(small_squares_a)]
                    )
                )
                for i in range(len(small_squares_b))
            ],
            run_time=6
        )

        self.wait()