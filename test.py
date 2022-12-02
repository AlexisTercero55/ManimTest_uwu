# Alexis Tercero 11/30/2022 uwu
from manim import *
import numpy as np
from math import pow
import random

# own imports
import sys
sys.path.append('e:\\dev\\Python_Dev\\CoputerGraphics\\test\\code')
from snippets import rHColor


class Test(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0,1.2,0.2],
            y_range=[0,1.2,0.2],
            # x_length=7,
            tips=True,
            axis_config={"include_numbers": True},
        )
        Ale = Text(
            'Alexis',
            t2c={'[:1]': '#3174f0', '[1:2]': '#e53125',
                '[2:3]': '#fbb003', '[3:4]': '#3174f0',
                '[4:5]': '#269a43', '[5:]': '#e53125'}, 
                font_size=45)
        Ale.move_to(np.array([4,3,0]))
        self.play(Write(Ale))


        self.play(Write(ax),run_time = 2.5)
        eq = MathTex('')
        self.add(eq)
        for n in range(2,3):
            graph = ax.plot(lambda x: pow(x,1/n), x_range=[0, 10,0.001], use_smoothing=True)
            graph.color = rHColor()
            rep = MathTex('y = x',r'^{1\over',f'{n}','}').scale(2.5).move_to(np.array([0,-2,0]))
            rep.color = graph.color
            self.play(Transform(eq,rep))

            self.play(Create(graph), run_time = 2)