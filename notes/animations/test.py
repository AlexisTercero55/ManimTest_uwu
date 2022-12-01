from manim import *

class AnimationTest(Scene):
    def construct(self):
        l = 3
        txt = Tex('Alexis')

        sq1 = Square(side_length=l,
                    stroke_color = '#3E78FF',
                    fill_color = '#B38007',
                    fill_opacity = 0.75
                    )
        sq1.set_opacity(0)

        sq2 = Square(side_length=l,
                    stroke_color = '#EB4B23',
                    fill_color = '#19B377',
                    fill_opacity = 0.75
                    )
        sq2.set_opacity(0)

        tri = Triangle()
        tri.set_opacity(0)

        # creatw and arrange VGroup
        G = VGroup(txt,sq1,sq2,tri)
        G.arrange_in_grid(rows=2, buff=0.1)
        self.add(G)

        # Showing some creation mobjects animation types
        self.play(Write(txt), run_time=2)
        
        sq1.set_opacity(1)
        self.play(Create(sq1), run_time=2)

        sq2.set_opacity(1)
        self.play(DrawBorderThenFill(sq2), run_time=2)

        tri.set_stroke(opacity=1)
        self.play(Create(tri), run_time=2)
        
        # self.play(ShowSubmobjectsOneByOne(G,run_time=3))