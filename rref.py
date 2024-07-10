# manim -q l rref.py; ffplay /home/penguin/Code/projects-that-may-or-may-not-be-in-progress/manim-related/rref/media/videos/rref/480p15/rref.mp4

from manimlib import *


# Figure out how to make an rref video asap.
class rref(Scene):
    def construct(self):
        def find(mobject, r=0.5):
            self.play(Indicate(mobject), run_time=r)

        def advanced_show(mobject):
            num = Text("0").to_edge(DOWN)
            self.add(num)
            for i in range(len(mobject)):
                num.become(Text(str(i)).to_edge(DOWN))
                self.play(Indicate(mobject[i]))
            self.remove(num)

        # Title sequence

        text = VGroup()
        text.add(TexText("Reduced Row-Echelon Form"))
        text.add(TexText("RREF").next_to(text, DOWN))
        text.add(TexText("Using Gaussian Elimination").next_to(text, DOWN))

        text.move_to(ORIGIN)

        for i in range(len(text)):
            self.play(Write(text[i], stroke_color=WHITE), run_time=2)
        self.wait()
        self.play(FadeOut(text))

        text = VGroup()
        text.add(Tex("1x+2y-1z=1"))
        text.add(Tex("-1x-5y+2z=0").next_to(text[-1], DOWN))
        text.add(Tex("2x-4y+1z=10").next_to(text[-1], DOWN))
        text.move_to(ORIGIN)

        self.play(Write(text, stroke_color=WHITE))

        self.wait(7)

        matrix = Tex(r"""\left[
                            \begin{array}{c|c}
                            \begin{array}{ccc}
                            1 & 2 & -1 \\
                            -1 & -5 & 2 \\
                            2 & -4 & 1
                            \end{array} &
                            \begin{array}{c}
                            1 \\
                            0 \\
                            10
                            \end{array}
                            \end{array}\right]""").next_to(text, RIGHT, buff=1)

        allText = VGroup(text.copy(), matrix.copy()).move_to(ORIGIN)
        self.play(text.animate.move_to(allText[0]))
        matrix.move_to(allText[1])
        del allText

        answer = VGroup()
        answer.add(text[0][0][9].copy())
        answer.add(text[1][0][10].copy())
        answer.add(text[2][0][9:].copy())

        # Show ghost answer
        self.add(answer)
        self.play(
            answer[0].animate.move_to(matrix[0][16]),
            answer[1].animate.move_to(matrix[0][17]),
            answer[2].animate.move_to(matrix[0][18:20]),
        )
        self.remove(answer)

        self.add(matrix[0][16:20])

        # Show ghost row 1
        row = VGroup(
            text[0][0][0].copy(),
            text[0][0][3].copy(),
            text[0][0][5].copy(),
            text[0][0][6].copy(),
        )
        self.add(row)
        arcGroup = VGroup(
            ArcBetweenPoints(
                start=text[0][0][0].get_center(),
                end=matrix[0][2].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=text[0][0][3].get_center(),
                end=matrix[0][3].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=text[0][0][5].get_center(),
                end=matrix[0][4].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=text[0][0][6].get_center(),
                end=matrix[0][5].get_center(),
                angle=-PI,
            ),
        )
        self.play(
            *[MoveAlongPath(row[i], arcGroup[i]) for i in range(len(row))], run_time=2
        )
        self.remove(row)
        self.add(matrix[0][2], matrix[0][3], matrix[0][4], matrix[0][5])

        # Show ghost row 2
        row = VGroup(
            text[1][0][0].copy(),
            text[1][0][1].copy(),
            text[1][0][3].copy(),
            text[1][0][4].copy(),
            text[1][0][7].copy(),
        )
        self.add(row)
        arcGroup = VGroup(
            ArcBetweenPoints(
                start=text[1][0][0].get_center(),
                end=matrix[0][6].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=text[1][0][1].get_center(),
                end=matrix[0][7].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=text[1][0][3].get_center(),
                end=matrix[0][8].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=text[1][0][4].get_center(),
                end=matrix[0][9].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=text[1][0][7].get_center(),
                end=matrix[0][10].get_center(),
                angle=-PI,
            ),
        )
        self.play(
            *[MoveAlongPath(row[i], arcGroup[i]) for i in range(len(row))], run_time=2
        )
        self.remove(row)
        self.add(matrix[0][6], matrix[0][7], matrix[0][8], matrix[0][9], matrix[0][10])

        # Show ghost row 3
        row = VGroup(
            text[2][0][0].copy(),
            text[2][0][2].copy(),
            text[2][0][3].copy(),
            text[2][0][6].copy(),
        )
        self.add(row)
        arcGroup = VGroup(
            ArcBetweenPoints(
                start=text[2][0][0].get_center(),
                end=matrix[0][11].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=text[2][0][2].get_center(),
                end=matrix[0][12].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=text[2][0][3].get_center(),
                end=matrix[0][13].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=text[2][0][6].get_center(),
                end=matrix[0][14].get_center(),
                angle=-PI,
            ),
        )
        self.play(
            *[MoveAlongPath(row[i], arcGroup[i]) for i in range(len(row))], run_time=2
        )
        self.remove(row)
        self.add(matrix[0][11], matrix[0][12], matrix[0][13], matrix[0][14])

        # Add the rest of the matrix.
        self.play(FadeIn(matrix[0][0:2]), FadeIn(matrix[0][15]), FadeIn(matrix[0][20:]))

        temp_text = Text(
            "Must get 1s on the main diagonal and 0 everywhere else"
        ).next_to(VGroup(matrix, text), UP)
        self.play(Write(temp_text))
        self.wait(5)
        self.play(
            *[Indicate(matrix[0][i]) for i in [2, 8, 9, 14]],
            Indicate(text[0][0][0]),
            Indicate(text[1][0][3:5]),
            Indicate(text[2][0][6]),
        )
        self.wait(2)
        self.play(
            *[
                Indicate(matrix[0][i], color=BLUE)
                for i in range(2, 14)
                if i not in [8, 9]
            ],
            Indicate(text[0][0][3], color=BLUE),
            Indicate(text[0][0][5:7], color=BLUE),
            Indicate(text[1][0][0:2], color=BLUE),
            Indicate(text[1][0][7], color=BLUE),
            Indicate(text[2][0][0], color=BLUE),
            Indicate(text[2][0][2:4], color=BLUE),
        )
        self.play(FadeOut(temp_text))

        self.wait(3)

        temp_rect = VGroup(
            SurroundingRectangle(VGroup(matrix[0][2], matrix[0][6:8], matrix[0][11])),
            SurroundingRectangle(
                VGroup(text[0][0][0:2], text[1][0][0:3], text[2][0][0:2])
            ),
        )

        self.play(ShowCreation(temp_rect[0]), ShowCreation(temp_rect[1]))
        temp_rect[0].rotate(180 * DEGREES)
        temp_rect[1].rotate(180 * DEGREES)
        self.play(Uncreate(temp_rect[0]), Uncreate(temp_rect[1]))
        self.wait(0.5)

        # Indicate to the viewer that it is already a 1, so therefore no actions are needed
        self.play(Indicate(matrix[0][2]), Indicate(text[0][0][0]))
        temp_text = VGroup(Text("Already a 1!").next_to(VGroup(matrix, text), UP))
        self.play(Write(temp_text))
        self.play(temp_text.animate.shift(UP))

        self.wait(2)

        temp_text.add(
            Text("So no further actions are needed!").next_to(temp_text[-1], DOWN)
        )
        self.play(Write(temp_text[1]))

        self.play(FadeOut(temp_text))

        self.wait(6)

        text_copy = text[0].copy()
        text_copy2 = text[1].copy()

        matrix_copy = VGroup(matrix[0][2:6], matrix[0][16]).copy()
        matrix_copy2 = VGroup(matrix[0][6:11], matrix[0][17]).copy()

        self.add(text_copy, text_copy2, matrix_copy, matrix_copy2)
        self.play(
            text_copy.animate.next_to(text, DOWN),
            matrix_copy.animate.next_to(matrix, DOWN),
            run_time=1.5,
        )
        self.play(
            text_copy2.animate.next_to(text_copy, DOWN),
            matrix_copy2.animate.next_to(matrix_copy, DOWN),
            run_time=1.5,
        )

        add_sign_text_side = Tex("+").next_to(text_copy2, LEFT)
        add_sign_matrix_side = Tex("+").next_to(matrix_copy2, LEFT)

        underline_text_side = Line(
            VGroup(add_sign_text_side, text_copy2).get_corner(DL),
            VGroup(add_sign_text_side, text_copy2).get_corner(DR),
        ).shift(DOWN * 0.05)
        underline_matrix_side = Line(
            VGroup(add_sign_matrix_side, matrix_copy2).get_corner(DL),
            VGroup(add_sign_matrix_side, matrix_copy2).get_corner(DR),
        ).shift(DOWN * 0.05)

        self.play(
            FadeIn(add_sign_matrix_side),
            FadeIn(add_sign_text_side),
            FadeIn(underline_text_side),
            FadeIn(underline_matrix_side),
        )
        self.wait(3)

        text_side_result = Tex("0x-3y+1z=1").next_to(underline_text_side, DOWN)
        matrix_side_result = Tex("0~~~~-3~~~~1~~~~~~~1").next_to(
            underline_matrix_side, DOWN
        )

        text_side_result.shift(RIGHT / 3)
        matrix_side_result.shift(RIGHT / 3)

        self.play(FadeIn(text_side_result), FadeIn(matrix_side_result))

        self.play(
            *[
                FadeOut(i)
                for i in [
                    text_copy,
                    text_copy2,
                    matrix_copy,
                    matrix_copy2,
                    add_sign_text_side,
                    add_sign_matrix_side,
                    underline_text_side,
                    underline_matrix_side,
                ]
            ]
        )
        self.play(
            text_side_result.animate.next_to(text, DOWN),
            matrix_side_result.animate.next_to(matrix, DOWN),
        )

        self.wait()

        # Substitute for ShowPassingFlash
        temp_rect = VGroup(
            SurroundingRectangle(VGroup(matrix[0][6], matrix[0][17])),
            SurroundingRectangle(text[1]),
        )
        self.wait(0.75)
        self.play(ShowCreation(temp_rect[0]), ShowCreation(temp_rect[1]), run_time=1)
        temp_rect[0].rotate(180 * DEGREES)
        temp_rect[1].rotate(180 * DEGREES)
        self.play(Uncreate(temp_rect[0]), Uncreate(temp_rect[1]), run_time=1)

        # A refresher on what "TarTraRes" is:
        # Target, Transform (by moving), Resolve.
        # TarTraRes

        # Target
        text_target = VGroup(Tex("1x+2y-1z=1"), Tex("0x-3y+1z=1"), Tex("2x-4y+1z=10"))
        text_target.arrange(DOWN)

        matrix_target = Tex(r"""\left[
                            \begin{array}{c|c}
                            \begin{array}{ccc}
                            1 & 2 & -1 \\
                            0 & -3 & 1 \\
                            2 & -4 & 1
                            \end{array} &
                            \begin{array}{c}
                            1 \\
                            1 \\
                            10
                            \end{array}
                            \end{array}\right]""")
        allTextTarget = (
            VGroup(text_target, matrix_target).arrange(buff=1).move_to(ORIGIN)
        )

        # Generating paths are still part of target-making
        arcGroup = VGroup(
            ArcBetweenPoints(
                start=text_side_result.get_center(),
                end=text_target[1].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=matrix_side_result[0][0].get_center(),
                end=matrix_target[0][6].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=matrix_side_result[0][1].get_center(),
                end=matrix_target[0][7].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=matrix_side_result[0][2].get_center(),
                end=matrix_target[0][8].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=matrix_side_result[0][3].get_center(),
                end=matrix_target[0][9].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=matrix_side_result[0][4].get_center(),
                end=matrix_target[0][16].get_center(),
                angle=-PI,
            ),
        )

        # Transformation
        self.play(
            Transform(text[0], text_target[0]),
            Transform(text[2], text_target[2]),
            Transform(matrix[0][0:2], matrix_target[0][0:2]),
            Transform(matrix[0][15], matrix_target[0][14]),
            Transform(matrix[0][20:], matrix_target[0][19:]),
            FadeOut(matrix[0][6:11]),
            FadeOut(matrix[0][17]),
            # row 1
            Transform(matrix[0][2:6], matrix_target[0][2:6]),
            Transform(matrix[0][16], matrix_target[0][15]),
            # row 3
            Transform(matrix[0][11:15], matrix_target[0][10:14]),
            Transform(matrix[0][18:20], matrix_target[0][17:19]),
            # row 2
            FadeOut(text[1]),
            MoveAlongPath(text_side_result, arcGroup[0]),
            MoveAlongPath(matrix_side_result[0][0], arcGroup[1]),
            MoveAlongPath(matrix_side_result[0][1], arcGroup[2]),
            MoveAlongPath(matrix_side_result[0][2], arcGroup[3]),
            MoveAlongPath(matrix_side_result[0][3], arcGroup[4]),
            MoveAlongPath(matrix_side_result[0][4], arcGroup[5]),
        )

        # Resolve
        for i in text:
            self.remove(i)
        for i in matrix[0]:
            self.remove(i)
        self.remove(matrix_side_result, text_side_result)

        text = text_target
        matrix = matrix_target

        self.add(text, matrix)

        # Next animation:
        # TarTraRes
        scaling_text_side = (
            Tex(r"\frac{2}{-2}x-\frac{4}{-2}y+\frac{1}{-2}z=\frac{10}{-2}")
            .next_to(text, DOWN)
            .shift(LEFT * 3 / 4)
        )
        scaling_matrix_side = VGroup(
            Tex(r"\frac{2}{-2}").next_to(matrix[0][10], DOWN),
            Tex(r"\frac{-4}{-2}").next_to(matrix[0][11:13], DOWN),
            Tex(r"\frac{1}{-2}").next_to(matrix[0][13], DOWN),
            Tex(r"\frac{10}{-2}").next_to(matrix[0][17:19], DOWN),
        ).set_y(scaling_text_side.get_center()[1])

        text_copy = text[2][0].copy()
        matrix_copy = VGroup(matrix[0][10:14].copy(), matrix[0][17:19].copy())

        self.wait()
        self.play(Indicate(matrix[0][10]), Indicate(text[2][0][0]))
        self.wait()
        temp_text = VGroup(
            Text("Notice that the number is not 0, so we cannot skip it.").next_to(
                VGroup(matrix, text), UP
            )
        )
        self.play(Write(temp_text, stroke_color=WHITE))
        temp_text.add(
            Text("Notice that the number is not -1, so we cannot just add it.").next_to(
                VGroup(matrix, text), UP
            )
        )
        self.play(temp_text.animate.shift(UP), FadeIn(temp_text[1]))
        self.wait(4)
        self.play(FadeOut(temp_text))

        human_readable_matrix = [
            [matrix[0][2], matrix[0][3], matrix[0][4:6]],
            [matrix[0][6], matrix[0][7:9], matrix[0][9]],
            [matrix[0][10], matrix[0][11:13], matrix[0][13]],
        ]

        # Dag nab it, I gotta restart.
        self.wait()
        both = {
            "text": text[0].copy(),
            "matrix": VGroup(matrix[0][2:6].copy(), matrix[0][15].copy()),
        }
        text_target = VGroup(
            Tex(*r"-   2   \left(   1x+2y-1z=1   \right)".split("   ")).next_to(
                text, DOWN
            )
        )
        text_target.shift(LEFT * (text_target[0][3].get_x() - text[0].get_x()))

        matrix_target = VGroup(
            Tex(*r"-2 \cdot   \left(   1".split("   ")),
            Tex(*r"1   \right)".split("   ")),
        )
        m = both["matrix"].copy().next_to(matrix, DOWN)

        matrix_target[0].shift(UP * (m[0][0].get_y() - matrix_target[0][2].get_y()))
        matrix_target[0].shift(RIGHT * (m[0][0].get_x() - matrix_target[0][2].get_x()))
        matrix_target[1].shift(UP * (m[1].get_y() - matrix_target[1][0].get_y()))
        matrix_target[1].shift(RIGHT * (m[1].get_x() - matrix_target[1][0].get_x()))

        self.play(
            both["text"].animate.move_to(text_target[0][3]),
            FadeIn(text_target[0][0:3]),
            FadeIn(text_target[0][4]),
            both["matrix"].animate.move_to(m),
            FadeIn(matrix_target[0][0:2]),
            FadeIn(matrix_target[1][1]),
        )

        self.remove(matrix_target, text_target, m, *both.values())
        matrix_target = VGroup(matrix_target[0][0:2], matrix_target[1][1], m)
        matrix_target = VGroup(
            matrix_target[0][0][0],
            matrix_target[0][0][1],
            matrix_target[0][0][2],
            matrix_target[0][1],
            matrix_target[2][0][0],
            matrix_target[2][0][1],
            matrix_target[2][0][2:4],
            matrix_target[2][1],
            matrix_target[1],
        )

        text_target = Tex(
            *r"-2\left(   1   x   +2   y   -1   z   =   1   \right)".split("   ")
        ).move_to(text_target)
        self.add(text_target, matrix_target)

        both["text"] = text_target
        both["matrix"] = matrix_target

        text_target = (
            Tex(*"-2   x   -4   y   +2   z   =   -2".split("   "))
            .move_to(both["text"])
            .set_x(text[2].get_x())
        )

        matrix_target = VGroup(
            Tex("-2").move_to(both["matrix"][4]),
            Tex("-4").move_to(both["matrix"][5]),
            Tex("2").move_to(both["matrix"][6]),
            Tex("2").move_to(both["matrix"][7]),
        )

        self.wait(4)

        self.play(
            FadeOut(both["matrix"][0:4]),
            FadeOut(both["matrix"][8]),
            FadeOut(both["text"][0]),
            FadeOut(both["text"][9]),
            TransformMatchingTex(both["text"], text_target),
            FadeTransform(both["matrix"][4], matrix_target[0][0]),
            FadeTransform(both["matrix"][5], matrix_target[1]),
            FadeTransform(both["matrix"][6], matrix_target[2]),
            FadeTransform(both["matrix"][7], matrix_target[3]),
        )

        both["text"] = text_target
        both["matrix"] = matrix_target

        text_target = text[2].copy()
        matrix_target = VGroup(matrix[0][10:14].copy(), matrix[0][17:19].copy())

        self.play(
            text_target.animate.next_to(both["text"], DOWN).set_x(text[2].get_x()),
            matrix_target.animate.next_to(both["matrix"], DOWN).set_x(
                VGroup(matrix[0][10:14], matrix[0][17:19]).get_x()
            ),
        )

        add_signs = {
            "text": Tex("+").next_to(text_target, LEFT),
            "matrix": Tex("+").next_to(matrix_target, LEFT),
        }
        underlines = {
            "text": Line(
                VGroup(both["text"], text_target, add_signs["text"]).get_corner(DL),
                VGroup(both["text"], text_target, add_signs["text"]).get_corner(DR),
            ),
            "matrix": Line(
                VGroup(both["matrix"], matrix_target, add_signs["matrix"]).get_corner(
                    DL
                ),
                VGroup(both["matrix"], matrix_target, add_signs["matrix"]).get_corner(
                    DR
                ),
            ),
        }

        VGroup(*underlines.values()).shift(DOWN * 0.07)

        self.play(FadeIn(VGroup(*underlines.values(), *add_signs.values())))

        results = {
            "text": Tex("0x-8y+3z=8").next_to(underlines["text"], DOWN),
            "matrix": VGroup(
                Tex("0")
                .next_to(underlines["matrix"], DOWN)
                .set_x(both["matrix"][0].get_x()),
                Tex("-8")
                .next_to(underlines["matrix"], DOWN)
                .set_x(both["matrix"][1].get_x()),
                Tex("3")
                .next_to(underlines["matrix"], DOWN)
                .set_x(both["matrix"][2].get_x()),
                Tex("8")
                .next_to(underlines["matrix"], DOWN)
                .set_x(both["matrix"][3].get_x()),
            ),
        }

        self.wait()
        self.play(FadeIn(VGroup(*results.values())))

        self.play(
            FadeOut(
                VGroup(
                    *both.values(),
                    *underlines.values(),
                    *add_signs.values(),
                    text_target,
                    matrix_target,
                )
            ),
            results["text"].animate.next_to(text, DOWN),
            results["matrix"].animate.next_to(matrix, DOWN),
        )

        # TarTraRes
        # Target
        text_target = VGroup(Tex("1x+2y-1z=1"), Tex("0x-3y+1z=1"), Tex(r"0x-8y+3z=8"))
        text_target.arrange(DOWN)

        matrix_target = Tex(r"""\left[
                    \begin{array}{c|c}
                    \begin{array}{ccc}
                    1 & 2 & -1 \\
                    0 & -3 & 1 \\
                    0 & -8 & 3
                    \end{array} &
                    \begin{array}{c}
                    1 \\
                    1 \\
                    8
                    \end{array}
                    \end{array}\right]""")

        VGroup(text_target, matrix_target).arrange(buff=1).move_to(ORIGIN)

        brackets = {
            "left": matrix[0][0:2],
            "middle": matrix[0][14],
            "right": matrix[0][19:21],
        }

        human_readable_matrix = [
            [matrix[0][2], matrix[0][3], matrix[0][4:6]],
            [matrix[0][6], matrix[0][7:9], matrix[0][9]],
            [matrix[0][10], matrix[0][11:13], matrix[0][13]],
            [matrix[0][15], matrix[0][16], matrix[0][17:19]],
        ]

        arcGroup = VGroup()

        arcGroup.add(
            ArcBetweenPoints(
                start=results["matrix"][0].get_center(),
                end=matrix_target[0][10].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=results["matrix"][1].get_center(),
                end=matrix_target[0][11:13].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=results["matrix"][2].get_center(),
                end=matrix_target[0][13].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=results["matrix"][3].get_center(),
                end=matrix_target[0][17].get_center(),
                angle=-PI,
            ),
            ArcBetweenPoints(
                start=results["text"].get_center(),
                end=text_target[2].get_center(),
                angle=-PI,
            ),
        )

        # Substitute for ShowPassingFlash
        temp_rect = VGroup(
            SurroundingRectangle(
                VGroup(*human_readable_matrix[2], human_readable_matrix[3][2])
            ),
            SurroundingRectangle(text[2]),
        )
        self.wait(0.75)
        self.play(ShowCreation(temp_rect[0]), ShowCreation(temp_rect[1]), run_time=1)
        temp_rect[0].rotate(180 * DEGREES)
        temp_rect[1].rotate(180 * DEGREES)
        self.play(Uncreate(temp_rect[0]), Uncreate(temp_rect[1]), run_time=1)

        self.play(
            *[MoveAlongPath(results["matrix"][i], arcGroup[i]) for i in range(4)],
            MoveAlongPath(results["text"], arcGroup[4]),
            FadeOut(text[2]),
            matrix[0][0:10].animate.move_to(matrix_target[0][0:10]),
            matrix[0][14].animate.move_to(matrix_target[0][14]),
            matrix[0][15].animate.move_to(matrix_target[0][15]),
            matrix[0][16].animate.move_to(matrix_target[0][16]),
            matrix[0][19].animate.move_to(matrix_target[0][18]),
            matrix[0][20].animate.move_to(matrix_target[0][19]),
            FadeOut(matrix[0][10:14]),
            FadeOut(matrix[0][17:19]),
            text[0].animate.move_to(text_target[0]),
            text[1].animate.move_to(text_target[1]),
        )

        self.remove(matrix, text, *results.values())
        matrix = matrix_target
        text = text_target
        self.add(matrix_target, text_target)

        brackets = {
            "left": matrix[0][0:2],
            "middle": matrix[0][14],
            "right": matrix[0][18:20],
        }

        human_readable_matrix = [
            [matrix[0][2], matrix[0][3], matrix[0][4:6]],
            [matrix[0][6], matrix[0][7:9], matrix[0][9]],
            [matrix[0][10], matrix[0][11:13], matrix[0][13]],
            [matrix[0][15], matrix[0][16], matrix[0][17]],
        ]

        text_copy = text[1].copy()
        matrix_copy = VGroup(
            *human_readable_matrix[1], human_readable_matrix[3][1]
        ).copy()

        human_readable_matrix = [
            [matrix[0][2], matrix[0][3], matrix[0][4:6]],
            [matrix[0][6], matrix[0][7:9], matrix[0][9]],
            [matrix[0][10], matrix[0][11:13], matrix[0][13]],
            [matrix[0][15], matrix[0][16], matrix[0][17]],
        ]

        # Substitute for ShowPassingFlash
        temp_rect = VGroup(
            SurroundingRectangle(
                VGroup(*[human_readable_matrix[i][1] for i in range(3)])
            ),
            SurroundingRectangle(VGroup(*[text[i][0][2:5] for i in range(3)])),
        )
        self.wait(4)
        self.play(ShowCreation(temp_rect[0]), ShowCreation(temp_rect[1]))
        temp_rect[0].rotate(180 * DEGREES)
        temp_rect[1].rotate(180 * DEGREES)
        self.play(Uncreate(temp_rect[0]), Uncreate(temp_rect[1]))

        self.play(Indicate(text[1][0][2:4]), Indicate(human_readable_matrix[1][1]))
        self.wait(11)
        self.add(text_copy, matrix_copy)
        self.play(
            text_copy.animate.next_to(text, DOWN),
            matrix_copy.animate.next_to(matrix, DOWN),
        )

        # Set up the target, and I'm lazy so I'm just gonna fade in the -3's
        matrix_target = VGroup(
            Tex(r"\frac{0}{-3}"),
            Tex(r"\frac{-3}{-3}"),
            Tex(r"\frac{1}{-3}"),
            Tex(r"\frac{1}{-3}"),
        )
        matrix_target[0].shift(
            RIGHT * (matrix_copy[0].get_x() - matrix_target[0][0][0].get_x())
        )
        matrix_target[0].shift(
            UP * (matrix_copy[0].get_y() - matrix_target[0][0][0].get_y())
        )
        matrix_target[1].shift(
            RIGHT * (matrix_copy[1].get_x() - matrix_target[1][0][0:2].get_x())
        )
        matrix_target[1].shift(
            UP * (matrix_copy[1].get_y() - matrix_target[1][0][0:2].get_y())
        )
        matrix_target[2].shift(
            RIGHT * (matrix_copy[2].get_x() - matrix_target[2][0][0].get_x())
        )
        matrix_target[2].shift(
            UP * (matrix_copy[2].get_y() - matrix_target[2][0][0].get_y())
        )
        matrix_target[3].shift(
            RIGHT * (matrix_copy[3].get_x() - matrix_target[3][0][0].get_x())
        )
        matrix_target[3].shift(
            UP * (matrix_copy[3].get_y() - matrix_target[3][0][0].get_y())
        )
        # Debugging.
        # self.add(matrix_target.set_color(BLUE).set_opacity(0.5))

        # Add this at the end of the code to have an interactive adding and removing mobjects in real-time
        self.embed()
