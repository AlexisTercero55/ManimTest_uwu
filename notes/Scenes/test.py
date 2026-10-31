# Alexis Tercero 11/30/2022 uwu
from manim import *
from manim.camera.moving_camera import MovingCamera


# TODO: Move this scene into ./notes/Scenes/cameraConfig.ipynb.
class FrameControlledMovingCameraScene(MovingCameraScene):
    def get_camera_frame(self) -> Mobject:
        camera = self.camera
        if not isinstance(camera, MovingCamera):
            raise RuntimeError(
                "This scene requires MovingCamera; Manim's OpenGLCamera has no frame."
            )
        return camera.frame


class MobjectMotionAndCameraFraming(FrameControlledMovingCameraScene):
    '''Demonstrate initial camera framing and animated mobject motion.'''
    def construct(self):
        self.load_mobjects()

        self.animate_creation()

        self.animate_syntax()
        self.wait()

    def animate_syntax(self):
        self.update_caption(".animate interpolates each object between states.")
        self.wait(1)

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

    def animate_creation(self):
        self.play(FadeIn(self.caption), run_time=0.5)
        self.wait(1.5)
        self.update_caption("Write, Create, and DrawBorderThenFill reveal objects.")
        self.play(Write(self.txt)) 
        self.play(DrawBorderThenFill(self.sq), run_time=2) 
        self.play(Create(self.tri))

        self.update_caption("always_redraw keeps arrow endpoints attached.")
        self.play(Create(self.arrowVG))
        # self.play(Create(VGroup(*self.res), run_time=2))
        self.wait(2)

    def load_mobjects(self):
        ''' Mobjects'''
        self.txt = Tex('Alexis').to_edge(UL, buff=0.5)
        self.sq = Square(side_length=0.5, 
                        fill_color=GREEN, 
                        fill_opacity=0.75)
        self.tri = Triangle().scale(0.6).to_edge(DR)

        self.redraw_mobjects()

        content = VGroup(self.txt, self.sq, self.tri)
        self.get_camera_frame().height = content.height + 4 * SMALL_BUFF + 1
        self.caption = Text(
            "Camera frame height fits the starting objects.",
            font_size=20,
        ).to_edge(DOWN, buff=0.25)

    def update_caption(self, text):
        next_caption = Text(text, font_size=20).move_to(self.caption)
        self.play(ReplacementTransform(self.caption, next_caption), run_time=0.5)
        self.caption = next_caption

    def redraw_mobjects(self):
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

    def _Write(self, obj: VMobject, rt=1, wt=0.5):
        self.play(Write(obj), run_time=rt)
        self.wait(wt)


class Example(FrameControlledMovingCameraScene):
    def construct(self):
        mob = DashedLine(color= YELLOW)
        self.get_camera_frame().width = mob.width + 4 * SMALL_BUFF
        self.add(mob)

class ChangingCameraWidthAndRestore(FrameControlledMovingCameraScene):
    def construct(self):
        text = Text("Hello World").set_color(BLUE)
        self.add(text)
        frame = self.get_camera_frame()
        frame.save_state()
        self.play(frame.animate.set(width=text.width * 1.2))
        self.wait(0.3)
        self.play(Restore(frame))


class Example_(FrameControlledMovingCameraScene):
    def construct(self):
        s= Star()
        self.get_camera_frame().height = s.height + 4 * SMALL_BUFF
        self.add(s)