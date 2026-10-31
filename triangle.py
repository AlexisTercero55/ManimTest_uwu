from manim import *
import numpy as np

class TriangleInequalityLecture(Scene):
    def construct(self):
        # Title slide
        title = Text("The Triangle Inequality", font_size=48, color=BLUE)
        subtitle = Text("From Geometry to Abstract Spaces", font_size=24, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Part 1: Geometric interpretation
        self.geometric_interpretation()
        
        # Part 2: Algebraic formulation
        self.algebraic_formulation()
        
        # Part 3: Metric spaces
        self.metric_spaces_explanation()
        
        # Part 4: Normed spaces
        self.normed_spaces_explanation()
        
        # Part 5: Applications and implications
        self.applications_and_implications()

    def geometric_interpretation(self):
        title = Text("1. Geometric Interpretation", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create triangle
        A = LEFT * 3 + DOWN * 2
        B = RIGHT * 3 + DOWN * 2
        C = UP * 2
        
        triangle = Polygon(A, B, C, color=WHITE, stroke_width=3)
        vertices = VGroup(
            Dot(A, color=RED), Dot(B, color=RED), Dot(C, color=RED)
        )
        
        # Labels
        labels = VGroup(
            Text("A", font_size=24).next_to(A, DL, buff=0.1),
            Text("B", font_size=24).next_to(B, DR, buff=0.1),
            Text("C", font_size=24).next_to(C, UP, buff=0.1)
        )
        
        self.play(Create(triangle), Create(vertices), Write(labels))
        self.wait(1)
        
        # Show sides with measurements
        side_AB = Line(A, B, color=YELLOW, stroke_width=6)
        side_BC = Line(B, C, color=GREEN, stroke_width=6)
        side_CA = Line(C, A, color=PURPLE, stroke_width=6)
        
        # Calculate actual lengths for demonstration
        ab_length = np.linalg.norm(B - A)
        bc_length = np.linalg.norm(C - B)
        ca_length = np.linalg.norm(A - C)
        
        length_labels = VGroup(
            Text(f"|AB| = {ab_length:.2f}", font_size=20, color=YELLOW)
            .next_to(side_AB, DOWN, buff=0.1),
            Text(f"|BC| = {bc_length:.2f}", font_size=20, color=GREEN)
            .next_to(side_BC, RIGHT, buff=0.1),
            Text(f"|CA| = {ca_length:.2f}", font_size=20, color=PURPLE)
            .next_to(side_CA, LEFT, buff=0.1)
        )
        
        # Animate sides one by one
        self.play(Create(side_AB), Create(length_labels[0]))
        self.wait(0.5)
        self.play(Create(side_BC), Write(length_labels[1]))
        self.wait(0.5)
        self.play(Create(side_CA), Write(length_labels[2]))
        self.wait(1)
        
        # Show the inequalities
        inequalities = VGroup(
            MathTex("|AB| + |BC| > |AC|", font_size=28),
            MathTex("|BC| + |CA| > |AB|", font_size=28),
            MathTex("|CA| + |AB| > |BC|", font_size=28)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        inequalities.next_to(triangle, DOWN, buff=1)
        
        # Verify with actual numbers
        verification = VGroup(
            MathTex(f"{ab_length:.2f} + {bc_length:.2f} > {ca_length:.2f}", font_size=24),
            MathTex(f"{bc_length:.2f} + {ca_length:.2f} > {ab_length:.2f}", font_size=24),
            MathTex(f"{ca_length:.2f} + {ab_length:.2f} > {bc_length:.2f}", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        verification.next_to(inequalities, DOWN, buff=0.5)
        
        self.play(Write(inequalities))
        self.wait(1)
        self.play(Write(verification))
        self.wait(2)
        
        # Degenerate case - collinear points
        degenerate_text = Text("Equality case: Collinear points", font_size=24, color=ORANGE)
        degenerate_text.next_to(verification, DOWN, buff=0.8)
        
        A2 = LEFT * 3
        B2 = ORIGIN
        C2 = RIGHT * 3
        
        collinear_points = VGroup(
            Dot(A2, color=RED), Dot(B2, color=RED), Dot(C2, color=RED)
        )
        collinear_line = Line(A2, C2, color=WHITE, stroke_width=2)
        
        collinear_group = VGroup(collinear_points, collinear_line)
        collinear_group.next_to(degenerate_text, DOWN, buff=0.5)
        
        self.play(Write(degenerate_text))
        self.play(Create(collinear_line), Create(collinear_points))
        
        equality_eq = MathTex("|AB| + |BC| = |AC|", font_size=28)
        equality_eq.next_to(collinear_group, DOWN, buff=0.3)
        
        self.play(Write(equality_eq))
        self.wait(2)
        
        # Clear for next section
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def algebraic_formulation(self):
        title = Text("2. Algebraic Formulation", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Show the general inequality
        general_ineq = MathTex("|x + y| \\leq |x| + |y|", font_size=40)
        general_ineq.shift(UP * 2)
        
        self.play(Write(general_ineq))
        self.wait(1)
        
        # Proof visualization
        proof_title = Text("Proof Strategy:", font_size=24, color=GREEN)
        proof_title.next_to(general_ineq, DOWN, buff=1)
        
        proof_steps = VGroup(
            MathTex("|x + y|^2 = (x + y)^2", font_size=24),
            MathTex("= x^2 + 2xy + y^2", font_size=24),
            MathTex("\\leq |x|^2 + 2|x||y| + |y|^2", font_size=24),
            MathTex("= (|x| + |y|)^2", font_size=24)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        proof_steps.next_to(proof_title, DOWN, buff=0.5)
        
        self.play(Write(proof_title))
        self.wait(0.5)
        
        for step in proof_steps:
            self.play(Write(step))
            self.wait(0.5)
        
        # Number line demonstration
        number_line = NumberLine(x_range=[-5, 5], length=10, include_numbers=True)
        number_line.shift(DOWN * 2)
        
        x_val = 2
        y_val = 3
        
        x_point = number_line.n2p(x_val)
        y_point = number_line.n2p(y_val)
        sum_point = number_line.n2p(x_val + y_val)
        
        x_dot = Dot(x_point, color=RED)
        y_dot = Dot(y_point, color=GREEN)
        sum_dot = Dot(sum_point, color=BLUE)
        
        x_label = MathTex("x", font_size=20, color=RED).next_to(x_dot, UP, buff=0.1)
        y_label = MathTex("y", font_size=20, color=GREEN).next_to(y_dot, UP, buff=0.1)
        sum_label = MathTex("x+y", font_size=20, color=BLUE).next_to(sum_dot, UP, buff=0.1)
        
        self.play(Create(number_line))
        self.play(Create(x_dot), Write(x_label))
        self.play(Create(y_dot), Write(y_label))
        self.play(Create(sum_dot), Write(sum_label))
        
        # Show the inequality on number line
        abs_x = MathTex(f"|x| = {abs(x_val)}", font_size=20, color=RED)
        abs_y = MathTex(f"|y| = {abs(y_val)}", font_size=20, color=GREEN)
        abs_sum = MathTex(f"|x+y| = {abs(x_val + y_val)}", font_size=20, color=BLUE)
        sum_abs = MathTex(f"|x|+|y| = {abs(x_val) + abs(y_val)}", font_size=20, color=YELLOW)
        
        abs_group = VGroup(abs_x, abs_y, abs_sum, sum_abs).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        abs_group.next_to(number_line, DOWN, buff=1)
        
        self.play(Write(abs_group))
        self.wait(2)
        
        # Clear for next section
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def metric_spaces_explanation(self):
        title = Text("3. Metric Spaces", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Definition of metric space
        definition = Text("A metric space is a set M with a distance function d:", font_size=20)
        definition.shift(UP * 2.5)
        
        axioms = VGroup(
            MathTex("1.\\, d(x,y) \\geq 0 \\text{ and } d(x,y) = 0 \\iff x = y", font_size=20),
            MathTex("2.\\, d(x,y) = d(y,x)", font_size=20),
            MathTex("3.\\, d(x,z) \\leq d(x,y) + d(y,z) \\quad \\text{(Triangle Inequality)}", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        axioms.next_to(definition, DOWN, buff=0.5)
        
        self.play(Write(definition))
        self.wait(0.5)
        for axiom in axioms:
            self.play(Write(axiom))
            self.wait(0.5)
        
        # Visualize the triangle inequality in metric space
        points_text = Text("Visualizing the triangle inequality:", font_size=18)
        points_text.next_to(axioms, DOWN, buff=1)
        
        # Create three points in "abstract" space
        points = [
            LEFT * 2 + UP,
            RIGHT * 2 + UP,
            DOWN * 1.5
        ]
        
        dots = VGroup(*[Dot(point, color=RED, radius=0.08) for point in points])
        labels = VGroup(
            MathTex("x", font_size=16).next_to(points[0], UL, buff=0.1),
            MathTex("y", font_size=16).next_to(points[1], UR, buff=0.1),
            MathTex("z", font_size=16).next_to(points[2], DOWN, buff=0.1)
        )
        
        # Draw distances
        dist_xy = DashedLine(points[0], points[1], color=YELLOW)
        dist_yz = DashedLine(points[1], points[2], color=GREEN)
        dist_xz = DashedLine(points[0], points[2], color=BLUE)
        
        dist_labels = VGroup(
            MathTex("d(x,y)", font_size=14, color=YELLOW).move_to((points[0] + points[1])/2 + UP*0.3),
            MathTex("d(y,z)", font_size=14, color=GREEN).move_to((points[1] + points[2])/2 + RIGHT*0.3),
            MathTex("d(x,z)", font_size=14, color=BLUE).move_to((points[0] + points[2])/2 + LEFT*0.3)
        )
        
        inequality = MathTex("d(x,z) \\leq d(x,y) + d(y,z)", font_size=24, color=ORANGE)
        inequality.next_to(points_text, DOWN, buff=1.5)
        
        self.play(Write(points_text))
        self.play(Create(dots), Write(labels))
        self.play(Create(dist_xy), Write(dist_labels[0]))
        self.wait(0.5)
        self.play(Create(dist_yz), Write(dist_labels[1]))
        self.wait(0.5)
        self.play(Create(dist_xz), Write(dist_labels[2]))
        self.wait(0.5)
        self.play(Write(inequality))
        
        # Arrow showing the "detour" is longer
        arrow = CurvedArrow(
            points[0] + RIGHT*0.5 + DOWN*0.5,
            points[2] + LEFT*0.5 + UP*0.5,
            angle=-TAU/4,
            color=RED
        )
        arrow_label = Text("Direct path is shortest", font_size=12, color=RED)
        arrow_label.next_to(arrow, RIGHT, buff=0.1)
        
        self.play(Create(arrow), Write(arrow_label))
        self.wait(2)
        
        # Clear for next section
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def normed_spaces_explanation(self):
        title = Text("4. Normed Vector Spaces", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Definition
        definition = Text("In a normed space (V, ‖·‖):", font_size=20)
        definition.shift(UP * 2.5)
        
        norm_axioms = VGroup(
            MathTex("\\|x\\| \\geq 0 \\text{ and } \\|x\\| = 0 \\iff x = 0", font_size=20),
            MathTex("\\|\\alpha x\\| = |\\alpha|\\cdot\\|x\\|", font_size=20),
            MathTex("\\|x + y\\| \\leq \\|x\\| + \\|y\\|", font_size=20)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        norm_axioms.next_to(definition, DOWN, buff=0.5)
        
        self.play(Write(definition))
        self.wait(0.5)
        for axiom in norm_axioms:
            self.play(Write(axiom))
            self.wait(0.5)
        
        # Vector addition visualization
        vec_text = Text("Vector Addition Visualization:", font_size=18)
        vec_text.next_to(norm_axioms, DOWN, buff=1)
        
        # Create coordinate system
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            x_length=6,
            y_length=4,
            axis_config={"color": BLUE}
        )
        axes.shift(DOWN * 1)
        
        # Define vectors
        vec_x = [2, 1]
        vec_y = [1, 1.5]
        vec_sum = [vec_x[0] + vec_y[0], vec_x[1] + vec_y[1]]
        
        # Create vector arrows
        arrow_x = Arrow(axes.c2p(0, 0), axes.c2p(*vec_x), color=RED, buff=0)
        arrow_y = Arrow(axes.c2p(0, 0), axes.c2p(*vec_y), color=GREEN, buff=0)
        arrow_sum = Arrow(axes.c2p(0, 0), axes.c2p(*vec_sum), color=BLUE, buff=0)
        arrow_y_shifted = Arrow(axes.c2p(*vec_x), axes.c2p(*vec_sum), color=GREEN, buff=0)
        
        # Labels
        vec_labels = VGroup(
            MathTex("\\vec{x}", font_size=16, color=RED).next_to(arrow_x.get_center(), UL, buff=0.1),
            MathTex("\\vec{y}", font_size=16, color=GREEN).next_to(arrow_y.get_center(), DL, buff=0.1),
            MathTex("\\vec{x} + \\vec{y}", font_size=16, color=BLUE).next_to(arrow_sum.get_center(), UR, buff=0.1)
        )
        
        self.play(Write(vec_text))
        self.play(Create(axes))
        self.play(Create(arrow_x), Write(vec_labels[0]))
        self.wait(0.5)
        self.play(Create(arrow_y), Write(vec_labels[1]))
        self.wait(0.5)
        self.play(Create(arrow_sum), Write(vec_labels[2]))
        self.wait(0.5)
        self.play(Create(arrow_y_shifted))
        
        # Show the parallelogram law connection
        parallelogram_text = Text("The triangle inequality ensures the direct path\nis shorter than the sum of individual paths", 
                                font_size=14, color=YELLOW)
        parallelogram_text.next_to(axes, DOWN, buff=0.5)
        
        self.play(Write(parallelogram_text))
        self.wait(2)
        
        # Clear for next section
        self.play(*[FadeOut(mob) for mob in self.mobjects])

    def applications_and_implications(self):
        title = Text("5. Applications and Implications", font_size=36, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Convergence implications
        convergence_title = Text("Convergence and Continuity:", font_size=20, color=GREEN)
        convergence_title.shift(UP * 2)
        
        convergence_points = VGroup(
            MathTex("\\text{If } d(x_n, L) \\to 0 \\text{ and } d(x_n, L') \\to 0", font_size=18),
            MathTex("\\text{Then } d(L, L') \\leq d(L, x_n) + d(x_n, L') \\to 0", font_size=18),
            MathTex("\\Rightarrow L = L' \\text{ (Uniqueness of limits)}", font_size=18)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        convergence_points.next_to(convergence_title, DOWN, buff=0.5)
        
        self.play(Write(convergence_title))
        self.wait(0.5)
        for point in convergence_points:
            self.play(Write(point))
            self.wait(0.5)
        
        # L^p spaces
        lp_title = Text("L^p Spaces (Minkowski's Inequality):", font_size=20, color=ORANGE)
        lp_title.next_to(convergence_points, DOWN, buff=1)
        
        minkowski = MathTex(
            "\\left(\\int |f + g|^p\\, d\\mu\\right)^{1/p} \\leq \\left(\\int |f|^p\\, d\\mu\\right)^{1/p} + \\left(\\int |g|^p\\, d\\mu\\right)^{1/p}",
            font_size=16
        )
        minkowski.next_to(lp_title, DOWN, buff=0.3)
        
        self.play(Write(lp_title))
        self.play(Write(minkowski))
        self.wait(1)
        
        # Modern applications
        modern_title = Text("Modern Applications:", font_size=20, color=PURPLE)
        modern_title.next_to(minkowski, DOWN, buff=1)
        
        applications = VGroup(
            Text("• Machine Learning: Kernel methods", font_size=16),
            Text("• Data Science: Nearest neighbor search", font_size=16),
            Text("• Computer Science: Metric embeddings", font_size=16),
            Text("• Probability: Concentration of measure", font_size=16)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        applications.next_to(modern_title, DOWN, buff=0.5)
        
        self.play(Write(modern_title))
        self.wait(0.5)
        for app in applications:
            self.play(Write(app))
            self.wait(0.3)
        
        # Final summary
        summary_text = Text("The triangle inequality is fundamental to", font_size=18)
        summary_text2 = Text("constructing coherent mathematical spaces", font_size=18)
        summary_text2.next_to(summary_text, DOWN, buff=0.1)
        summary_group = VGroup(summary_text, summary_text2)
        summary_group.next_to(applications, DOWN, buff=1)
        
        self.play(Write(summary_group))
        self.wait(3)

# Additional specialized scene for interactive demonstration
class InteractiveTriangleDemo(Scene):
    def construct(self):
        title = Text("Interactive Triangle Inequality Demo", font_size=32, color=BLUE)
        title.to_edge(UP)
        
        # Create draggable points
        A = Dot(LEFT * 2 + DOWN, color=RED)
        B = Dot(RIGHT * 2 + DOWN, color=GREEN) 
        C = Dot(UP, color=BLUE)
        
        A_label = Text("A", font_size=20, color=RED).next_to(A, DL, buff=0.1)
        B_label = Text("B", font_size=20, color=GREEN).next_to(B, DR, buff=0.1)
        C_label = Text("C", font_size=20, color=BLUE).next_to(C, UP, buff=0.1)
        
        triangle = always_redraw(lambda: Polygon(
            A.get_center(), B.get_center(), C.get_center(), 
            color=WHITE, stroke_width=3
        ))
        
        # Dynamic side lengths
        def get_side_lengths():
            a = B.get_center()
            b = C.get_center()
            c = A.get_center()
            return [
                np.linalg.norm(a - b),
                np.linalg.norm(b - c),
                np.linalg.norm(c - a)
            ]
        
        side_text = always_redraw(lambda: VGroup(
            MathTex(f"|AB| = {get_side_lengths()[0]:.2f}", font_size=18),
            MathTex(f"|BC| = {get_side_lengths()[1]:.2f}", font_size=18),
            MathTex(f"|CA| = {get_side_lengths()[2]:.2f}", font_size=18)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_edge(LEFT))
        
        inequality_text = always_redraw(lambda: VGroup(
            MathTex(f"{get_side_lengths()[0]:.2f} + {get_side_lengths()[1]:.2f} > {get_side_lengths()[2]:.2f}", 
                   font_size=18, color=GREEN if get_side_lengths()[0] + get_side_lengths()[1] > get_side_lengths()[2] else RED),
            MathTex(f"{get_side_lengths()[1]:.2f} + {get_side_lengths()[2]:.2f} > {get_side_lengths()[0]:.2f}", 
                   font_size=18, color=GREEN if get_side_lengths()[1] + get_side_lengths()[2] > get_side_lengths()[0] else RED),
            MathTex(f"{get_side_lengths()[2]:.2f} + {get_side_lengths()[0]:.2f} > {get_side_lengths()[1]:.2f}", 
                   font_size=18, color=GREEN if get_side_lengths()[2] + get_side_lengths()[0] > get_side_lengths()[1] else RED)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1).to_edge(RIGHT))
        
        self.play(Write(title))
        self.play(Create(A), Create(B), Create(C))
        self.play(Write(A_label), Write(B_label), Write(C_label))
        self.play(Create(triangle))
        self.play(Write(side_text), Write(inequality_text))
        
        # Demonstrate by moving points
        self.play(
            A.animate.move_to(LEFT * 3 + DOWN * 1.5),
            B.animate.move_to(RIGHT * 1 + DOWN * 2),
            C.animate.move_to(UP * 0.5 + RIGHT * 0.5)
        )
        self.wait(1)
        
        # Try to break the inequality (make points collinear)
        self.play(
            A.animate.move_to(LEFT * 3),
            B.animate.move_to(ORIGIN),
            C.animate.move_to(RIGHT * 3)
        )
        self.wait(2)