# @author: Alexis Tercero
from manim import *
import random

def rHColor():
    '''Hexadecimal color random number generator'''
    return  "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])

class Test(Scene):
    '''
    Here is declared how output looks like.
    '''
    def construct(self):
        pass

class ZoomTest(MovingCameraScene):
    '''Zoom camera as 2D render by changing width and height
       self.camera.frame.height
       self.camera.frame.width
       self.camera.frame.animate.set(width=Mobject.width * 1.2)'''