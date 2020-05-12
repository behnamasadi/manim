from manimlib.imports import *

SVG_IMAGE_DIR="/home/behnam/anaconda3/envs/manim/src/youtube/ransac/raster_images/"
RASTER_IMAGE_DIR="/home/behnam/anaconda3/envs/manim/src/youtube/ransac/raster_images/"

class RANSACSIntro(Scene):
   def construct(self):
        ransac_title=TextMobject("RANSAC")
        ransac_title.scale(2)
        ransac_title.to_edge(UL)
        self.play(Write(ransac_title))
        self.wait(3)

        #,text-alignment='left'
        ransac_describtion=TextMobject("RANSAC is an iterative algorithm for fitting a parametric model into data containing outliers.")
        ransac_describtion.scale(.8)
        ransac_describtion.shift(ransac_title.get_corner(DOWN),DOWN)
        ransac_describtion.to_edge(LEFT)
        self.play(Write(ransac_describtion))
        self.wait(3)


        ransac_examples=TextMobject("Examples: fitting a line, plane, cylinder into scanned data, findig an affine transformation, homographpy")
        ransac_examples.scale(.8)
        ransac_examples.shift(ransac_describtion.get_corner(DOWN)+0.5*DOWN)
        ransac_examples.to_edge(LEFT)
        self.play(Write(ransac_examples))
        self.wait(3)



        file_path = os.path.join(RASTER_IMAGE_DIR, "Line_with_outliers.svg.png" )
        image = ImageMobject(file_path)
        image.scale(2)  # Resize to be twice as big
        image.shift(ransac_examples.get_corner(DOWN), 2.5*DOWN)
        image.to_edge(LEFT)
        #self.play(ShowCreation(image))  # Display the image
        self.play(FadeIn(image))
        self.wait(2)


        file_path = os.path.join(RASTER_IMAGE_DIR, "Fitted_line_inc.svg.png" )
        image = ImageMobject(file_path)
        image.scale(2)  # Resize to be twice as big
        image.shift(ransac_examples.get_corner(DOWN), 2.5*DOWN)
        image.to_edge(RIGHT)
        #self.play(ShowCreation(image))  # Display the image
        self.play(FadeIn(image))
        self.wait(2)

class RANSACSStep(Scene):
    def construct(self):
        step1_title = TextMobject("Step 1")
        step1_title.scale(1.5)
        step1_title.to_edge(UL)
        self.play(Write(step1_title))
        self.wait(2)


        step1=TextMobject("Randomly select minimum number of points for your model.")
        step1.scale(.8)
        step1.shift(step1_title.get_corner(DOWN),DOWN)
        step1.to_edge(LEFT)
        self.play(Write(step1))
        self.wait(3)

        file_path = os.path.join(RASTER_IMAGE_DIR, "Line_with_outliers_2_points_selected.svg.png" )
        image = ImageMobject(file_path)
        image.scale(2)  # Resize to be twice as big
        image.shift(step1.get_corner(DOWN), 2.5*DOWN)
        image.to_edge(LEFT)
        #self.play(ShowCreation(image))  # Display the image
        self.play(FadeIn(image))
        self.wait(2)

        step2_title=TextMobject("Step 2")
        step2_title.scale(1.5)
        step2_title.to_edge(UL)
        self.play(Transform(step1_title,step2_title))
        self.wait(2)

        step2 = TextMobject("Hypothesize a model, y=mx+b")
        step2.scale(.8)
        step2.shift(step2_title.get_corner(DOWN), DOWN)
        step2.to_edge(LEFT)
        self.play(Transform(step1, step2))
        self.wait(3)

        file_path = os.path.join(RASTER_IMAGE_DIR, "Line_with_outliers_fitted_line.svg.png")
        image2 = ImageMobject(file_path)
        image2.scale(2)  # Resize to be twice as big
        image2.shift(step1.get_corner(DOWN), 2.5 * DOWN)
        image2.to_edge(RIGHT)
        self.play(FadeIn(image2))
        self.wait(2)

        step3_title = TextMobject("Step 3")
        step3_title.scale(1.5)
        step3_title.to_edge(UL)
        self.play(Transform(step1_title, step3_title))
        self.wait(2)

#Distance threshold t
#• Choose t so probability for inlier is p (e.g. 0.95)
#• Zero-mean Gaussian noise with std. dev. σ: t2=3.84σ2


        step3 = TextMobject("Compute error function, finding the set of inliers from the dataset based on given threshold")
        step3.scale(.8)
        step3.shift(step3_title.get_corner(DOWN), DOWN)
        step3.to_edge(LEFT)
        self.play(Transform(step1,step3))
        self.wait(3)

        self.play(FadeOut(image))
        self.play(FadeOut(image2))

        file_path = os.path.join(RASTER_IMAGE_DIR, "Fitted_line.svg.png")
        image3 = ImageMobject(file_path)
        image3.scale(2)  # Resize to be twice as big
        image3.shift(step1.get_corner(DOWN), 2.5 * DOWN)
        self.play(FadeIn(image3))
        self.wait(2)


        step4_title = TextMobject("Step 4")
        step4_title.scale(1.5)
        step4_title.to_edge(UL)
        self.play(Transform(step1_title, step4_title))
        self.wait(2)

        step4 = TextMobject("If the number of inliers is more than the best previous model, set the new model as best model and repeat from step 1")
        step4.scale(.8)
        step4.shift(step4_title.get_corner(DOWN), DOWN)
        step4.to_edge(LEFT)
        self.play(Transform(step1,step4))
        self.wait(3)


class RANSACParameterExplanation(Scene):
    def construct(self):
        Explanation_of_Parameters=TextMobject("Explanation of Parameters")
        N_formula=TexMobject(r"N=\frac{\log(1-p)}{\log(1-(1-e)^s)}")
        self.play(Write(N_formula))
        self.wait(3)
        self.play(ApplyMethod( N_formula.to_edge,UP))
        self.wait(3)

        s = TextMobject("s: Minimum number of needed to fit the model line fitting 2, fitting a plane is 3, findig an affine transformation 3, homographpy 4")
        s.scale(0.8)
        s.shift(N_formula.get_corner(DOWN),DOWN)
        s.to_edge(LEFT)
        self.play(Write(s))
        self.wait(3)

        e = TextMobject("e: Probability that a point is an outlier")
        e.scale(0.8)
        e.shift(s.get_corner(DOWN),DOWN)
        e.to_edge(LEFT)
        self.play(Write(e))
        self.wait(3)





        p = TextMobject("p: Desired probability that we get a good sample")
        p.scale(0.8)
        p.shift(e.get_corner(DOWN), DOWN)
        p.to_edge(LEFT)
        self.play(Write(p))
        self.wait(3)


        N = TextMobject("N: Number of samples such that with probability p, at least one random sample is free from outliers (e.g. p=0.99) (outlier ratio: e) ")
        N.scale(0.8)
        N.shift(p.get_corner(DOWN), DOWN)
        N.to_edge(LEFT)
        self.play(Write(N))
        self.wait(3)

        #e is Probability that a point is an outlier, therefore 1-e that a point is inlier
        self.clear()
        N_formula1=TexMobject(r"e")
        self.play(Write(N_formula1))
        self.wait(3)

        N_formula2 = TexMobject(r"1-e")
        self.play(Transform(N_formula1,  N_formula2 ))
        self.wait(3)

        #since we our model need s point and our data points are indipendnt of each other so the joint probability would be multipication of them
        #so the follwoing is the probability of choosing s points and all of them are inliers
        N_formula3 = TexMobject(r"(1-e)^s")
        self.play(Transform(N_formula1, N_formula3))
        self.wait(3)

        #the complmenet, selecting s points and not all of them are inlier, meaning at least 1 or more outlier
        N_formula4 = TexMobject(r"1-(1-e)^s")
        self.play(Transform(N_formula1, N_formula4))
        self.wait(3)

        #since we are selecting N samples adn they are indipent of each other, P(A,B)=P(A)P(B)
        # choosing N samples and they have outliers
        N_formula5 = TexMobject(r"(1-(1-e)^s)^N")
        self.play(Transform(N_formula1, N_formula5))
        self.wait(3)

        #the complmenet would be choosing N samples and not all of them are contaminated with outliers meaning there is at least 1 inlier in our data
        N_formula6 = TexMobject(r"1-(1-(1-e)^s)^N")
        self.play(Transform(N_formula1, N_formula6))
        self.wait(3)

        #this is the p that we are looking for, probability that at least 1 sample is inliers
        N_formula7 = TexMobject(r"p=1-(1-(1-e)^s)^N")
        self.play(Transform(N_formula1, N_formula7))
        self.wait(3)

        #by taking logarithm from both side we would get the following, which gives us how many sample we should have such that with probabilit of p there is at least 1 inlier
        N_formula8 = TexMobject(r"N=\frac{\log(1-p)}{\log(1-(1-e)^s)}")
        self.play(Transform(N_formula1, N_formula8))
        self.wait(3)


        self.clear()

        # Choose N such that with probability p = 0.99 at least one random sample is free from outliers
        set_p = TextMobject("Set p=0.99, chance of getting good sample:")
        #N.scale(0.8)
        set_p.to_edge(LEFT)

        self.play(FadeIn(set_p))
        self.play(ApplyMethod( set_p.to_edge,UP))
        #

        s_2_e_5_n_2 = TexMobject(r"\text{s=2, e=5\%, N=2}")
        s_2_e_5_n_2.shift(set_p.get_corner(DOWN), DOWN)
        s_2_e_5_n_2.to_edge(LEFT)
        self.play(Write(s_2_e_5_n_2))
        self.wait(1)

        s_2_e_50_n_17 = TexMobject(r"\text{s=2, e=50\%, N=17}")
        s_2_e_50_n_17.shift(s_2_e_5_n_2.get_corner(DOWN), DOWN)
        s_2_e_50_n_17.to_edge(LEFT)
        self.play(Write(s_2_e_50_n_17))
        self.wait(1)

        s_4_e_5_n_3 = TexMobject(r"\text{s=4, e=5\%, N=3}")
        s_4_e_5_n_3.shift(s_2_e_50_n_17.get_corner(DOWN), DOWN)
        s_4_e_5_n_3.to_edge(LEFT)
        self.play(Write(s_4_e_5_n_3))
        self.wait(1)

        s_4_e_50_n_72 = TexMobject(r"\text{s=4, e=50\%, N=72}")
        s_4_e_50_n_72.shift(s_4_e_5_n_3.get_corner(DOWN), DOWN)
        s_4_e_50_n_72.to_edge(LEFT)
        self.play(Write(s_4_e_50_n_72))
        self.wait(1)

        # https://cs.gmu.edu/~kosecka/cs682/lect-fitting.pdf
        # https://www.cc.gatech.edu/~afb/classes/CS4495-Fall2014/slides/CS4495-Ransac.pdf
        # https://salzis.wordpress.com/2014/06/10/robust-linear-model-estimation-using-ransac-python-implementation/
        # https://github.com/falcondai/py-ransac
        # https://gist.github.com/ryanpeach/9cf207f1caeb0475e9e0ae09152a4b3d



# class ImageTest(Scene):
#     def construct(self):
#         image = ImageMobject("/home/behnam/anaconda3/envs/manim/src/youtube/ransac/raster_images/Fitted_line_inc.svg.png")
#         image.scale(2)  # Resize to be twice as big
#         image.shift(2 * UP)  # Move the image
#
#         self.play(ShowCreation(image))  # Display the image
#
#         self.play(FadeIn(image))
#         self.wait()
#


