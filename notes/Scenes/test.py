# Alexis Tercero 11/30/2022 uwu
from manim import *
import numpy as np


# TODO: Save this class as MakingZoom class at ./notes/Scenes/cameraConfig.ipynb
class MakingZoom(MovingCameraScene):
    '''Zoom camera as 2D render by changing width and height
       self.camera.frame.height
       self.camera.frame.width
       self.camera.frame.animate.set(width=Mobject.width * 1.2)'''
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
        self.play(Create(self.arrowVG))
        # self.play(Create(VGroup(*self.res), run_time=2))
        self.wait(2)

    def loadMobjects(self):
        ''' Mobjects'''
        self.txt = Tex('Alexis').to_edge(UL, buff=0.5)
        self.sq = Square(side_length=0.5, 
                        fill_color=GREEN, 
                        fill_opacity=0.75)
        self.tri = Triangle().scale(0.6).to_edge(DR)

        self.redrawMobjects()

        V = VGroup(self.txt,self.tri)
        self.camera.frame.height= V.height+4*SMALL_BUFF # even better

    def redrawMobjects(self):
        self.arrowVG = VGroup(always_redraw(
                                lambda : Line(
                                    start= self.sq.get_top(),
                                    end= self.txt.get_bottom(), buff=0.2
                                ).add_tip()
                             ))
        self.arrowVG.add(always_redraw(
            lambda : Line(
                start= self.sq.get_bottom(),
                end= self.tri.get_top(), buff=0.2
            ).add_tip()
        ))

    def _moveCopy(self, a : Mobject, b : Mobject, wt = 0.5):
        self.play(Transform(a.copy(),b))
        self.wait(wt)

    def _Write(self, obj: Mobject , rt = 1 , wt = 0.5):
        self.play(Write(obj), run_time=rt)
        self.wait(wt)


class Example(MovingCameraScene):
    def construct(self):
        mob = DashedLine(color= YELLOW)
        self.camera.frame.width=mob.width +4*SMALL_BUFF
        self.add(mob)

class ChangingCameraWidthAndRestore(MovingCameraScene):
    def construct(self):
        text = Text("Hello World").set_color(BLUE)
        self.add(text)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width=text.width * 1.2))
        self.wait(0.3)
        self.play(Restore(self.camera.frame))


class Example_(MovingCameraScene):
    def construct(self):
        s= Star()
        self.camera.frame.height=s.height+4*SMALL_BUFF # even better
        self.add(s)