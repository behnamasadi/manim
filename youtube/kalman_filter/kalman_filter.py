from manimlib.imports import *
from sympy import *
from sympy.stats import Probability, Normal
from sympy import Integral

class BayesBelif(Scene):
    def construct(self):
        #Bel(X_t) = \eta * P(Z_t | X_t) \times \int    P(X_t | U_{t - 1}, X_{t - 1}) \times Bel(X_{t - 1})) dX_t
        bayes_equation = TexMobject(r"Bel(X_t)=",r" \eta \times P(Z_t | X_t)",r" \times \int  P(X_t | U_{t - 1}, X_{t - 1}) \times  Bel(X_{t - 1})) dX_t")
        bayes_equation.scale(1)
        brace_top = Brace(bayes_equation[1], UP, buff=SMALL_BUFF)
        brace_bottom = Brace(bayes_equation[2], DOWN, buff=SMALL_BUFF)
        text_top = brace_top.get_text("$Update$")
        text_bottom = brace_bottom.get_text("$Prediction (Estimation)$")
        self.play(
            GrowFromCenter(brace_top),
            GrowFromCenter(brace_bottom),
            FadeIn(text_top),
            FadeIn(text_bottom)
        )
        self.play(Write(bayes_equation))

        # Cov(X)=\Sigma
        # Cov(AX)=A \Sigma A^\mathsf{T}
        self.wait(3)
        self.clear()
        cov_equation_tex = TexMobject(r"Cov(X)=\Sigma")
        self.play(Write(cov_equation_tex))

        self.wait(3)
        self.clear()
        cov_equation_tex = TexMobject(r"Cov(AX)=A \Sigma A^\mathsf{T}")
        self.clear()
        self.play(Write(cov_equation_tex))

def Range(in_val,end_val,step=1):
    return list(np.arange(in_val,end_val+step,step))

class NormalsDistributionsPlot(GraphScene):
    CONFIG = {
        "y_max" : 1.5,
        "y_min" : -1.5,
        "x_max" : 4*PI/2,
        "x_min" : -4*PI/2,
        "y_tick_frequency" : 0.5,
        "x_tick_frequency" : PI/2,
        "graph_origin" : ORIGIN,
        "y_axis_label": None, # Don't write y axis label
        "x_axis_label": None,
    }
    def construct(self):
        self.setup_axes()

        sigma1=0.5
        mu1=1

        #sigma2=0.2
        #mu2=2


        k=1.5
        sigma2=(k**2)*sigma1
        mu2=k*mu1


        normal1 = self.get_graph(lambda x : np.exp( -((x-mu1)**2)/(2*sigma1**2))* (1/(np.sqrt(2*PI*sigma1**2))) ,
                                    color = WHITE,
                                    x_min=-1,
                                    x_max=4,
                                )
        normal2 = self.get_graph(lambda x : np.exp( -((x-mu2)**2)/(2*sigma2**2))* (1/(np.sqrt(2*PI*sigma2**2))),
                                    color = BLUE,
                                    x_min=-1,
                                    x_max=4,
                                )
        normal1.set_stroke(width=3) # width of line
        normal2.set_stroke(width=3)
        # Animation
        for plot in (normal1,normal2):
            self.play(
                    ShowCreation(plot),
                    run_time = 2
                )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        # width of edges
        self.x_axis.set_stroke(width=2)
        self.y_axis.set_stroke(width=2)
        # color of edges
        self.x_axis.set_color(RED)
        self.y_axis.set_color(YELLOW)
        # Add x,y labels
        func = TexMobject(r"y")
        var = TexMobject(r"x")
        func.set_color(YELLOW)
        var.set_color(RED)
        func.next_to(self.y_axis,UP)
        var.next_to(self.x_axis,RIGHT+UP)
        # Y labels
        self.y_axis.label_direction = LEFT*1.5
        self.y_axis.add_numbers(*[-1,1])
        #Parametters of x labels
        init_val_x = -3*PI/2
        step_x = PI/2
        end_val_x = 3*PI/2
        # List of the positions of x labels
        values_decimal_x=Range(init_val_x,end_val_x,step_x)
        # List of tex objects
        list_x=TexMobject("-\\frac{3\\pi}{2}", #   -3pi/2
                            "-\\pi", #              -pi
                            "-\\frac{\\pi}{2}", #   -pi/2
                            "\\,", #                 0 (space)
                            "\\frac{\\pi}{2}", #     pi/2
                            "\\pi",#                 pi
                            "\\frac{3\\pi}{2}" #     3pi/2
                          )
        #List touples (position,label)
        values_x = [(i,j)
            for i,j in zip(values_decimal_x,list_x)
                    ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            x_tex.scale(0.7)
            if x_val == -PI or x_val == PI: #if x is equals -pi or pi
                x_tex.next_to(self.coords_to_point(x_val, 0), 2*DOWN) #Put 2*Down
            else: # In another case
                x_tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(x_tex)

        self.play(
            *[Write(objeto)
            for objeto in [
                    self.y_axis,
                    self.x_axis,
                    #self.x_axis_labels,
                    func,var
                ]
            ],
            run_time=2
        )

class NomalMultipiction(Scene):
    def construct(self):

        normal_fromula = TexMobject(r"X \sim \mathcal{N}(\mu\prime,\,\sigma^{\prime2})\ ")

        self.play(Write(normal_fromula))
        self.wait(2)
        self.play(ApplyMethod(normal_fromula.to_edge,UP))

        nomal_multipiction = TexMobject(r"X \sim \mathcal{N}(\mu_0,\,\sigma_{0}^{2})\ * X \sim \mathcal{N}(\mu_1,\,\sigma_{1}^{2})\ ")
        self.play(Write(nomal_multipiction))
        self.wait(2)
        self.play(ApplyMethod(nomal_multipiction.shift, TOP+ 2*DOWN) )

        sigma_prime=TexMobject(r"\sigma^{\prime2}=\sigma_{0}^{2}-\frac{\sigma_{0}^{4}}{  \sigma_{0}^{2} +\sigma_{1}^{2}   } ")
        self.play(Write(sigma_prime))
        self.wait(2)

        mu_prime=TexMobject(r"\mu\prime=\mu_{0} +\frac{\sigma_{0}^{2}  (\mu_{1}-\mu_{0}))}{  \sigma_{0}^{2} +\sigma_{1}^{2}    }     ")
        mu_prime.next_to(sigma_prime, DOWN)
        self.play(Write(mu_prime))
        self.wait(2)

class NomalMultipictionRewritten(Scene):
    def construct(self):
        k=TexMobject(r" K=\frac{\sigma_{0}^{2}}{  \sigma_{0}^{2} +\sigma_{1}^{2}   }")
        self.play(Write(k))
        self.wait(2)

        self.play(ApplyMethod(k.to_edge,UP) )
        self.wait(2)

        sigma_prime = TexMobject(r" \sigma^{\prime2}=\sigma_{0}^{2}-K\sigma_{0}^{2}")
        self.play(Write(sigma_prime))
        self.wait(2)
        self.play(ApplyMethod(sigma_prime.shift, TOP+ 2.2*DOWN) )



        mu_prime = TexMobject(r" \mu ^ {\prime}=\mu_{0}  - K(\mu_1 -\mu_0)")
        self.play(Write(mu_prime))
        self.wait(2)

        self.play(ApplyMethod(mu_prime.shift, TOP+ 3*DOWN) )
        self.wait(2)

        sigma_0_lim_inf=TexMobject(r"\lim_{\sigma_{0} \to +\infty}  K=\frac{\sigma_{0}^{2}}{  \sigma_{0}^{2} +\sigma_{1}^{2}   }")
        self.play(Write(sigma_0_lim_inf))
        self.wait(2)

        sigma_0_lim_0 = TexMobject( r" \lim_{\sigma_{0} \to 0}  K=\frac{\sigma_{0}^{2}}{  \sigma_{0}^{2} +\sigma_{1}^{2}   } ")
        sigma_0_lim_0.shift(ORIGIN +  1.2*DOWN)
        self.play(Write(sigma_0_lim_0))
        self.wait(2)

        sigma_0_lim_0_k_becomes_inf=TexMobject(r"K=1")
        self.play(Transform(sigma_0_lim_inf, sigma_0_lim_0_k_becomes_inf) )
        self.wait(2)

        sigma_prime_becomes_1 = TexMobject(r" \sigma^{\prime2}=0")
        sigma_prime_becomes_1.shift(sigma_0_lim_0_k_becomes_inf.get_corner(RIGHT),1.5*RIGHT)
        self.play(Write(sigma_prime_becomes_1))

        mu_prime_becomes_mu_1=TexMobject(r"\mu ^ {\prime}=\mu1")
        mu_prime_becomes_mu_1.shift(sigma_prime_becomes_1.get_corner(RIGHT), 1.5*RIGHT)
        self.play(Write(mu_prime_becomes_mu_1))



        sigma_0_lim_0_k_becomes_0=TexMobject(r"K=0")
        sigma_0_lim_0_k_becomes_0.shift(ORIGIN + 1.2 * DOWN)
        self.play(Transform(sigma_0_lim_0, sigma_0_lim_0_k_becomes_0) )
        self.wait(2)

        sigma_prime_becomes_sigma_o = TexMobject(r" \sigma^{\prime2}=\sigma_{0}^{2}")
        sigma_prime_becomes_sigma_o.shift(sigma_0_lim_0_k_becomes_0.get_corner(RIGHT), 1.5*RIGHT)
        self.play(Write(sigma_prime_becomes_sigma_o))

        mu_prime_becomes_mu_0 = TexMobject(r"\mu ^ {\prime}=\mu0")
        mu_prime_becomes_mu_0.shift(sigma_prime_becomes_sigma_o.get_corner(RIGHT), 1.5*RIGHT)
        self.play(Write(mu_prime_becomes_mu_0))
        self.wait(2)

class NomalMultipictionMultiDimension(Scene):
    def construct(self):

        k=TexMobject(r"K=\Sigma_{0}(\Sigma_{0} +\Sigma_{0} )^{-1}")
        self.play(Write(k))
        self.wait(2)
        self.play(ApplyMethod(k.shift, TOP + 1 * DOWN))



        mu=TexMobject(r"\mu\vec{}= \mu\vec{}_{0}+K(\mu\vec{}_{1} - \mu\vec{}_{0}  )")
        self.play(Write(mu))
        self.wait(2)
        self.play(ApplyMethod(mu.shift, TOP + 2 * DOWN))


        sigma=TexMobject(r"\Sigma{}'=\Sigma_{0}-K\Sigma_{0}")
        self.play(Write(sigma))
        self.wait(2)
        self.play(ApplyMethod(sigma.shift, TOP + 3 * DOWN))
        self.wait(2)

class KinematicExample(Scene):
    def construct(self):
        position_and_velocity_title = TexMobject(r"\text{Position And Velocity}")
        position_and_velocity_title.to_edge(UL )#= UP + LEFT
        self.play(Write(position_and_velocity_title))

        position=TexMobject(r"p=p_{0}+\frac{1}{2}*  at^2+v_{0}t")
        position.shift(position_and_velocity_title.get_corner(DOWN)+DOWN )
        position.to_edge(LEFT_SIDE)
        self.play(Write(position))


        velocity=TexMobject(r" v=at+v_{0}")
        velocity.shift(position_and_velocity_title.get_corner(DOWN) + 2*DOWN )
        velocity.to_edge(LEFT_SIDE  )
        self.play(Write(velocity))
        self.wait(2)



        state_space = TexMobject(r"\text{State Space}")
        state_space.to_edge(LEFT )#= UP + LEFT
        self.play(Write(state_space))
        self.wait(2)


        x_k = TexMobject(r"X_{k}= \begin{bmatrix} P_{k}  \\ V_{k} \end{bmatrix} " )
        x_k.shift(state_space.get_corner(DOWN) + DOWN)
        x_k.to_edge(LEFT_SIDE)
        self.play(Write(x_k))




        p_k = TexMobject(r"P_k=P_{k-1}+V_{k-1} t +\frac{1}{2}at^2 ")
        p_k.shift(position_and_velocity_title.get_corner(DOWN) + DOWN)
        p_k.to_edge(LEFT_SIDE)

        self.play(Transform(position,p_k))

        v_k = TexMobject(r"V_{k}=V_{k-1}+a\times t ")
        v_k.shift(position_and_velocity_title.get_corner(DOWN) + 2*DOWN )
        v_k.to_edge(LEFT_SIDE  )
        self.play(Transform(velocity, v_k))

class KinematicPredictionMatrixForm(Scene):
    def construct(self):
        position_and_velocity_title = TexMobject(r"\text{Matrix Representation Of Position And Velocity}")
        position_and_velocity_title.to_edge(UL )#= UP + LEFT
        self.play(Write(position_and_velocity_title))
        x_k_hat = TexMobject( r"\hat{X}_{k}=\begin{bmatrix} 1 & t\\ 0 & 1 \end{bmatrix}  \hat{X}_{k-1} +\begin{bmatrix} t^2\\ t \end{bmatrix}a")
        x_k_hat.shift(position_and_velocity_title.get_corner(DOWN)+DOWN )
        x_k_hat.to_edge(LEFT_SIDE)
        self.play(Write(x_k_hat))


        x_k_hat_matrix_form = TexMobject(r"\hat{X}_{k}=" , r"F",r"\hat{X}_{k-1}+",r"B",r"\vec{U}")
        x_k_hat_matrix_form.shift(position_and_velocity_title.get_corner(DOWN)+3*DOWN )
        x_k_hat_matrix_form.to_edge(LEFT_SIDE)

        self.play(Write(x_k_hat_matrix_form))
        self.wait(3)

        brace_text_scale=0.60

        x_k_hat_brace_bottom = Brace(x_k_hat_matrix_form[0], DOWN, buff=MED_SMALL_BUFF)
        x_k_hat_brace_bottom_text = x_k_hat_brace_bottom.get_text(r"$State Prior$")
        x_k_hat_brace_bottom_text.scale_in_place(brace_text_scale)

        self.play(GrowFromCenter(x_k_hat_brace_bottom))
        self.play(FadeIn(x_k_hat_brace_bottom_text))



        f = Brace(x_k_hat_matrix_form[1], TOP, buff=MED_SMALL_BUFF)
        f_top_text = f.get_text(r"$\text{Prediction Matrix}$")
        f_top_text.scale_in_place(brace_text_scale)

        self.play(GrowFromCenter(f))
        self.play(FadeIn(f_top_text))



        b = Brace(x_k_hat_matrix_form[3], DOWN, buff=MED_SMALL_BUFF)
        b_bottom_text = b.get_text(r"$\text{Control Matrix$}")
        b_bottom_text.scale_in_place(brace_text_scale)

        self.play(GrowFromCenter(b))
        self.play(FadeIn(b_bottom_text))


        u = Brace(x_k_hat_matrix_form[4], TOP, buff=MED_SMALL_BUFF)
        u_top_text = u.get_text(r"$\text{Control  Vetor}$")
        u_top_text.scale_in_place(brace_text_scale)

        self.play(GrowFromCenter(u))
        self.play(FadeIn(u_top_text))



        p_k_matrix_form = TexMobject(r"P_k","=F_k P_{k-1}F^\mathsf{T}_{k}+","Q_{k} ")
        p_k_matrix_form.shift(position_and_velocity_title.get_corner(DOWN) + 5 * DOWN)

        p_k_matrix_form.to_edge(LEFT_SIDE)
        self.play(Write(p_k_matrix_form))



        p_k = Brace(p_k_matrix_form[0], BOTTOM, buff=MED_SMALL_BUFF)
        p_k_text = p_k.get_text(r"$\text{Prior Error Covariance}$")
        p_k_text.scale_in_place(brace_text_scale)
        self.play(GrowFromCenter(p_k))
        self.play(FadeIn(p_k_text))


        q_k = Brace(p_k_matrix_form[2], BOTTOM, buff=MED_SMALL_BUFF)
        q_k_text = q_k.get_text(r"$\text{Process Noise}$")
        q_k_text.scale_in_place(brace_text_scale)
        self.play(GrowFromCenter(q_k))
        self.play(FadeIn(q_k_text))

        self.wait(3)

class KinematicMeasurmentMatrixForm(Scene):
    def construct(self):

        measurment_title = TexMobject(r"\text{Measurment Update}")
        measurment_title.to_edge(UL )#= UP + LEFT
        self.play(Write(measurment_title))

        #correction=
        mean=TexMobject(r"\mu_{k}=","H_{k}", "\hat{X}_{k}")
        mean.shift(measurment_title.get_corner(DOWN)+DOWN)
        self.play(Write(mean))
        self.wait(2)

        brace_text_scale=0.6

        h_k = Brace(mean[1], BOTTOM, buff=MED_SMALL_BUFF)
        h_k_text = h_k.get_text(r"$\text{Measurment Matrix}$")
        h_k_text.scale_in_place(brace_text_scale)
        self.play(GrowFromCenter(h_k))
        self.play(FadeIn(h_k_text))





        cov = TexMobject(r"\Sigma_{k}=H_{k}P_{k} H^\mathsf{T}_{k} +","R_{k} ")
        cov.shift(mean.get_corner(DOWN)+2*DOWN)
        self.play(Write(cov))
        self.wait(2)



        R_k = Brace(cov[1], BOTTOM, buff=MED_SMALL_BUFF)
        R_k_text = R_k.get_text(r"$\text{Measurment Noise}$")
        R_k_text.scale_in_place(brace_text_scale)
        self.play(GrowFromCenter(R_k))
        self.play(FadeIn(R_k_text))
        self.wait(2)


class Fusion(Scene):
    def construct(self):
        fusion_title = TexMobject(r"\text{Data Fusion}")
        fusion_title.to_edge(UL)  # = UP + LEFT
        self.play(Write(fusion_title))


        k_prime = TexMobject(r"""K^\prime=P_{k}H_{k}^\mathsf{T}(H_{k}P_{k}H_{k}^\mathsf{T}+R_{k} )^{-1}""")
        k_prime.shift(fusion_title.get_corner(DOWN)+DOWN)
        k_prime.to_edge(LEFT_SIDE)
        self.play(Write(k_prime))
        self.wait(2)


        #new mean
        x_k_hat_prime=TexMobject(r"\hat{X}^{'}_{k}=\hat{X}_{k}+K^{'}(Z_k-H_{k}\hat{X}_{k} )")
        x_k_hat_prime.shift(k_prime.get_corner(DOWN)+2*DOWN )
        x_k_hat_prime.to_edge(LEFT_SIDE)
        self.play(Write(x_k_hat_prime))
        self.wait(2)



        # new cov
        p_k_prime=TexMobject(r"P^{'}_k=P_k-K^{'}H_{k}P_{k}")
        p_k_prime.shift(k_prime.get_corner(DOWN)+4*DOWN )
        p_k_prime.to_edge(LEFT_SIDE)
        self.play(Write(p_k_prime))
        self.wait(2)