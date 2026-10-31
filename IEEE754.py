'''
array of bits

run: manim -spqh -r "1080,1350" IEEE754.py SquareMatrix
'''

from manim import *
import numpy as np

class SquareMatrix(Scene):
    def construct(self):
        # Define the size and spacing of the squares
        square_size = 1
        square_spacing = 0.2
        
        # Define the number of rows and columns
        num_rows = 4
        num_cols = 8
        
        # Define the total number of squares to draw
        num_squares = num_rows * num_cols
        
        # Create an array of latex objects to display the values of 2^n
        '''
        To break it down further, the expression f"$2^{{{i}}}$" creates a string that contains the LaTeX expression for 2 raised to the power of i. The outermost pair of braces indicate that we want to include a Python expression within the string. The inner pair of braces is used to indicate that the expression i should be interpreted as a superscript in the LaTeX expression. The third pair of braces is used to escape the braces around the superscript so that they are interpreted correctly by the f-string.
        '''
        texts = [Tex(f"$2^{{{i}}}$") for i in range(num_squares)]
        
        # Create an array of squares with the Text objects inside
        squares = VGroup()
        for i in range(num_rows):
            for j in range(num_cols):
                square = Square(side_length=square_size)
                text = texts[i * num_cols + j]
                text.move_to(square.get_center())
                square.add(text)
                square.shift((square_size + square_spacing) * j * RIGHT + (square_size + square_spacing) * i * DOWN)
                squares.add(square)
        
        # Add the squares to the scene
        squares.move_to(np.array([-0.2,-0.2,0]))
        self.play(Create(squares), run_time=5)
        self.wait()

class SquareArray(Scene):
  def construct(self):
    # Define the size and spacing of the squares
    square_size = 1
    square_spacing = 0.1
    
    # Define the number of squares to draw
    num_squares = 10
    
    # Create an array of Text objects to display the values of 2^n
    texts = [Tex("$2^{{{}}}$".format(i)) for i in range(num_squares)]
    
    # Create an array of squares with the Text objects inside
    squares = VGroup()
    

    for i in range(num_squares):
      square = Square(side_length=square_size)
      text = texts[i]
      text.move_to(square.get_center())
      square.add(text)
      square.shift((square_size + square_spacing) * i * RIGHT)
      squares.add(square)
  
    # Add the squares to the scene
    squares.move_to(np.array([-0.2,0,0]))
    self.play(Create(squares))
    self.wait()
