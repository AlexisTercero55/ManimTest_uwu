# @author: Alexis Tercero
# from manim import *
import random

def uwu_txt(v = [4,3,0]):
    Ale = Text(
            'Alexis',
            t2c={'[:1]': '#3174f0', '[1:2]': '#e53125',
                '[2:3]': '#fbb003', '[3:4]': '#3174f0',
                '[4:5]': '#269a43', '[5:]': '#e53125'}, 
                font_size=20)
    Ale.move_to(np.array(v))
    return Ale

def rHColor():
    '''Hexadecimal color random number generator'''
    c = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    print(f'Color uwu: {c}')
    return c

# class Test(Scene):
#     '''
#     Here is declared how output looks like.
#     '''
#     def construct(self):
#         pass

# class ZoomTest(MovingCameraScene):
#     '''Zoom camera as 2D render by changing width and height
#        self.camera.frame.height
#        self.camera.frame.width
#        self.camera.frame.animate.set(width=Mobject.width * 1.2)'''