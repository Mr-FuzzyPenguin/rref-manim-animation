# manim -q l latex-test.py; ffplay media/videos/latex-test/480p15/test.mp4

"""MANIMGL VERSION"""
from manimlib import *
from sys import exit

# Figure out how to make an rref video asap.
class test(Scene):
    def construct(self):
        def advanced_show(mobject):
            num = Text('0').to_edge(DOWN)
            self.add(num)
            for i in range(len(mobject)):
                num.become(Text(str(i)).to_edge(DOWN))
                self.play(Indicate(mobject[i]))
            self.remove(num)

        # To test your latex, put it here!
        text = Tex(r"""\left[
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
        text = Tex(r"\frac{2}{-2}x-\frac{4}{-2}y+\frac{1}{-2}z=\frac{10}{-2}")
        self.play(ShowCreation(text))
        advanced_show(text[0])

        self.embed()
        # text2 = MathTex("1").next_to(text,RIGHT)
        # self.play(Create(text2))
        # self.play(text2.animate.move_to(text[0][2]))
        # self.wait()


"""MANIMCE VERSION"""
# from manim import *
# from sys import exit
#
# # Figure out how to make an rref video asap.
# class test(Scene):
#     def construct(self):
#         def advanced_show(mobject):
#             num = Text('0').to_edge(DOWN)
#             self.add(num)
#             for i in range(len(mobject)):
#                 num.become(Text(str(i)).to_edge(DOWN))
#                 self.play(Indicate(mobject[i]))
#             self.remove(num)
#
#         # To test your latex, put it here!
#         text = MathTex(r"""\left[ \begin{array}{ccc|c}
#                             1 & 2 & -1  & 1 \\
#                             -1 & -5 & 2 & 0 \\
#                             2 & -4 & 1 & 10
#                             \end{array} \right]""")
#         self.play(Create(text))
#         advanced_show(text[0])
#         # text2 = MathTex("1").next_to(text,RIGHT)
#         # self.play(Create(text2))
#         # self.play(text2.animate.move_to(text[0][2]))
#         # self.wait()
