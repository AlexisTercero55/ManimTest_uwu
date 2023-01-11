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
    '''
    Code MObject animation whit react color theme.
    '''
    def construct(self):
        self.camera.background_color =  '#282C34'

        # React Icon------------------------------------------
        svg = self.svgWriter('React-icon.svg',5)
        self.play(Write(svg),run_time=3)
        self.play(svg.animate.shift(DOWN*7.5).scale(0.2).rotate(2*PI/3), run_time=3)
        # self.play(Unwrite(svg),run_time=3)
        # self.wait()


        #Explanation-------------------------------------------------

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
            'yellow' : '#f7df1e',
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

        html = self.WCC('index.html','html',5)
        svg = self.svgWriter('this.svg',0.3,pos=[4.5,7.5,0])
        # DOM = self.svgWriter('DOM_Diagram2.svg',4.5,pos=[0,-3.5,0])

        # self.wait(1)

        # domEng = self.svgWriter('DOM engines.svg',.3,[4.7,0.5,0],rt=1)

        # e1 = self.pngCreation('blink.png',pos=[4.7,-1,0])
        # e2 = self.pngCreation('webkit.png',pos=[4.7,-3,0])
        # e3 = self.pngCreation('gecko.png',pos=[4.7,-5,0])

        # self.play(FadeOut(e1),
        #             FadeOut(e2),
        #             FadeOut(e3),
        #             FadeOut(domEng),
        #             Unwrite(DOM))

        script = self.WCC('style.css','css',-.8)
        script = self.WCC('script.js','js',-5.8)


    def WCC(self,file:str,lang:str = 'js', y:float = 0,rt:int = 3):
        '''Write custom code MObject'''
        snippet1 = self.customCode(file,y,lang)
        self.play(Write(snippet1), run_time=rt)
        return snippet1
        # self.snippet1.move_to(np.array([0, 2, 0]))

    def pngCreation(self,file,scale=1,pos=[0,0,0],rt=1):
        img = ImageMobject('assets/png/'+file)
        img.scale(scale)
        img.move_to(np.array(pos))
        self.play(FadeIn(img), run_time=rt)
        return img

    
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

class Snippet_3(Scene):

    def construct(self):
        #react theme color palette.
        self.colorPalette = {
            'yellow' : '#f7df1e',
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

        self.next_section('Write Snippet: 3')
        snippet3 = self.WCC('this1.js',y=4)

        self.next_section('Run Snippet: 3')
        _color_ = self.colorPalette['gray']
        self.play(snippet3.animate.set(stroke_color='#f7df1e'),rt=1)
        self.play(snippet3.animate.set(stroke_color=_color_),rt=1)

        self.next_section('Write Snippet: 3 output')
        snippet3_output = self.WCC('error.log',scale=1.5,y=-4.3,x=2,lang='nodejsrepl')#nodejsrepl, powershell
        self.wait(10)
        

    def WCC(self,file:str,lang:str = 'js', y:float = 0,x:float=0,scale:float=2,rt:int = 3):
        '''Write custom code MObject'''
        snippet = self.customCode(file,lang,scale=scale)
        # snippet.scale(scale)
        snippet.move_to(np.array([x, y, 0]))
        self.play(Write(snippet), run_time=rt)
        return snippet

    def customCode(self,file,lang,scale:float=1):
        snippet = Code(file_name = file,
                        tab_width=4, 
                        background='window',
                        language=lang,
                        style=Code.styles_list[15],#8
                        font="consolas",
                        font_size=12,
                        line_spacing= 0.9,
                        generate_html_file=True)
        snippet.background_mobject[0].color = '#1F2937'
        snippet.background_mobject[0].stroke_color = '#b4b7be'
        snippet.background_mobject[0].stroke_width = 10
        snippet.scale(scale)
        # snippet.move_to(np.array([0,y,0]))

        return snippet
