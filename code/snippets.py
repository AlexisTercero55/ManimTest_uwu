# @author: Alexis Tercero
from manim import Text
import random
import numpy as np

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

# ---------------------------------------------
# class PlotUpdaters(Scene):
#     def construct(self):
#         # constants
#         X_LEN = PI
#         X_RANGE = [-X_LEN, X_LEN]
#         X_STEP = 0.1

#         t = ValueTracker(-PI/2)

#         ax = (Axes(x_range=X_RANGE,
#                   y_range=[-1,1],
#                   x_length=2*X_LEN,
#                   y_length=2).add_coordinates()
#                 ).scale(1.7)

#         # Axes labels
#         y_label = ax.get_y_axis_label(MathTex(r'\sin(x)'),
#         edge=UP, buff=0.4)
    
#         x_label = ax.get_x_axis_label(MathTex(r'x'),
#         edge=RIGHT, buff=0.2)
        

#         plott = ax.plot(lambda x: sin(x), 
#                         x_range=X_RANGE.append(X_STEP), 
#                         color='#00AF3D')

#         c1 = rHColor()
#         slope = always_redraw(
#             lambda : ax.get_secant_slope_group(
#                 x= t.get_value(),
#                 graph=plott,
#                 dx=0.01
#                 ,dx_line_color=None
#                 ,secant_line_color='#E30000'
#                 ,secant_line_length=4
#             )
#         )

#         c2 = '#E349E1'
#         dot = always_redraw(
#             lambda : Dot(color=c2).move_to(
#                 ax.c2p(t.get_value()
#                        ,plott.underlying_function(t.get_value()))
#             )
#         )

#         txt = uwu_txt()
#         self.play(Write(txt))
        
#         self.play(Create(VGroup(ax)), run_time=3)
#         self.play(Write(x_label))
#         self.play(Write(y_label))

#         self.play(Create(VGroup(plott)), run_time=3)

#         self.play(Create(VGroup(slope,dot)))
#         self.play(t.animate.set_value(PI/2), run_time=3)


# class Reiman(Scene):
#     def construct(self):
#         # constants
#         X_LEN = 10
#         X_STEP = 0.1
#         X_RANGE = [-X_LEN, X_LEN]
#         Y_LEN = 10
#         Y_RANGE = [-Y_LEN, Y_LEN]

#         t = ValueTracker(-PI/2)
#         plane = (
#             NumberPlane(
#                 x_range=X_RANGE
#                 ,y_range=Y_RANGE
#             ).add_coordinates()
#         )
#         labels = plane.get_axis_labels(x_label=MathTex('x')
#                                       ,y_label=MathTex('\sin(x)'))
#         self.placeLabels(labels,plane)

#         plott = plane.plot(lambda x: sin(x)
#                            ,x_range=X_RANGE.append(X_STEP)
#                            ,color='#0EB110'
#                           )

#         area = plane.get_riemann_rectangles(graph=plott
#                                             ,x_range=X_RANGE
#                                             ,input_sample_type='center'
#                                             ,fill_opacity=0.5
#                                             ,color=np.array((rHColor(), rHColor(),rHColor(),rHColor())))
        
        
#         self.cameraSettings()
#         self.uwu_txt(v = [-2.6,3,0])
#         self.play(Write(VGroup(plane)),run_time = 4) # 4s is better for creating plane
#         self.play(Write(labels))
#         self.play(Create(VGroup(plott)),run_time = 3)
#         self.play(Create(VGroup(area)),run_time = 5)
#         self.wait(3)


#     def uwu_txt(self,v = [4,3,0]):
#         Ale = Text(
#                 'Alexis',
#                 t2c={'[:1]': '#3174f0', '[1:2]': '#e53125',
#                     '[2:3]': '#fbb003', '[3:4]': '#3174f0',
#                     '[4:5]': '#269a43', '[5:]': '#e53125'}, 
#                     font_size=10).scale(3.5)
#         Ale.move_to(np.array(v))
#         self.play(Write(Ale))

#     def placeLabels(self,labels,plane):
#         # get separate labels
#         x,y = labels[0], labels[1]
#         x.move_to(np.array([3.3,0.4,0]))
#         y.move_to(np.array([0.5,3.3,0])).scale(0.8)

#     def cameraSettings(self)->None:
#         self.camera.frame_height = self.camera.frame_height*0.5
#         self.camera.frame_width  = self.camera.frame_width*0.5

# class BasicMarkupExample(Scene):
#     def construct(self):
#         text1 = MarkupText("<b>foo</b> <i>bar</i> <b><i>foobar</i></b>")
#         text2 = MarkupText("<s>foo</s> <u>bar</u> <big>big</big> <small>small</small>")
#         text3 = MarkupText("H<sub>2</sub>O and H<sub>3</sub>O<sup>+</sup>")
#         text4 = MarkupText("type <tt>help</tt> for help")
#         text5 = MarkupText(
#             '<span underline="double">foo</span> <span underline="error">bar</span>'
#         )
#         group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
#         self.add(group)
    
# class GetSecantSlopeGroupExample(Scene):
#     def construct(self):
#         ax = Axes(y_range=[-1, 7])
#         graph = ax.plot(lambda x: sin(x), color=BLUE)
#         slopes = ax.get_secant_slope_group(
#             x=PI/3,
#             graph=graph,
#             dx=0.1,
#             dx_label=Tex("dx = 1.0"),
#             dy_label="dy",
#             dx_line_color=GREEN_B,
#             secant_line_length=4,
#             secant_line_color=RED_D,
#         )

#         self.add(ax, graph, slopes)

#