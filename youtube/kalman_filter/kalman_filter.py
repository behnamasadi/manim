from manimlib.imports import *
from sympy import *
from sympy.stats import Probability, Normal
from sympy import Integral

class Formula(Scene): 
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


        # X \sim \mathcal{N}(\mu_0,\,\sigma_{0}^{2})\ * X \sim \mathcal{N}(\mu_1,\,\sigma_{1}^{2})\

        # X \sim \mathcal{N}(\mu\prime,\,\sigma^{\prime2})\

        # \sigma^{\prime2}=\sigma_{0}^{2}-\frac{\sigma_{0}^{4}}{  \sigma_{0}^{2} +\sigma_{1}^{2}   }

        #\mu\prime=\mu0 +\frac{\sigma_{0}^{2}  (\mu1-\mu0))}{  \sigma_{0}^{2} +\sigma_{1}^{2}    }

        # K=\frac{\sigma_{0}^{2}}{  \sigma_{0}^{2} +\sigma_{1}^{2}   }

        # \sigma^{\prime2}=\sigma_{0}^{2}-K\sigma_{0}^{2}

        #\mu ^ {\prime2}=\sigma_{0} ^ {2} - K(\mu_1 -\mu_0)

        #A prime  A{}'

        # \lim_{\sigma_{0} \to +\infty}  K=\frac{\sigma_{0}^{2}}{  \sigma_{0}^{2} +\sigma_{1}^{2}   }

        # \lim_{\sigma_{0} \to 0}  K=\frac{\sigma_{0}^{2}}{  \sigma_{0}^{2} +\sigma_{1}^{2}   }

        # K=\Sigma_{0}(\Sigma_{0} +\Sigma_{0} )^{-1}

        # \mu\vec{}= \mu\vec{}_{0}+K(\mu\vec{}_{1} - \mu\vec{}_{0}  )

        # \Sigma{}'=\Sigma_{0}-K\Sigma_{0}

        #copytwoformula

        #p=1/2*at^2+v_{0}t
        #v=at+v_{0}
        
        
# X_{k}=
# \begin{bmatrix}
#  P_{k}
# \\ V_{k}
# \end{bmatrix}

#P_k=P_{k-1}+V_{k-1}\times t +\frac{1}{2}at^2
    #V_{k}=V_{k-1}+a\times t


# \^{X}_{k}=\begin{bmatrix}
# 1 & t\\
# 0 & 1
# \end{bmatrix} \times \^{X}_{k-1} +\begin{bmatrix}
# t^2\\
# t
# \end{bmatrix}*a
    
    #\^{X}_{k}=F*\^{X}_{k-1}+B\vec{U}

    #P_k=F_k P_{k-1}F^\mathsf{T}_{k}+Q_{k}

#correction
# \mu_{k}=H_{k} \^{X}_{k}    
#\Sigma_{k}=H_{} }
#\Sigma_{k}=H_{k}P_{k} H^\mathsf{T}_{k} +R_{k}      
    
#K^\prime=P_{k}H_{k}^\mathsf{T}(H_{k}P_{k}H_{k}^\mathsf{T}+R_{k} )^{-1}
#\^{X}^{'}_{k}=\^{X}_{k}+K^{'}(Z_k-H_{k}\^{X}_{k} )
#P^{'}_k=P_k-K^{'}H_{k}P_{k}

def Range(in_val,end_val,step=1):
    return list(np.arange(in_val,end_val+step,step))

class normals(GraphScene):
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




