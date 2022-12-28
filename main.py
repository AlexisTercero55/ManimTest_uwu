# Alexis Tercero 11/30/2022 uwu
from manim import *
import numpy as np
from math import pow, sin
import random

# own imports
import sys
# sys.path.append('e:\\dev\\Python_Dev\\CoputerGraphics\\ManimCE\\code')
# from code.snippets import rHColor, uwu_txt

# run: manim -spqh -r "1080,1350" main.py ReactComponents

'''['default', 'emacs', 'friendly', 'friendly_grayscale', 'colorful', 'autumn', 
'murphy', 'manni', 'material', 
'monokai', 'perldoc', 'pastie', 'borland', 'trac', 'native', 'fruity', 'bw', 'vim', 'vs', 'tango', 'rrt', 'xcode', 'igor', 'paraiso-light', 'paraiso-dark', 'lovelace', 
'algol', 'algol_nu', 'arduino', 'rainbow_dash', 'abap', 'solarized-dark', 'solarized-light', 'sas', 'stata', 'stata-light', 'stata-dark', 
'inkpot', 'zenburn', 'gruvbox-dark', 'gruvbox-light', 'dracula', 'one-dark', 'lilypond']'''

class ReactComponents(Scene):
    def construct(self):
        self.camera.background_color =  '#282C34'

        # React Icon------------------------------------------
        svg = self.svgWriter('React-icon.svg',5)
        self.play(Write(svg),run_time=3)
        # self.add(svg)
        # svg.move_to(np.array([0, -7.2, 0]))
        # svg.move_to()
        self.play(svg.animate.shift(DOWN*7.5).scale(0.2).rotate(2*PI/3),
                #   svg.animate.scale(0.2),
                #   svg.animate.rotate(PI/2),
                #   svg.animate.scale(0.2),
                  run_time=3)
        # self.play(Unwrite(svg),run_time=3)
        # self.wait()


        #text-------------------------------------------------

        svg = self.svgWriter('title.svg',1)
        svg.move_to(np.array([0, 7, 0]))
        # svg.move_to()
        self.play(Write(svg),run_time=3)

        svg = self.svgWriter('Class component.svg',.3)
        svg.move_to(np.array([0, 4.7, 0]))
        # svg.move_to()
        self.play(Write(svg),run_time=3)

        self.snippet1 = self.customCode('CComponent.jsx',2,"js")
        self.play(Write(self.snippet1), run_time=5)
        self.snippet1.move_to(np.array([0, 2, 0]))

        svg = self.svgWriter('Function component.svg',.3)
        svg.move_to(np.array([0, -1.8, 0]))
        # svg.move_to()
        self.play(Write(svg),run_time=3)

        self.snippet1 = self.customCode('FComponent.jsx',-2,"js")
        self.snippet1.move_to(np.array([0, -4, 0]))
        self.play(Write(self.snippet1), run_time=4)

        # svg = self.svgWriter('React.svg',5)
        # svg.move_to(np.array([0, 0, 0]))
        # # svg.move_to()
        # self.play(Write(svg),run_time=3)


        # components : listings---------------------------------


        # # self.snippet1 = self.customCode('style.css',-5,'CSS')
        # # self.play(Write(self.snippet1), run_time=5)


    def WCC(self,file:str,lang:str = 'js', y:float = 0,rt:int = 3):
        '''Write custom code'''
        snippet1 = self.customCode(file,y,lang)
        self.play(Write(snippet1), run_time=rt)
        # self.snippet1.move_to(np.array([0, 2, 0]))
    
    def svgWriter(self,file:str,scale:float):
        svg_ = SVGMobject('assets/svg/'+file)#.scale(6).move_to(np.array([1,-1,0]))
        return svg_.scale(scale)


    def customCode(self,file,y,lang):
        snippet = Code(file_name = file,
                             tab_width=4, 
                             background='window',
                             language=lang,
                             style=Code.styles_list[15],#8
                             font="consolas",
                             font_size=12,)
        snippet.background_mobject[0].color = '#1F2937'
        snippet.background_mobject[0].stroke_color = '#b4b7be'
        snippet.background_mobject[0].stroke_width = 10
        snippet.scale(2)
        snippet.move_to(np.array([0,y,0]))

        return snippet
        # print()
        # print(Code.styles_list)

        # checking for bounded box
        # snippet.add_background_rectangle(color=GREEN)
        # self.add(snippet)



class DOM(Scene):
    def construct(self):
        '''Defining a DOM creation Scene'''
        self.colorPalette = {
            'background': '#282C34',
            'lowContrast': '#20232A',
            'mediumContrast': '#16181D',
            'highContrast': '#32363E',
            'tittle': '#61DAFB',
            'txt': '#FFFFF2',
            'grayTXT': '#b4b7be',
            'gray': '#b4b7be'
        }
        self.camera.background_color =  self.colorPalette['background']

        self.WCC('index.html','html',5)
        svg = self.svgWriter('this.svg',0.3,pos=[4.5,7.5,0])
        self.svgWriter('DOM_Diagram2.svg',4.5,pos=[0,-3.5,0])

        # self.wait(1.5)


    def WCC(self,file:str,lang:str = 'js', y:float = 0,rt:int = 3):
        '''Write custom code'''
        snippet1 = self.customCode(file,y,lang)
        self.play(Write(snippet1), run_time=rt)
        return snippet1
        # self.snippet1.move_to(np.array([0, 2, 0]))
    
    def svgWriter(self,file:str,scale:float=1,pos:list = [0, 0, 0],rt:int=3) -> SVGMobject:
        svg_ = SVGMobject('assets/svg/'+file)#.scale(6).move_to(np.array([1,-1,0]))
        svg_.scale(scale)
        svg_.move_to(np.array(pos))
        # svg.move_to()
        self.play(Write(svg_),run_time=rt)
        return svg_


    def customCode(self,file,y,lang):
        snippet = Code(file_name = file,
                             tab_width=4, 
                             background='window',
                             language=lang,
                             style=Code.styles_list[15],#8
                             font="consolas",
                             font_size=12,)
        snippet.background_mobject[0].color = '#1F2937'
        snippet.background_mobject[0].stroke_color = '#b4b7be'
        snippet.background_mobject[0].stroke_width = 10
        snippet.scale(2)
        snippet.move_to(np.array([0,y,0]))

        return snippet

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