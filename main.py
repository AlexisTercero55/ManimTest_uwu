# Alexis Tercero 11/30/2022 uwu
from manim import *

import numpy as np
from math import pow, sin
import random
# own imports
import sys
# sys.path.append('e:\\dev\\Python_Dev\\CoputerGraphics\\ManimCE\\code')
# from code.snippets import rHColor, uwu_txt

# run: manim -spqh -r "1080,1920" main.py Snippet_3 ReactComponents

# ─────────────────────────────────────────────────────────────
#  Base class – holds every method shared across scenes
# ─────────────────────────────────────────────────────────────
class BaseScene(Scene):
    """Common helpers for code / svg / png animation scenes."""

    colorPalette = {
        'yellow':         '#f7df1e',
        'background':     '#282C34',
        'lowContrast':    '#20232A',
        'mediumContrast': '#16181D',
        'highContrast':   '#32363E',
        'tittle':         '#61DAFB',
        'txt':            '#FFFFF2',
        'grayTXT':        '#b4b7be',
        'gray':           '#b4b7be',
    }

    # ── asset helpers ────────────────────────────────────────
    def svgWriter(self, file: str, scale: float = 1,
                  pos: list | None = None, rt: int = 3, play: bool = True):
        svg_ = SVGMobject('assets/svg/' + file).scale(scale)
        if pos is not None:
            svg_.move_to(np.array(pos))
        if play:
            self.play(Write(svg_), run_time=rt)
        return svg_

    def pngCreation(self, file: str, scale: float = 1,
                    pos: list = (0, 0, 0), rt: int = 1):
        img = ImageMobject('assets/png/' + file).scale(scale)
        img.move_to(np.array(pos))
        self.play(FadeIn(img), run_time=rt)
        return img

    # ── code helpers ─────────────────────────────────────────
    def customCode(self, file: str, lang: str = 'js', scale: float = 2,
                   formatter_style: str | None = None,
                   code_kwargs: dict | None = None):
        if formatter_style is None:
            formatter_style = Code.get_styles_list()[30]

        kwargs = dict(
            code_file=file,
            tab_width=4,
            background='window',
            language=lang,
            formatter_style=formatter_style,
            background_config={
                "buff": 0.3,
                "fill_color": '#1F2937',
                "stroke_color": '#b4b7be',
                "corner_radius": 0.2,
                "stroke_width": 10,
                "fill_opacity": 1,
            },
            paragraph_config={
                "font": "consolas",
                "font_size": 12,
                "line_spacing": 0.5,
                "disable_ligatures": True,
            },
        )
        if code_kwargs:
            kwargs.update(code_kwargs)

        return Code(**kwargs).scale(scale)

    def WCC(self, file: str, lang: str = 'js', x: float = 0, y: float = 0,
            scale: float = 2, rt: int = 3, **code_kwargs):
        """Write Custom Code – create, position and animate a Code snippet."""
        snippet = self.customCode(file, lang=lang, scale=scale,
                                  code_kwargs=code_kwargs)
        snippet.move_to(np.array([x, y, 0]))
        self.play(Write(snippet), run_time=rt)
        return snippet

class Snippet_3(BaseScene):
    def construct(self):
        background = Rectangle(
                            width = 15,#config.frame_width,
                            height = 18,#config.frame_height,
                            stroke_width = 0,
                            fill_color = [GREEN, BLUE, RED, '#FFFFFF' ], # make sure to change these by the colors you like
                            fill_opacity = 1
                        )
        self.add(background)

        self.next_section('Write Snippet: 3')
        snippet3 = self.WCC(
            'SingleActivity.kt', y=4, scale=.5,
            formatter_style="emacs",  # ← override per scene
        )

        self.next_section('Run Snippet: 3')
        _color_ = self.colorPalette['gray']
        self.play(snippet3.animate.set(stroke_color='#f7df1e'), run_time=1)
        self.play(snippet3.animate.set(stroke_color=_color_), run_time=1)
        self.wait(1)    

class DOM(BaseScene):
    """Defining a DOM creation Scene."""
    def construct(self):
        background = Rectangle(
                    width = 15,#config.frame_width,
                    height = 18,#config.frame_height,
                    stroke_width = 0,
                    fill_color = [GREEN, BLUE, RED, '#FFFFFF' ], # make sure to change these by the colors you like
                    fill_opacity = 1
                )
        self.add(background)

        self.WCC('./assets/codes/index.html', 'html', y=5)
        self.svgWriter('this.svg', 0.3, pos=[4.5, 7.5, 0])
        DOM = self.svgWriter('DOM_Diagram2.svg', 4.5, pos=[0, -3.5, 0])
        self.wait(1)
        
        domEng = self.svgWriter('DOM engines.svg', 0.3,
                                pos=[4.7, 0.5, 0], rt=1)

        e1 = self.pngCreation('blink.png',  pos=[4.7, -1, 0])
        e2 = self.pngCreation('webkit.png', pos=[4.7, -3, 0])
        e3 = self.pngCreation('gecko.png',  pos=[4.7, -5, 0])

        self.play(
            FadeOut(e1),
            FadeOut(e2),
            FadeOut(e3),
            FadeOut(domEng),
            Unwrite(DOM),
        )

        script = self.WCC('./assets/codes/style.css', 'css', y=-0.8)
        script = self.WCC('./assets/codes/script.js', 'js',  y=-5.8)

'''['default', 'emacs', 'friendly', 'friendly_grayscale', 'colorful', 'autumn', 
'murphy', 'manni', 'material', 
'monokai', 'perldoc', 'pastie', 'borland', 'trac', 'native', 'fruity', 'bw', 'vim', 'vs', 'tango', 'rrt', 'xcode', 'igor', 'paraiso-light', 'paraiso-dark', 'lovelace', 
'algol', 'algol_nu', 'arduino', 'rainbow_dash', 'abap', 'solarized-dark', 'solarized-light', 'sas', 'stata', 'stata-light', 'stata-dark', 
'inkpot', 'zenburn', 'gruvbox-dark', 'gruvbox-light', 'dracula', 'one-dark', 'lilypond']'''
config.background_color = "#0C1531"
class ReactComponents(Scene):
    '''
    Code MObject animation whit react color theme.
    '''
    def construct(self):
        background = Rectangle(
            width = 15,#config.frame_width,
            height = 18,#config.frame_height,
            stroke_width = 0,
            fill_color = [GREEN, BLUE, RED, '#FFFFFF' ], # make sure to change these by the colors you like
            fill_opacity = 1
        )
        self.add(background)
        # self.camera.background_color( "#ece6e2")
        #react background color
        #self.camera.background_color( color= ManimColor.from_rgb((0, 1, 0.4, 0.5)) )#react background color

        # React Icon------------------------------------------
        # svg = self.svgWriter('React-icon.svg',5)
        # self.play(Write(svg),run_time=3)
        # self.play(svg.animate.shift(DOWN*7.5).scale(0.2).rotate(2*PI/3), run_time=3)
        # self.play(Unwrite(svg),run_time=3)
        # self.wait()


        #Explanation-------------------------------------------------

        # svg = self.svgWriter('title.svg',1)
        # svg.move_to(np.array([0, 7, 0]))
        # # svg.move_to()
        # self.play(Write(svg),run_time=3)

        # svg = self.svgWriter('Class component.svg',.3)
        # svg.move_to(np.array([0, 4.7, 0]))
        # # svg.move_to()
        # self.play(Write(svg),run_time=3)

        self.snippet1 = self.customCode('CComponent.jsx',2,"js")
        self.play(Write(self.snippet1), run_time=5)
        self.snippet1.move_to(np.array([0, 2, 0]))

        # svg = self.svgWriter('Function component.svg',.3)
        # svg.move_to(np.array([0, -1.8, 0]))
        # # svg.move_to()
        # self.play(Write(svg),run_time=3)

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
        snippet = Code(code_file = file,
                             tab_width=4, 
                             background='window',
                             language=lang,
                             formatter_style=Code.get_styles_list()[30],#jsx_7_10_15_24__25__30
                             background_config = {
                                    "buff": 0.3,
                                    "fill_color": '#1F2937',
                                    "stroke_color": '#b4b7be',
                                    "corner_radius": 0.2,
                                    "stroke_width": 10,
                                    "fill_opacity": 1
                                },
                             paragraph_config = {
                                    "font": "consolas",
                                    "font_size": 12,
                                    "line_spacing": 0.5,
                                    "disable_ligatures": True,
                                })
        snippet.scale(2)
        snippet.move_to(np.array([0,y,0]))

        return snippet
        # print()
        # print(Code.styles_list)

        # checking for bounded box
        # snippet.add_background_rectangle(color=GREEN)
        # self.add(snippet)