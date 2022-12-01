# Alexis Tercero 11/30/2022 uwu
from manim import *
import numpy as np

# TODO: Save this version of AnimateSyntax class at ./notes/animations/AnimationTypes.ipynb
class Test(Scene):
    '''Using Transfrom and Mobject.copy()
    Circunference concept'''
    def construct(self):
        self.loadMobjects()

        self.animateCration()

        self.animateSyntax()
        self.wait()

    def animateSyntax(self):
        # .animate syntax for motion animation
        rt = 2
        self.play(self.txt.animate.to_edge(UR),
                  run_time=rt)
        self.play(self.sq.animate.to_edge(LEFT),
                  run_time=rt)
        self.play(self.sq.animate.move_to(ORIGIN),
                  run_time=rt)
        self.play(self.tri.animate.to_edge(DL),
                  run_time=rt)
        self.play(self.tri.animate.to_edge(DR),
                  self.txt.animate.to_edge(UL),
                  self.sq.animate.scale(2),
                  run_time=rt)

    def animateCration(self):
        # Creation animations
        self.play(Write(self.txt)) 
        self.play(DrawBorderThenFill(self.sq), run_time=2) 
        self.play(Create(self.tri)) 
        self.wait(2)

    def loadMobjects(self):
        ''' Mobjects'''
        self.txt = Tex('Alexis').to_edge(UL, buff=0.5)
        self.sq = Square(side_length=0.5, 
                        fill_color=GREEN, 
                        fill_opacity=0.75)
        self.tri = Triangle().scale(0.6).to_edge(DR)

    def _moveCopy(self, a : Mobject, b : Mobject, wt = 0.5):
        self.play(Transform(a.copy(),b))
        self.wait(wt)

    def _Write(self, obj: Mobject , rt = 1 , wt = 0.5):
        self.play(Write(obj), run_time=rt)
        self.wait(wt)

