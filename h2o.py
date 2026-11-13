import numpy as np
from manim import (
    BLUE_B,
    DEGREES,
    DOWN,
    FadeIn,
    FadeOut,
    GREEN_A,
    GREEN_E,
    LEFT,
    LaggedStart,
    Line,
    ORANGE,
    ParametricFunction,
    RED_D,
    RIGHT,
    Sphere,
    TAU,
    Text,
    ThreeDScene,
    UP,
    VGroup,
    WHITE,
    YELLOW,
    Create,
    config,
)
from manim.utils.opengl import perspective_projection_matrix

ELECTRIC_BLUE = "#7DF9FF"

config.frame_width = config.frame_height * 9 / 16


def uri_txt(v=(0, 0, 0)):
    name = Text(
        "@uri.sab",
        t2c={
            "[:1]": "#3174f0",
            "[1:2]": "#e53125",
            "[2:3]": "#fbb003",
            "[3:5]": "#269a43",
            "[5:6]": "#e53125",
            "[6:7]": "#fbb003",
            "[7:]": "#3174f0",
        },
        font_size=40,
        font="Avenir",
    )
    return name.move_to(np.array(v, dtype=float))


class WaterMolecule(ThreeDScene):
    bond_angle = 104.5 * DEGREES
    bond_length = 1.0
    oxygen_radius = 0.34
    hydrogen_radius = 0.23

    @staticmethod
    def make_particle(position, radius, color):
        return Sphere(
            radius=radius,
            resolution=(12, 8),
            fill_color=color,
            fill_opacity=1,
            checkerboard_colors=False,
            stroke_opacity=0,
        ).move_to(position)

    @staticmethod
    def make_orbit(center, radius, plane):
        def point(t):
            coordinates = np.array([np.cos(t), np.sin(t), 0.0])
            if plane == "xz":
                coordinates = np.array([np.cos(t), 0.0, np.sin(t)])
            elif plane == "yz":
                coordinates = np.array([0.0, np.cos(t), np.sin(t)])
            return center + radius * coordinates

        return VGroup(
            ParametricFunction(
                point,
                t_range=(0, TAU),
                color=ORANGE,
                stroke_width=14,
                stroke_opacity=0.05,
            ),
            ParametricFunction(
                point,
                t_range=(0, TAU),
                color=ORANGE,
                stroke_width=8,
                stroke_opacity=0.16,
            ),
            ParametricFunction(
                point,
                t_range=(0, TAU),
                color=ORANGE,
                stroke_width=2.5,
                stroke_opacity=0.9,
            ),
        )

    def make_atom(self, center, element):
        if element == "O":
            radius = self.oxygen_radius
            protons, neutrons = 8, 8
            nucleon_radius, nucleus_radius = 0.042, 0.075
            shells = [(0.13, 2, "xy"), (0.255, 6, "xz")]
        else:
            radius = self.hydrogen_radius
            protons, neutrons = 1, 0
            nucleon_radius, nucleus_radius = 0.057, 0.0
            shells = [(0.155, 1, "yz")]

        nucleons = VGroup()
        count = protons + neutrons
        golden_angle = np.pi * (3 - np.sqrt(5))
        for index in range(count):
            y = 1 - 2 * (index + 0.5) / count
            ring_radius = np.sqrt(1 - y * y)
            direction = np.array(
                [
                    np.cos(index * golden_angle) * ring_radius,
                    y,
                    np.sin(index * golden_angle) * ring_radius,
                ]
            )
            color = BLUE_B if index < protons else ELECTRIC_BLUE
            nucleons.add(
                self.make_particle(
                    center + nucleus_radius * direction,
                    nucleon_radius,
                    color,
                )
            )

        orbitals = VGroup()
        electrons = VGroup()
        for shell_radius, electron_count, plane in shells:
            orbitals.add(self.make_orbit(center, shell_radius, plane))
            for index in range(electron_count):
                angle = TAU * index / electron_count
                if plane == "xz":
                    offset = shell_radius * np.array(
                        [np.cos(angle), 0.0, np.sin(angle)]
                    )
                elif plane == "yz":
                    offset = shell_radius * np.array(
                        [0.0, np.cos(angle), np.sin(angle)]
                    )
                else:
                    offset = shell_radius * np.array(
                        [np.cos(angle), np.sin(angle), 0.0]
                    )
                electrons.add(
                    self.make_particle(center + offset, 0.027, RED_D)
                )

        shell = Sphere(
            radius=radius,
            resolution=(48, 32),
            fill_color=WHITE if element == "H" else RED_D,
            fill_opacity=0.1,
            checkerboard_colors=False,
            stroke_opacity=0,
        ).move_to(center)
        label = Text(
            element,
            font_size=24,
            font="Avenir",
            color=YELLOW,
            weight="BOLD",
        ).move_to(center + DOWN * (radius + 0.36))
        return {
            "center": np.array(center, dtype=float),
            "shell": shell,
            "orbitals": orbitals,
            "nucleons": nucleons,
            "electrons": electrons,
            "label": label,
            "model": VGroup(shell, orbitals, nucleons, electrons, label),
        }

    def construct(self) -> None:
        self.renderer.background_color = "#0B1020"
        self.camera.frame_shape = (config.frame_width, config.frame_height)
        self.camera.set_width(config.frame_width, stretch=True)
        self.camera.set_height(config.frame_height, stretch=True)
        self.camera.projection_matrix = perspective_projection_matrix(
            width=config.frame_width / 6,
            height=config.frame_height / 6,
        )
        self.set_camera_orientation(
            phi=50 * DEGREES,
            theta=-55 * DEGREES,
            zoom=1.62,
        )

        grid_color = "#C0C0C0"
        grid_lines = VGroup(
            *[
                Line(
                    [x, -config.frame_height / 2, 0],
                    [x, config.frame_height / 2, 0],
                    color=grid_color,
                    stroke_width=0.8,
                    stroke_opacity=0.04,
                )
                for x in np.arange(
                    -config.frame_width / 2,
                    config.frame_width / 2 + 0.01,
                    0.4,
                )
            ],
            *[
                Line(
                    [-config.frame_width / 2, y, 0],
                    [config.frame_width / 2, y, 0],
                    color=grid_color,
                    stroke_width=0.8,
                    stroke_opacity=0.04,
                )
                for y in np.arange(
                    -config.frame_height / 2,
                    config.frame_height / 2 + 0.01,
                    0.4,
                )
            ],
        )
        grid_lines.stretch(2.8, dim=0)
        self.add_fixed_in_frame_mobjects(grid_lines)
        grid_motion = {"time": 0.0, "offset": np.zeros(3)}

        def drift_grid(grid, dt):
            grid_motion["time"] += dt
            time = grid_motion["time"]
            offset = np.array(
                [
                    0.045 * np.sin(0.19 * time)
                    + 0.02 * np.sin(0.071 * time + 1.0),
                    0.04 * np.sin(0.17 * time + 2.0)
                    + 0.025 * np.sin(0.093 * time),
                    0.0,
                ]
            )
            grid.shift(offset - grid_motion["offset"])
            grid_motion["offset"] = offset

        grid_lines.add_updater(drift_grid)
        self.play(FadeIn(grid_lines), run_time=0.6)

        title = Text(
            "DEL ÁTOMO A LA\nMOLÉCULA DE AGUA",
            font_size=34,
            font="Avenir",
            color=ELECTRIC_BLUE,
            weight="BOLD",
            line_spacing=0.8,
        ).stretch(1.8, dim=0).to_edge(UP, buff=0.65)
        legend = VGroup(
            Text("PROTÓN", font_size=18, font="Avenir", color=BLUE_B),
            Text(
                "NEUTRÓN",
                font_size=18,
                font="Avenir",
                color=ELECTRIC_BLUE,
            ),
            Text("ELECTRÓN", font_size=18, font="Avenir", color=RED_D),
            Text("ÓRBITA", font_size=18, font="Avenir", color=ORANGE),
        ).arrange(RIGHT, buff=0.1)
        legend.stretch(2.5, dim=0).next_to(title, DOWN, buff=0.16)
        username = uri_txt().to_corner(UP + RIGHT, buff=0.22).shift(RIGHT * 4.25)
        self.add_fixed_in_frame_mobjects(title, legend, username)

        def text_glyphs(mobject):
            return [
                member
                for member in mobject.get_family()[1:]
                if not member.submobjects
            ]

        def write_text(mobject, run_time=1.4):
            glyphs = text_glyphs(mobject)
            return LaggedStart(
                *[
                    FadeIn(glyph, shift=UP * 0.025)
                    for glyph in glyphs
                ],
                lag_ratio=0.035,
                run_time=run_time,
            )

        def erase_text(mobject, run_time=0.8):
            return FadeOut(mobject, shift=DOWN * 0.025, run_time=run_time)

        author_glyphs = text_glyphs(username)
        author_cycle = {"time": 0.0}
        username.set_opacity(0)

        def animate_author(author, dt):
            author_cycle["time"] += dt
            phase = author_cycle["time"] % 5.6
            write_duration = 1.2
            hold_duration = 1.0
            erase_duration = 1.2
            if phase < write_duration:
                progress = phase / write_duration
            elif phase < write_duration + hold_duration:
                progress = 1.0
            elif phase < write_duration + hold_duration + erase_duration:
                progress = 1.0 - (
                    phase - write_duration - hold_duration
                ) / erase_duration
            else:
                progress = 0.0
            glyph_count = len(author_glyphs)
            for index, glyph in enumerate(author_glyphs):
                glyph_progress = np.clip(progress * glyph_count - index, 0, 1)
                opacity = glyph_progress * glyph_progress * (
                    3 - 2 * glyph_progress
                )
                glyph.set_opacity(opacity)

        username.add_updater(animate_author)
        self.play(
            write_text(title, run_time=2.0),
            write_text(legend, run_time=1.8),
            run_time=2.0,
        )

        spawn = np.zeros(3)
        oxygen_center = np.array([0.0, 0.85, 0.0])
        half_angle = self.bond_angle / 2
        hydrogen_vectors = [
            self.bond_length
            * np.array([sign * np.sin(half_angle), -np.cos(half_angle), 0.0])
            for sign in (-1, 1)
        ]
        hydrogen_centers = [oxygen_center + vector for vector in hydrogen_vectors]

        def narration(text):
            return (
                Text(text, font_size=18, font="Avenir", color=WHITE)
                .stretch(2.8, dim=0)
                .to_edge(DOWN, buff=0.9)
            )

        oxygen = self.make_atom(spawn, "O")
        oxygen["model"].scale(1.7, about_point=spawn)

        oxygen_caption = narration(
            "El oxígeno tiene seis\nelectrones externos.",
        )
        self.add_fixed_in_frame_mobjects(oxygen_caption)
        self.play(
            FadeIn(oxygen["orbitals"]),
            write_text(oxygen_caption, run_time=1.1),
            run_time=1.4,
        )
        self.play(
            FadeIn(oxygen["nucleons"]),
            FadeIn(oxygen["electrons"]),
            run_time=1.1,
        )
        self.play(
            FadeIn(oxygen["shell"]),
            write_text(oxygen["label"], run_time=0.8),
            run_time=0.8,
        )
        self.wait(2.5)
        self.play(
            oxygen["model"]
            .animate.scale(1 / 1.7, about_point=spawn)
            .shift(oxygen_center - spawn),
            run_time=1.5,
        )

        hydrogen_caption = narration("Cada hidrógeno aporta\nun electrón.")
        self.play(erase_text(oxygen_caption))
        self.remove_fixed_in_frame_mobjects(oxygen_caption)
        self.add_fixed_in_frame_mobjects(hydrogen_caption)
        self.play(write_text(hydrogen_caption, run_time=0.9))

        for target in hydrogen_centers:
            hydrogen = self.make_atom(spawn, "H")
            hydrogen["model"].scale(1.5, about_point=spawn)
            self.play(
                FadeIn(hydrogen["orbitals"]),
                FadeIn(hydrogen["nucleons"]),
                FadeIn(hydrogen["electrons"]),
                FadeIn(hydrogen["shell"]),
                write_text(hydrogen["label"], run_time=1.1),
                run_time=1.1,
            )
            self.wait(0.8)
            self.play(
                hydrogen["model"]
                .animate.scale(1 / 1.5, about_point=spawn)
                .shift(target - spawn),
                run_time=1.5,
            )
        self.wait(1.5)

        bonds = VGroup(
            *[
                VGroup(
                    *[
                        ParametricFunction(
                            lambda t, direction=vector: oxygen_center
                            + (
                                self.oxygen_radius
                                + t
                                * (
                                    np.linalg.norm(direction)
                                    - self.oxygen_radius
                                    - self.hydrogen_radius
                                )
                            )
                            * direction
                            / np.linalg.norm(direction),
                            t_range=(0, 1),
                            color=ELECTRIC_BLUE,
                            stroke_width=width,
                            stroke_opacity=opacity,
                        )
                        for width, opacity in ((20, 0.07), (11, 0.2), (4, 1))
                    ]
                )
                for vector in hydrogen_vectors
            ]
        )
        bond_caption = narration(
            "El oxígeno comparte\n"
            "un electrón con cada H:\n"
            "formando dos enlaces O–H.",
        )
        self.play(erase_text(hydrogen_caption))
        self.remove_fixed_in_frame_mobjects(hydrogen_caption)
        self.add_fixed_in_frame_mobjects(bond_caption)
        self.play(
            Create(bonds),
            write_text(bond_caption, run_time=1.3),
            run_time=1.8,
        )
        self.wait(3.5)

        arc_radius = 0.62
        arc_start = -np.pi / 2 - half_angle
        angle_arc = ParametricFunction(
            lambda t: oxygen_center
            + arc_radius * np.array([np.cos(t), np.sin(t), 0.0]),
            t_range=(arc_start, arc_start + self.bond_angle),
            color=GREEN_A,
            stroke_width=7,
            stroke_opacity=0.65,
        )
        outer_arc = ParametricFunction(
            lambda t: oxygen_center
            + (arc_radius + 0.045)
            * np.array([np.cos(t), np.sin(t), 0.0]),
            t_range=(arc_start, arc_start + self.bond_angle),
            color=GREEN_E,
            stroke_width=2,
            stroke_opacity=0.35,
        )
        angle_caption = Text(
            "ÁNGULO H–O–H: 104,5°",
            font_size=23,
            font="Avenir",
            color=YELLOW,
            weight="BOLD",
        ).to_edge(DOWN, buff=2.0)
        shape_caption = narration(
            "Dos pares libres repelen\n"
            "los enlaces y dan al agua\n"
            "forma angular: 104,5°.",
        )
        self.play(erase_text(bond_caption))
        self.remove_fixed_in_frame_mobjects(bond_caption)
        self.add_fixed_in_frame_mobjects(angle_caption, shape_caption)
        self.play(
            Create(angle_arc),
            Create(outer_arc),
            write_text(angle_caption, run_time=1.0),
            write_text(shape_caption, run_time=1.2),
            run_time=1.8,
        )
        self.wait(3.5)

        polarity_caption = narration(
            "El oxígeno atrae más\n"
            "los electrones compartidos:\n"
            "por eso el agua es polar.",
        )
        self.play(erase_text(shape_caption))
        self.remove_fixed_in_frame_mobjects(shape_caption)
        self.add_fixed_in_frame_mobjects(polarity_caption)
        self.play(write_text(polarity_caption, run_time=1.2))
        self.wait(3.5)

        self.begin_ambient_camera_rotation(rate=TAU / 25, about="theta")
        self.wait(25, frozen_frame=False)
        self.stop_ambient_camera_rotation()
        username.clear_updaters()
        username.set_opacity(1)
        self.play(write_text(username, run_time=1.2))
        self.wait(0.5)
        self.interactive_embed()
