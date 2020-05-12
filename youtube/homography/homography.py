from manimlib.imports import *

SVG_IMAGE_DIR="/home/behnam/anaconda3/envs/manim/src/youtube/homography/svg_images/"
RASTER_IMAGE_DIR="/home/behnam/anaconda3/envs/manim/src/youtube/homography/raster_images/"


class SVGTest(Scene):
    def construct(self):
        file_path = os.path.join(RASTER_IMAGE_DIR, "2cam.png" )
        image = ImageMobject(file_path)
        image.scale(2)
        self.play(FadeIn(image))
        self.wait(5)

#https://tex.stackexchange.com/questions/74353/what-commands-are-there-for-horizontal-spacing
class HomographyFormula(Scene):
    def construct(self):
        homo1=TexMobject(r"""
                      \left(
                        \begin{array}{ccccccccc}
                        -x1 \qquad -y1 \qquad -1 \qquad 0 \qquad 0 \qquad 0 \qquad x1*xp1 \qquad y1*xp1 \qquad xp1\\
                        0 \qquad 0 \qquad 0 \qquad -x1 \qquad -y1 \qquad -1 \qquad x1*yp1 \qquad y1*yp1 \qquad  yp1\\
                        -x2 \qquad -y2 \qquad -1 \qquad 0 \qquad 0 \qquad 0 \qquad x2*xp2 \qquad y2*xp2 \qquad xp2\\
                        0 \qquad 0 \qquad 0 \qquad -x2 \qquad -y2 \qquad -1 \qquad x2*yp2 \qquad y2*yp2 \qquad yp2\\
                        -x3 \qquad -y3 \qquad -1 \qquad 0 \qquad 0 \qquad 0 \qquad x3*xp3 \qquad y3*xp3 \qquad xp3\\
                        0 \qquad 0 \qquad 0 \qquad -x3 \qquad -y3 \qquad -1 \qquad x3*yp3 \qquad y3*yp3 \qquad yp3\\
                        -x4 \qquad -y4 \qquad -1 \qquad 0 \qquad 0 \qquad 0 \qquad x4*xp4 \qquad y4*xp4 \qquad xp4\\
                        0 \qquad 0 \qquad 0 \qquad -x4 \qquad -y4 \qquad -1 \qquad x4*yp4 \qquad y4*yp4 \qquad yp4\\
                        \end{array}
                        \right) *H=0 """,alignment="\centering")
        homo1.scale(0.6)
        self.play(Write(homo1))
        self.wait(3)
        self.clear()

        homo2=TexMobject(r" H^{*} \underset{H}{\mathrm{argmin}}= \left |\left | AH  \right | \right | ^{2}  \text{subject to }   \left |\left | H  \right |\right|=1 ")
        self.play(Write(homo2))
        self.wait(3)
        self.clear()


        homo3=TexMobject(r"\left(A_{M{\times}N} \right)")
        self.play(Write(homo3))
        self.wait(3)
        self.clear()

        homo4=TexMobject(r"""\underbrace{\mathbf{A}}_{M \times N} = \underbrace{\mathbf{U}}_{M \times M} \times \underbrace{\mathbf{\Sigma}}_{M\times N} \times \underbrace{\mathbf{V}^{\text{T}}}_{N \times N}""")
        self.play(Write(homo4))
        self.wait(3)
        self.clear()



        homo4_1 =TextMobject("U is a M $\\times$ M  matrix with orthogonal $\\break$  matrix columns are eigen vectors of A.")

        self.play(Write(homo4_1))
        self.wait(3)
        self.clear()


        homo4_2 = TextMobject("""$\\Sigma$  is a M $\\times$ N matrix with  non - negative entries, $\\break$ 
                               termed the singular   values $\\break$ (diagonal entries are eigen values of A).""")
        #homo4_2.scale(0.5)
        self.play(Write(homo4_2))
        self.wait(3)
        self.clear()



        homo4_3 = TexMobject(r"""\text{V  is an  N}{\times } \text{N  orthogonal matrix.""")
        self.play(Write(homo4_3))
        self.wait(3)
        self.clear()



        homo5 = TextMobject(r""" $H^{*}$  is the last column of V """)


        self.play(Write(homo5))
        self.wait(3)
        self.clear()

