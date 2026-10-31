from pathlib import Path
from manim import *
from manim.opengl import FullScreenQuad
import numpy as np

config.disable_caching = True
# config.fullscreen = True

class AbstractShaderScene(Scene):
  # renderer = OpenGLRenderer()
  shader_file = "fragment_01"
  shader_dir: Path = Path(__file__).resolve().parent

  def setup(self):
    # Import fragment shader from external file
    # with open(f"./{self.shader_file}.glsl", "r") as file:
    #   self.shader_str = file.read()
    # self.set_surface()
    self.shader_str = self.load_shader(self.shader_file)
    self.set_surface()

  def load_shader(self, name: str) -> str:
    path = self.shader_dir / f"{name}.glsl"
    if not path.is_file():
      raise FileNotFoundError(
        f"Shader source not found: {path}\n"
        f"(shader_dir = {self.shader_dir})"
      )
    return path.read_text(encoding="utf-8")
  
  def set_surface(self) -> None:
    self.surface = FullScreenQuad(
      self.renderer.context,
      self.shader_str,
    )
    
  def window_scale(self) -> float:
    """Framebuffer-to-window scale. Safe to call before the window exists."""
    window = getattr(self.renderer, "window", None)
    if window is None or not getattr(window, "width", 0):
        return 1.0
    return config.pixel_width / float(window.width)

  def set_resolution_uniform(self) -> None:
    self.surface.shader.set_uniform(
        "iResolution",
        np.array(
            [config.pixel_width, config.pixel_height], dtype=np.float32
        ),
    )

  def construct(self) -> None:
    self.add(self.surface)
    self.interactive_embed()

class Shaders01(AbstractShaderScene):
  shader_file = "fragment_01"
  def construct(self):
      self.interactive_embed()


# /////////////////////////////////////////////////
# Uniform variables
# /////////////////////////////////////////////////

class Shaders02(AbstractShaderScene):
  shader_file = "fragment_02"
  def construct(self):
    self.surface.shader.set_uniform("r", 0)
    self.surface.shader.set_uniform("g", 0)
    self.surface.shader.set_uniform("b", 0)
    self.add(self.surface)
    self.interactive_embed()


class Shaders03(AbstractShaderScene):
  shader_file = "fragment_03"
  def construct(self):
    self.surface.shader.set_uniform(
      "iResolution",
      (config.pixel_width, config.pixel_height)
    )
    self.add(self.surface)
    self.interactive_embed()


# /////////////////////////////////////////////////
# Normalize in 16/9 aspect ration
# /////////////////////////////////////////////////

class Shaders05(AbstractShaderScene):
  shader_file = "fragment_05"
  def construct(self):
    """
    Scene.renderer.window.width:
      It is the width of the interactive screen
      when we render the scene with OpenGL
    Scene.renderer.window.height:
      It is the height of the interactive screen
      when we render the scene with opengl
    """
    self.set_resolution_uniform()
    # Placeholder until the window exists; updater replaces it.
    self.surface.shader.set_uniform("u_scale", 1.0)

    def scale_updater(surface, dt):
        surface.shader.set_uniform("u_scale", self.window_scale())

    self.surface.add_updater(scale_updater)
    self.add(self.surface)
    self.interactive_embed()

# /////////////////////////////////////////////////
# iTime
# /////////////////////////////////////////////////

class Shaders06(AbstractShaderScene):
  shader_file = "fragment_06"
  def construct(self):
    self.set_resolution_uniform()
    self.surface.shader.set_uniform("u_scale", 1.0)

    iTime = 0.0

    def shader_updater(surface, dt):
        nonlocal iTime
        surface.shader.set_uniform("u_scale", self.window_scale())
        surface.shader.set_uniform("iTime", iTime)
        iTime += dt

    self.surface.add_updater(shader_updater)
    self.add(self.surface)
    self.interactive_embed()


class Shaders07(AbstractShaderScene):
  shader_file = "fragment_07"
  def construct(self):
        # 1. Placeholders for the very first frame
        self.set_resolution_uniform()
        self.surface.shader.set_uniform("u_scale", 1.0)
        self.surface.shader.set_uniform("iTime", 0.0)

        iTime = 0.0

        # 2. Updater to dynamically fix aspect ratio and animate time
        def shader_updater(surface, dt):
            nonlocal iTime
            window = getattr(self.renderer, "window", None)
            
            if window and window.width > 0:
                # Calculate scale based on actual window width
                scale = config.pixel_width / float(window.width)
                
                # Dynamically scale the resolution to match the actual window shape
                w = config.pixel_width
                h = window.height * scale
                
                surface.shader.set_uniform("iResolution", np.array([w, h], dtype=np.float32))
                surface.shader.set_uniform("u_scale", scale)
            else:
                surface.shader.set_uniform("iResolution", np.array([config.pixel_width, config.pixel_height], dtype=np.float32))
                surface.shader.set_uniform("u_scale", 1.0)

            surface.shader.set_uniform("iTime", iTime)
            iTime += dt

        # 3. Attach and run
        self.surface.add_updater(shader_updater)
        self.add(self.surface)
        # self.interactive_embed()
        self.add(self.surface)
        self.wait(16, frozen_frame=False)

class Shaders08(AbstractShaderScene):
  shader_file = "fragment_08"
  def construct(self):
        # 1. Placeholders for initial frame
        self.set_resolution_uniform()
        self.surface.shader.set_uniform("u_scale", 1.0)
        self.surface.shader.set_uniform("iTime", 0.0)

        iTime = 0.0

        # 2. Updater to dynamically fix aspect ratio and animate time
        def shader_updater(surface, dt):
            nonlocal iTime
            window = getattr(self.renderer, "window", None)
            
            if window and window.width > 0:
                # Calculate scale based on actual window width
                scale = config.pixel_width / float(window.width)
                
                # Dynamically scale the resolution to match the actual window shape
                w = config.pixel_width
                h = window.height * scale
                
                surface.shader.set_uniform("iResolution", np.array([w, h], dtype=np.float32))
                surface.shader.set_uniform("u_scale", scale)
            else:
                surface.shader.set_uniform("iResolution", np.array([config.pixel_width, config.pixel_height], dtype=np.float32))
                surface.shader.set_uniform("u_scale", 1.0)

            surface.shader.set_uniform("iTime", iTime)
            iTime += dt

        # 3. Attach and run
        self.surface.add_updater(shader_updater)
        self.add(self.surface)
        self.interactive_embed()

class Shaders09(AbstractShaderScene):
  shader_file = "fragment_09"
  
  def construct(self):
        # Set placeholders until the first frame renders
        self.set_resolution_uniform()
        self.surface.shader.set_uniform("u_scale", 1.0)
        self.surface.shader.set_uniform("iTime", 0.0)

        iTime = 0.0

        def shader_updater(surface, dt):
            nonlocal iTime
            window = getattr(self.renderer, "window", None)
            
            if window and window.width > 0:
                # Calculate scale based on width
                scale = config.pixel_width / float(window.width)
                
                # Dynamically scale the resolution to match the actual window shape
                w = config.pixel_width
                h = window.height * scale
                
                surface.shader.set_uniform("iResolution", np.array([w, h], dtype=np.float32))
                surface.shader.set_uniform("u_scale", scale)
            else:
                surface.shader.set_uniform("iResolution", np.array([config.pixel_width, config.pixel_height], dtype=np.float32))
                surface.shader.set_uniform("u_scale", 1.0)

            surface.shader.set_uniform("iTime", iTime)
            iTime += dt

        self.surface.add_updater(shader_updater)
        self.add(self.surface)
        self.interactive_embed()


class Shaders10(AbstractShaderScene):
  shader_file = "fragment_10"
  
  def construct(self) -> None:
    # Static uniforms
    self.set_resolution_uniform()                 # iResolution : vec2
    self.surface.shader.set_uniform("u_scale", 1.0)  # placeholder
    self.surface.shader.set_uniform("iTime", 0.0)    # placeholder

    iTime = 0.0

    def shader_updater(surface, dt):
      nonlocal iTime
      # window may not exist at construct() time — this is why
      # u_scale has to be (re)applied every frame.
      surface.shader.set_uniform("u_scale", self.window_scale())
      surface.shader.set_uniform("iTime", iTime)
      iTime += dt

    self.surface.add_updater(shader_updater)
    self.add(self.surface)
    self.interactive_embed()
