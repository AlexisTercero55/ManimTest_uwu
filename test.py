# Alexis Tercero 11/30/2022 uwu
from manim import *
class Test(Scene):
    '''
    Here is declared how output looks like.
    '''
    def construct(self):
        # Mobjects
        txt = Tex('Alexis').to_edge(UL, buff=0.5)
        sq = Square(side_length=0.5, 
                    fill_color=GREEN, 
                    fill_opacity=0.75)
        tri = Triangle().scale(0.6).to_edge(DR)

        # Creation animations
        self.play(Write(txt)) 
        self.play(DrawBorderThenFill(sq), run_time=2) 
        self.play(Create(tri)) 
        self.wait(2)

        # .animate syntax for motion animation
        rt = 2
        self.play(txt.animate.to_edge(UR),
                  run_time=rt)
        self.play(sq.animate.to_edge(LEFT),
                  run_time=rt)
        self.play(sq.animate.move_to(ORIGIN),
                  run_time=rt)
        self.play(tri.animate.to_edge(DL),
                  run_time=rt)
        self.play(tri.animate.to_edge(DR),
                  txt.animate.to_edge(UL),
                  sq.animate.scale(2),
                  run_time=rt)
        self.wait()



code = '''class Graph {
    constructor(directed = true) 
    {
    this.directed = directed;
    this.nodes = [];
    this.edges = new Map();
    }
  }
}'''

class WriteSnippet(Scene):
    def construct(self):
        snippet = Code(code=code, 
                             tab_width=4, 
                             background="window",
                             language="js", 
                             font="Monospace",
                             font_size=12,)
        self.play(Write(snippet), run_time=5)

        # checking for bounded box
        # snippet.add_background_rectangle(color=GREEN)
        # self.add(snippet)

