from manimlib.imports import *
import sympy as sympy
#https://talkingphysics.wordpress.com/2018/06/11/learning-how-to-animate-videos-using-manim-series-a-journey/

# 1) Scenes and Animation
# You must define each scene as a separate class that is a subclass of Scene. This class must have a construct() method.
# The construct() method is essentially the main method in the class that gets called when run through extract_scene.py.
# It is similar to __init__; construct() is the method that is automatically called when you create an instance of the class.
# add(): objects appear on the screen without any animation.
# play() is what processes the various animations you ask manim to perform.
# you can add multiple animation in play(), i.e. self.play(Rotating(square), FadeIn(circle))

# 2) Coordinate
# The coordinates are specified using numpy arrays np.array().
# The overall scale of the vectors (the relationship between pixels and MUnits) is set by the FRAME_HEIGHT
# Default screen height is 8 Units (as defined in constants.py). The default screen width is 14.2 MUnits
# ORIGIN, UP RIGHT LEFT, DOWN, IN, and OUT
# The center edge of each screen side is also defined by vectors TOP, BOTTOM, LEFT_SIDE, and RIGHT_SIDE.
#____________________________________________________
#|                       TOP                        |
#|                                                  |
#|                                                  |
#|LEFT_SIDE           RIGHT_SIDE          RIGHT_SIDE|
#|                                                  |
#|                                                  |
#|                                                  |
#|______________________BOTTOM______________________|

# 3) Constants
# A list of the named colors can be found in the COLOR_MAP dictionary located in the constants.py
# The constants.py file contains other useful defintions, such as direction vectors that can be used to place objects in the scene.
# For example, UP is a numpy array (0,1,0), which corresponds to 1 unit of distance.

# 4) Shapes
# Circle(), Square(), Line(), Polygon() Rectangle(), Ellipse(), Annulus(), Arrow(), CurvedArrow()
# Some possible keywords include radius, height, width, color, fill_color, and fill_opacity.
# For the Annulus() class we have inner_radius and outer_radius for keyword arguments.
# All shapes, with the exception of lines and arrows, are created at the origin (center of the screen, which is (0,0,0)).
# For the lines and arrows you need to specify the location of the two ends.

# Mobjects relocation methods:
# square.next_to(cirle, DOWN)
# square.move_to(4 * UP + LEFT_SIDE)
# square.flip(RIGHT)
# square.rotate(-3 * TAU / 8)
# text1.next_to(text2.get_corner(DOWN + RIGHT), DOWN)


# 5) Transformations
# Different types of transformations available in /animation/transform.py
# Examples:

# ApplyMethod(my_text.shift, 3 * UP)
# GrowFromCenter(line)
# ShowCreation(circle)
# FadeOut(circle)
# GrowFromCenter(square)
# Transform(square, triangle)

# 6) Text
# square=Square(side_length=5,fill_color=YELLOW, fill_opacity=1)
# label=TextMobject("Text at an angle")
# label.bg=BackgroundRectangle(label,fill_opacity=1)
# label_group=VGroup(label.bg,label) #Order matters
# label_group.rotate(TAU/8)
# label2=TextMobject("Boxed text",color=BLACK)
# label2.bg=SurroundingRectangle(label2,color=BLUE,fill_color=RED, fill_opacity=.5)
# label2_group=VGroup(label2,label2.bg)

# 7) Graphing Functions
# To plot something inherit from  <<GraphScene>>.
# self.setup_axes() will create a set of axes on screen.
# All other variables for the axes are set using CONFIG{},
# Axes belong to your scene class so you will need to use self to access the methods related to the axes
# Once you have the axes set up you can use self.get_graph() to graph a function.
# we could use lambda functions. For example:
# self.func = lambda x: np.cos(x)
# self.get_graph(self.func)

# input_to_graph_point():  By specifying an x-value on the graph, this method will return the coordinate on the screen
# where that graph point lies. This is handy if you want to place some text or other mobject to call out a particular
# point on a graph.

# 8) 3D Scenes
# Similar to 2D. You must inherite from <<ThreeDScene>> you can now move the camera around using self.move_camera()
# set_camera_position(phi, theta, distance, center_x, center_y, and center_z): moves the camera to the specified location and orientation. The camera will abruptly jump to the given location.
# move_camera(): If we want a smooth camera transition (panning the camera)

#                Z
#                |        r,θ,φ
#                |        /|
#                |    r /  |
#                |    /    |
#                |φ /      |
#                |/________|________ Y
#               /θ\        |
#              /    \      |
#             /       \    |
#            /          \  |
#           /             \|
#          X
class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        line = Line(np.array([0, 0, 0]), np.array([5, 1, 3]))
        triangle = Polygon(np.array([0, 0, 0]), np.array([1, 1, 0]), np.array([1, -1, 0]))

        self.add(line)
        self.play(GrowFromCenter(line))
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square, triangle))

        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(4*UP+LEFT_SIDE )
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        self.play(FadeIn(square))
        self.play(Rotating(square), FadeIn(circle))

        annulus=Annulus()
        self.play(FadeIn(annulus))

        arrow=CurvedArrow(np.array([0,0,0]) ,np.array([2,3,1]))
        self.play(ShowCreation(arrow))
        self.wait(3)

class AddingText(Scene):
# Adding text on the screen
    def construct(self):
        my_first_text = TextMobject("Writing with manim is fun")
        second_line = TextMobject("and easy to do!")
        second_line.next_to(my_first_text, DOWN)
        third_line = TextMobject("for me and you!")
        third_line.next_to(my_first_text, DOWN)

        self.add(my_first_text, second_line)
        self.wait(2)
        self.play(Transform(second_line, third_line))
        self.wait(2)
        second_line.shift(3 * DOWN)
        self.play(ApplyMethod(my_first_text.shift, 3 * UP))
        self.wait(2)
        self.play(ApplyMethod(my_first_text.rotate, -3 * TAU / 8))

class AddingMoreText(Scene):
    # Playing around with text properties
    def construct(self):
        quote = TextMobject("Imagination is more important than knowledge")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject("A person who never made a mistake never tried anything new")
        quote2.set_color(YELLOW)
        author = TextMobject("-Albert Einstein")
        author.scale(0.75)
        author.next_to(quote.get_corner(DOWN + RIGHT), DOWN)

        self.add(quote)
        self.add(author)
        self.wait(2)
        #self.play(Transform(quote, quote2))
        self.play(Transform(quote, quote2), ApplyMethod(author.move_to, quote2.get_corner(DOWN + RIGHT) + DOWN + 2 * LEFT))
        self.play(ApplyMethod(author.match_color, quote2), Transform(author, author.scale(1)))
        #self.play(FadeOut(quote))


        square = Square(side_length=5, fill_color=YELLOW, fill_opacity=1)
        label = TextMobject("Text at an angle")
        label.bg = BackgroundRectangle(label, fill_opacity=1)
        label_group = VGroup(label.bg, label)  # Order matters
        label_group.rotate(TAU / 8)
        label2 = TextMobject("Boxed text", color=BLACK)
        label2.bg = SurroundingRectangle(label2, color=BLUE, fill_color=RED, fill_opacity=.5)
        label2_group = VGroup(label2, label2.bg)
        label2_group.next_to(label_group, DOWN)
        label3 = TextMobject("Rainbow")
        label3.scale(2)
        label3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        label3.to_edge(DOWN)

        self.add(square)
        self.play(FadeIn(label_group))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))

class AligningTextUsingBraces(Scene):
    def construct(self):
        eq1A = TextMobject("4x + 3y")
        eq1B = TextMobject("=")
        eq1C = TextMobject("0")
        eq2A = TextMobject("5x -2y")
        eq2B = TextMobject("=")
        eq2C = TextMobject("3")
        eq1B.next_to(eq1A, RIGHT)
        eq1C.next_to(eq1B, RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A, LEFT)
        eq2B.align_to(eq1B, LEFT)
        eq2C.align_to(eq1C, LEFT)

        eq_group = VGroup(eq1A, eq2A)
        braces = Brace(eq_group, LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces), Write(eq_text))

class Formula(Scene): 
    def construct(self):
        sympy.init_printing(use_latex=True)
        x = sympy.symbols('x')
        equation = sympy.Eq(sympy.Integral(sympy.exp(x) * sympy.cos(x), x), sympy.exp(x) * sympy.sin(x) / 2 + sympy.exp(x) * sympy.cos(x) / 2)
        formula = TexMobject(r"\displaystyle \left[\begin{matrix}2 x & 2 y & 0\\0 & 1 & -1\end{matrix}\right]")
        formula.set_color(BLUE)
        formula.scale(2)
        self.play(Write(formula))


        formula2 = TextMobject(r"equation: $\displaystyle \left[\begin{matrix}2 x & 2 y & 0\\0 & 1 & -1\end{matrix}\right]$")
        formula2.set_color(BLUE)
        self.play(Write(formula2))

        self.clear()

        #formula3 = TextMobject(r"equation: $\int e ^ {x} \cos {\left(x \right)}\, dx = \frac {e ^ {x} \sin {\left(x \right)}}{2} + \frac {e ^ {x} \cos   {\left(x \right)}}{2}$")
        formula3 = TextMobject(r"equation: $"+str(sympy.latex(equation))+"$")

        formula3.set_color(BLUE)
        self.play(Write(formula3))
        self.wait(3)

class ColoringEquations(Scene):
#Grouping and coloring parts of equations
    def construct(self):
        line1=TexMobject("\\text{The vector }", "\\vec{F}_{net}", "\\text{ is the net force on object of mass }")
        line1.set_color_by_tex("force", BLUE)
        line2=TexMobject("m", "\\text{ and acceleration }", "\\vec{a}", ". ")
        line2.set_color_by_tex_to_color_map({
        "m": YELLOW,
        "{a}": RED
        })
        sentence=VGroup(line1,line2)
        # SMALL_BUFF = 0.1
        # MED_SMALL_BUFF = 0.25
        # MED_LARGE_BUFF = 0.5
        # LARGE_BUFF = 1
        sentence.arrange_submobjects(DOWN, buff=LARGE_BUFF)
        self.play(Write(sentence))

class PlotFunctions(GraphScene):
    # CONFIG = {
    #     "x_min": -10,
    #     "x_max": 10,
    #     "y_min": -1.5,
    #     "y_max": 1.5,
    #     "graph_origin": ORIGIN,
    #     "function_color": RED,
    #     "axes_color": GREEN,
    #     "x_labeled_nums": range(-10, 12, 2),
    # }

    CONFIG = {
        "x_min": -1,
        "x_max": 20,
        "x_axis_width": 9,
        "x_tick_frequency": 1,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": range(10, 12, 1),
        "x_axis_label": "$x$",
        "y_min": -1,
        "y_max": 10,
        "y_axis_height": 6,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": None,
        "y_axis_label": "$y$",
        "axes_color": GREY,
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
        "exclude_zero_label": True,
        "num_graph_anchor_points": 25,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,

        "function_color": RED,
    }

    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph, self.function_color)
        func_graph2 = self.get_graph(self.func_to_graph2)
        vert_line = self.get_vertical_line_to_graph(TAU, func_graph, color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label="\\cos(x)")
        graph_lab2 = self.get_graph_label(func_graph2, label="\\sin(x)", x_val=-10, direction=UP / 2)
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU, func_graph)
        two_pi.next_to(label_coord, RIGHT + UP)
        self.play(ShowCreation(func_graph), ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2), ShowCreation(two_pi))
        self.wait(5)


    def func_to_graph(self, x):
        return np.cos(x)

    def func_to_graph2(self, x):
        return np.sin(x)

class ExampleApproximation(GraphScene):
    CONFIG = {
        "function": lambda x: np.cos(x),
        "function_color": BLUE,
        "taylor": [lambda x: 1, lambda x: 1 - x ** 2 / 2,
                   lambda x: 1 - x ** 2 / math.factorial(2) + x ** 4 / math.factorial(4),
                   lambda x: 1 - x ** 2 / 2 + x ** 4 / math.factorial(4) - x ** 6 / math.factorial(6),
                   lambda x: 1 - x ** 2 / math.factorial(2) + x ** 4 / math.factorial(4) - x ** 6 / math.factorial(
                       6) + x ** 8 / math.factorial(8),
                   lambda x: 1 - x ** 2 / math.factorial(2) + x ** 4 / math.factorial(4) - x ** 6 / math.factorial(
                       6) + x ** 8 / math.factorial(8) - x ** 10 / math.factorial(10)],
        "center_point": 0,
        "approximation_color": GREEN,
        "x_min": -10,
        "x_max": 10,
        "y_min": -1,
        "y_max": 1,
        "graph_origin": ORIGIN,
        "x_labeled_nums": range(-10, 12, 2),

    }


    def construct(self):
        self.setup_axes(animate=True)


        func_graph = self.get_graph(self.function, self.function_color, )
        approx_graphs = [ self.get_graph( f, self.approximation_color ) for f in self.taylor ]

        term_num = [ TexMobject("n = " + str(n), aligned_edge=TOP) for n in range(0, 8)]
        [t.to_edge(BOTTOM, buff=SMALL_BUFF) for t in term_num]

        term = TexMobject("")
        term.to_edge(BOTTOM, buff=SMALL_BUFF)

        approx_graph = VectorizedPoint( self.input_to_graph_point(self.center_point, func_graph) )

        self.play( ShowCreation(func_graph), )
        for n, graph in enumerate(approx_graphs):
            self.play( Transform(approx_graph, graph, run_time=2),  Transform(term, term_num[n])  )
        self.wait()

class ParametricCurve2(ThreeDScene):
    def construct(self):
        curve1=ParametricFunction(lambda u : np.array([ 1.2*np.cos(u),  1.2*np.sin(u),  u/2 ]),color=RED,t_min=-TAU,t_max=TAU,)
        curve1.set_shade_in_3d(True)
        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi=80 * DEGREES,theta=-60*DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.play(ShowCreation(curve1))
        self.wait()

class SurfacesAnimation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cylinder = ParametricSurface(
            lambda u, v: np.array([
                np.cos(TAU * v),
                np.sin(TAU * v),
                2 * (1 - u)
            ]),
            resolution=(6, 32)).fade(0.5) #Resolution of the surfaces

        paraboloid = ParametricSurface(
            lambda u, v: np.array([
                np.cos(v)*u,
                np.sin(v)*u,
                u**2
            ]),v_max=TAU,
            checkerboard_colors=[PURPLE_D, PURPLE_E],
            resolution=(10, 32)).scale(2)

        para_hyp = ParametricSurface(
            lambda u, v: np.array([
                u,
                v,
                u**2-v**2
            ]),v_min=-2,v_max=2,u_min=-2,u_max=2,checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(15, 32)).scale(1)

        cone = ParametricSurface(
            lambda u, v: np.array([
                u*np.cos(v),
                u*np.sin(v),
                u
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[GREEN_D, GREEN_E],
            resolution=(15, 32)).scale(1)

        hip_one_side = ParametricSurface(
            lambda u, v: np.array([
                np.cosh(u)*np.cos(v),
                np.cosh(u)*np.sin(v),
                np.sinh(u)
            ]),v_min=0,v_max=TAU,u_min=-2,u_max=2,checkerboard_colors=[YELLOW_D, YELLOW_E],
            resolution=(15, 32))

        ellipsoid=ParametricSurface(
            lambda u, v: np.array([
                1*np.cos(u)*np.cos(v),
                2*np.cos(u)*np.sin(v),
                0.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[TEAL_D, TEAL_E],
            resolution=(15, 32)).scale(2)

        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]),v_min=0,v_max=TAU,u_min=-PI/2,u_max=PI/2,checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).scale(2)


        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)


        self.add(axes)
        self.play(Write(sphere))
        self.wait()
        self.play(ReplacementTransform(sphere,ellipsoid))
        self.wait()
        self.play(ReplacementTransform(ellipsoid,cone))
        self.wait()
        self.play(ReplacementTransform(cone,hip_one_side))
        self.wait()
        self.play(ReplacementTransform(hip_one_side,para_hyp))
        self.wait()
        self.play(ReplacementTransform(para_hyp,paraboloid))
        self.wait()
        self.play(ReplacementTransform(paraboloid,cylinder))
        self.wait()
        self.play(FadeOut(cylinder))

class ExampleThreeD(ThreeDScene):
    CONFIG = {
        "plane_kwargs": {
            "color": RED_B
        },
        "point_charge_loc": 0.5 * RIGHT - 1.5 * UP,
    }


    def construct(self):
        #self.set_camera_position(0, -np.pi / 2)
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field2D = VGroup(*[self.calc_field2D(x * RIGHT + y * UP)
                           for x in np.arange(-9, 9, 1)
                           for y in np.arange(-5, 5, 1)
                           ])

        self.play(ShowCreation(field2D))
        self.wait()
        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.begin_ambient_camera_rotation()
        self.wait(6)


    def calc_field2D(self, point):
        x, y = point[:2]
        Rx, Ry = self.point_charge_loc[:2]
        r = math.sqrt((x - Rx) ** 2 + (y - Ry) ** 2)
        efield = (point - self.point_charge_loc) / r ** 3
        return Vector(efield).shift(point)

#https://talkingphysics.wordpress.com/2018/07/03/3d-scenes-manim-series-part-10/
class EFieldInThreeD(ThreeDScene):
    CONFIG = {
        "plane_kwargs": {
            "color": RED_B
        },
        "point_charge_loc": 0.5 * RIGHT - 1.5 * UP,
    }


    def construct(self):
        #self.set_camera_position(0.1, -np.pi / 2)
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field2D = VGroup(*[self.calc_field2D(x * RIGHT + y * UP)
                           for x in np.arange(-9, 9, 1)
                           for y in np.arange(-5, 5, 1)
                           ])

        field3D = VGroup(*[self.calc_field3D(x * RIGHT + y * UP + z * OUT)
                           for x in np.arange(-9, 9, 1)
                           for y in np.arange(-5, 5, 1)
                           for z in np.arange(-5, 5, 1)])

        self.play(ShowCreation(field3D))
        self.wait()
        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)
        self.begin_ambient_camera_rotation()
        self.wait(6)


    def calc_field2D(self, point):
        x, y = point[:2]


        Rx, Ry = self.point_charge_loc[:2]
        r = math.sqrt((x - Rx) ** 2 + (y - Ry) ** 2)
        efield = (point - self.point_charge_loc) / r ** 3
        return Vector(efield).shift(point)


    def calc_field3D(self, point):
        x, y, z = point


        Rx, Ry, Rz = self.point_charge_loc
        r = math.sqrt((x - Rx) ** 2 + (y - Ry) ** 2 + (z - Rz) ** 2)
        efield = (point - self.point_charge_loc) / r ** 3
        return Vector(efield).shift(point)


class SVGStickMan(Scene):
    def construct(self):
        start_man = StickMan()
        plain_man = StickMan()
        waving_man = StickMan("wave")
        self.add(start_man)
        self.wait()
        self.play(Transform(start_man, waving_man))
        self.play(Transform(start_man, plain_man))

SVG_IMAGE_DIR="/home/behnam/anaconda3/envs/manim/src/examples/svg_files/"

HEAD_INDEX   = 0
BODY_INDEX   = 1
ARMS_INDEX   = 2
LEGS_INDEX   = 3

class StickMan(SVGMobject):
    CONFIG = {
        "color": BLUE_E,
        "stroke_width": 2,
        "stroke_color": WHITE,
        "fill_opacity": 1.0,
        "propagate_style_to_family": True,
        "height": 3,
        "corner_scale_factor": 0.75,
        "flip_at_start": False,
        "is_looking_direction_purposeful": False,
        "start_corner": None,
        # Range of proportions along body where arms are
        "right_arm_range": [0.55, 0.7],
        "left_arm_range": [.34, .462],
    }


    def __init__(self, mode="plain", **kwargs):
        self.parts_named = False
        try:
            svg_file = os.path.join(SVG_IMAGE_DIR, "stick_man_%s.svg" % mode  )
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        except:
            warnings.warn("No StickMan design with mode %s" % mode)
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "stick_man.svg"
            )
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)

        if self.flip_at_start:
            self.flip()
        if self.start_corner is not None:
            self.to_corner(self.start_corner)


    def name_parts(self):
        # self.mouth = self.submobjects[MOUTH_INDEX]
        self.head = self.submobjects[HEAD_INDEX]
        self.body = self.submobjects[BODY_INDEX]
        self.arms = self.submobjects[ARMS_INDEX]
        self.legs = self.submobjects[LEGS_INDEX]
        self.parts_named = True

    def init_colors(self):
        SVGMobject.init_colors(self)

        if not self.parts_named:
            self.name_parts()

        self.head.set_fill(RED, opacity=0)
        self.body.set_fill(self.color, opacity=1)
        self.arms.set_fill(YELLOW, opacity=0)
        self.legs.set_fill(GREEN, opacity=0)
        return self