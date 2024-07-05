from manim import *
from PIL import Image
# class Pith(Scene):
#     def construct(self):

#         sq=Square(
#             side_length=3,stroke_color=GREEN,fill_opacity=0.75,fill_color=BLUE
#         )

#         self.play(Create(sq),run_time = 3)
#         self.wait() # 1 second default

class Testing(Scene):
    # CONFIG = { "camera_config":{"background_color": "#FFFFFF"}}
    def construct(self):
        self.camera.background_color = PURPLE_A
        
        # title
        title1 = Text("Concensus Capacity of",color=BLACK).shift(UP*0.8)
        title2 = Text("Noisy Broadcast",color=BLACK)
        title3 = Text("Channels",color=BLACK).shift(DOWN*0.8)
        sq=Rectangle(width=10,height=3,stroke_color = PURPLE_E)
        self.play(Create(sq),Write(title1),Write(title2),Write(title3), run_time=4)
        self.wait(5)
        # self.play(name.animate.shift(RIGHT*5),sq.animate.to_edge(UR))
        # self.play(name.animate.shift(UP*3))
        self.play(FadeOut(title1),FadeOut(title2),FadeOut(title3),FadeOut(sq))
        names1 = Text("Project by -",color=PURPLE_E).shift(UP*2)
        names2 = Text("Masumi Desai",color = WHITE).shift(UP*1)
        names3 = Text("&",color = WHITE)
        names4 = Text("Shravan Gadbail",color = WHITE).shift(DOWN*1)
        self.play(Create(names1),Write(names2),Write(names3),Write(names4),run_time = 0.2)
        sq2 = Square(side_length=3)
        self.play(Create(sq2))
        self.play(sq2.animate.shift(RIGHT))
        self.play(sq2.animate.scale(2))
        self.play(sq2.animate.rotate(PI / 2),runtime = 0.2)
        self.play(names1.animate.shift(RIGHT),names2.animate.shift(RIGHT),names3.animate.shift(RIGHT),names4.animate.shift(RIGHT),runtime=0.2)
        self.play(FadeOut(names1),FadeOut(names2),FadeOut(names3),FadeOut(names4),FadeOut(sq2),run_time=0.2)
        aim = Text("Main Aim",font_size=60,color=BLACK,weight = BOLD).shift(LEFT*4.3)
        arrow = Arrow(start=[-2.5,0,0],end=[-0.5,0,0],color=BLACK).shift(DOWN*0.1)
        toget = Text("To get",color = BLACK,font_size=55).shift(RIGHT*2.48).shift(UP*1.6).shift(RIGHT*0.45)
        noiseless = Text("Noiseless Broadcast",color = PURE_RED,font_size=55).shift(RIGHT*2.56).shift(UP*0.8).shift(RIGHT*0.45)
        From = Text("from",color = BLACK,font_size=55).shift(RIGHT*2.5).shift(RIGHT*0.45)
        Noisy = Text("Noisy Broadcast",color = BLACK,font_size=55).shift(DOWN*0.92).shift(RIGHT*2.7).shift(RIGHT*0.32)
        channel = Text("Channel",color = BLACK, font_size=55).shift(RIGHT*2.96).shift(DOWN*1.7)
        self.play(Create(aim),run_time= 0.6)
        self.play(Create(arrow))
        self.play(Write(toget),Write(noiseless),Write(From),Write(Noisy),Write(channel))

        self.play(FadeOut(aim),FadeOut(arrow),FadeOut(toget),FadeOut(noiseless),FadeOut(From),FadeOut(Noisy),FadeOut(channel))


class Intro(Scene):
    def construct(self):
        self.camera.background_color = PURPLE_A

        Intro_text=Text("INTRODUCTION",color=BLACK,font_size=60,weight = BOLD)
        re1=Rectangle(width=7,height=2.2,stroke_color=BLACK)
        self.play(Write(Intro_text))
        self.play(Create(re1))
        self.wait()
        self.play(FadeOut(Intro_text),FadeOut(re1))

        # BroadCast channel:

        Broad = Text("Broadcast Channel",color = BLACK,font_size = 43,weight = BOLD).shift(UP*2.9)
        Bu1 = Underline(mobject=Broad,stroke_color = BLACK)
        # P_{YZ|X}
        Function1 = Tex("$P_{YZ|X}$",color=BLACK,font_size=40)
        I1 = Tex("$x\epsilon\chi$",color = BLACK).shift(LEFT*3.3)
        O1 = Tex("$Y^{n}$",color=BLACK,font_size = 40).shift(UP).shift(RIGHT*2.2)
        O2 = Tex("$Z^{n}$",color = BLACK,font_size = 40).shift(DOWN).shift(RIGHT*2.2)
        F1B = Rectangle(width=2,height=1,color=BLACK)
        sender = Text("SENDER",color=DARK_BLUE).shift(LEFT)
        inar1 = Arrow(start=[-3,0,0],end=[-1,0,0],color = BLACK)
        outar1 = Arrow(start = [1,0,0],end = [2,1,0],color = BLACK)
        outar2 = Arrow(start = [1,0,0], end = [2,-1,0],color = BLACK)
        Rel1 = Tex("$(Y,Z) \sim P_{YZ|X}(y,z|x)$",color=BLACK).shift(DOWN*3)
        self.play(Create(Broad))
        self.play(Create(Bu1))
        self.play(Create(Function1),Create(F1B))
        self.play(Create(I1))
        self.play(Create(inar1))
        self.play(Create(outar1),Create(outar2))
        self.play(Create(O1),Create(O2))
        self.play(Create(Rel1))
        self.wait(5)
        self.wait(10)
        self.play(FadeOut(Broad),FadeOut(Bu1),FadeOut(Function1),FadeOut(F1B),FadeOut(I1),FadeOut(inar1),FadeOut(outar1),FadeOut(outar2),FadeOut(O1),FadeOut(O2),FadeOut(Rel1))
        # main problem to that the authors deal with 
        #mainprob = Text("The main problem that is being dealt with here:")
        Function2 = Tex("$P^{n}_{YZ|X}$",color=BLACK,font_size=40)
        I2 = Tex("$m\epsilon M$",color = BLACK).shift(LEFT*5.5)
        inar3 = Arrow(start=[-5.1,0,0],end=[-3.6,0,0],color = BLACK)
        SB = Square(side_length=1, stroke_color = GREEN_E, fill_opacity = 0.5, fill_color = GREEN_A).shift(LEFT*3.3)
        sender = Text("sender",font_size=30,color=BLACK).shift(DOWN*0.8).shift(LEFT*3.3)
        R1 = Tex("$Y^{n}$",color=BLACK,font_size = 40).shift(UP*0.84).shift(RIGHT*1.4)
        R2 = Tex("$Z^{n}$",color = BLACK,font_size = 40).shift(DOWN*0.84).shift(RIGHT*1.4)
        F2B = Rectangle(width=2,height=1,color=BLACK)
        inar2 = Arrow(start=[-3,0,0],end=[-0.7,0,0],color = BLACK)
        inarT = Tex("codeword$(m)$",font_size = 26,color=BLACK).shift(LEFT*1.97).shift(UP*0.3)
        outar3 = Arrow(start = [1,0,0],end = [2.5,1.5,0],color = BLACK)
        outar4 = Arrow(start = [1,0,0], end = [2.5,-1.5,0],color = BLACK)
        RB1 = Square(side_length=1, stroke_color = GREEN_E, fill_opacity = 0.5, fill_color = GREEN_A).shift(RIGHT*3.3).shift(UP*1.3)
        RB2 = Square(side_length=1, stroke_color = GREEN_E, fill_opacity = 0.5, fill_color = GREEN_A).shift(RIGHT*3.3).shift(DOWN*1.3)
        RBT1 = Text("Receiver 1",font_size=30,color=BLACK).shift(RIGHT*3.3).shift(UP*0.5)
        RBT2 = Text("Receiver 2",font_size=30,color=BLACK).shift(RIGHT*3.3).shift(DOWN*2.2)
        Rel2 = Tex("Want : $\hat{M}_{1} = \hat{M}_{2} = m$",color=BLACK).shift(DOWN*3)
        head = Text("Normal communication",color = BLACK, font_size = 55).shift(UP*3.1)
        self.play(Write(head))
        self.play(Create(I2))
        self.play(Create(inar3))
        self.play(Create(SB))
        self.play(Create(sender))
        self.play(Create(inar2),Write(inarT))
        self.play(Create(F2B),Write(Function2))
        self.play(Create(outar3),Create(outar4))
        self.play(Create(R1),Create(R2))
        self.play(Create(RB1),Create(RB2))
        self.play(Create(RBT1),Create(RBT2))
        self.play(Create(Rel2))
        self.wait(10)
        
        cross = Cross(scale_factor = 0.25,stroke_color = PURE_RED).shift(LEFT*1.95).shift(UP*0.3)
        inarTR = Tex("$x^{n}$",color = BLACK, font_size=35).shift(LEFT*1.95).shift(DOWN*0.3)
        head2 = Text("with consensus",font_size = 55, color = DARK_BLUE).shift(RIGHT*3.2).shift(UP*3.1)
        rel2T = Tex("Want : $\hat{M}_{1} = \hat{M}_{2} $",color=BLACK).shift(DOWN*3)
        self.play(head.animate.shift(LEFT*3), Create(head2),ReplacementTransform(Rel2,rel2T),Create(inarTR))
        self.add(cross)
        self.wait(17)
        self.play(FadeOut(I2),FadeOut(head2),FadeOut(head),FadeOut(inarTR),FadeOut(cross),FadeOut(inar3),FadeOut(SB),FadeOut(sender),FadeOut(inar2),FadeOut(inarT),FadeOut(outar3),FadeOut(outar4),FadeOut(R1),FadeOut(R2),FadeOut(RB1),FadeOut(RB2),FadeOut(RBT1),FadeOut(RBT2),FadeOut(rel2T),FadeOut(F2B),FadeOut(Function2))


        introTitle = Text("Byzantine General's Problem",color = BLACK, font_size=40,weight = BOLD).shift(UP*3)
        u1 = Underline(mobject=introTitle,stroke_color=BLACK, buff = 0.2)
        self.camera.background_color = WHITE
        # Byzantine General's problem
        self.wait(0.5)
        self.play(Create(introTitle),Create(u1),run_time = 1.5)
        self.wait(2)

        # Fort:

        re2=Rectangle(width=1.5,height=1,stroke_color=BLACK).shift(DOWN*0.7)
        fort=Text("Fort",color=RED).shift(DOWN*0.7)

        # Circles (representing commanders):

        c1=Circle(radius=0.5,color=BLACK).shift(DOWN*2.7).shift(RIGHT*2.8)
        c2=Circle(radius=0.5,color=BLACK).shift(DOWN*2.7).shift(LEFT*2.8)
        c3=Circle(radius=0.5,color=BLACK).shift(UP*1.3).shift(LEFT*2.8)
        c4=Circle(radius=0.5,color=BLACK).shift(UP*1.3).shift(RIGHT*2.8)

        # Commander General:
        G0 = Text("General",color=DARK_BLUE).shift(UP*1.8)
        Gc1 = Rectangle(color = BLACK,width = 2.7,height = 0.8).shift(UP*1.8)

        # Generals:

        G1=Text("L3",color=DARK_BLUE).shift(DOWN*2.7).shift(RIGHT*2.8)
        G2=Text("L4",color=DARK_BLUE).shift(DOWN*2.7).shift(LEFT*2.8)
        G3=Text("L1",color=DARK_BLUE).shift(UP*1.3).shift(LEFT*2.8)
        G4=Text("L2",color=DARK_BLUE).shift(UP*1.3).shift(RIGHT*2.8)

        # Arrows:

        ar1 = Arrow(start=[-2.5,-2.6,0],end=[-0.6,-1,0],color = DARK_BLUE)
        ar2 = Arrow(start=[2.5,1.2,0],end=[0.5,-0.3,0],color = DARK_BLUE)
        ar3 = Arrow(start=[-2.57,1.12,0],end=[-0.57,-0.3,0],color = DARK_BLUE)
        ar4 = Arrow(start=[2.5,-2.6,0],end=[0.6,-1,0],color = DARK_BLUE)

        # Execution:

        self.play(Create(re2),Write(fort))
        self.play(Create(G0),Create(Gc1))
        self.play(Create(c3),Create(c4),Create(c1),Create(c2))
        self.play(Create(G3),Create(G4),Create(G1),Create(G2))
        # self.play(Create(G4))
        # self.play(Create(G1))
        # self.play(Create(G2))
        self.play(Create(ar3),Create(ar2),Create(ar4),Create(ar1))
        self.wait(10)
        # self.play(Create(ar2))
        # self.play(Create(ar4))
        # self.play(Create(ar1))
        self.play(FadeOut(re2),FadeOut(fort),FadeOut(G0),FadeOut(Gc1),FadeOut(c3),FadeOut(c4),FadeOut(ar2),FadeOut(ar3),FadeOut(G2),FadeOut(G1),FadeOut(G4),FadeOut(G3),FadeOut(c2),FadeOut(c1),FadeOut(ar4),FadeOut(ar1))

        # Target/Favourable communication

        Target = Text("• Successful Communication",color=BLACK, font_size = 35).shift(LEFT*3.5).shift(UP*1.55)
        bull1 = Text("(i) If the commander is honest, all honest lieutenants agree on the\n commander's message.",font_size = 30,color=BLACK).shift(LEFT*0.5).shift(UP*0.25)
        bull2 = Text("(ii) All honest lieutenants agree on the same message even if the commander\n is malicious.",color = BLACK, font_size = 30).shift(RIGHT*0.45).shift(DOWN*1.25)

        self.play(Create(Target))
        self.play(Write(bull1))
        self.play(Write(bull2))
        self.wait(12)
        self.play(FadeOut(Target),FadeOut(bull1),FadeOut(bull2))

        # Setup:
        # setup = Text("Setup",color = BLACK, font_size = 48, weight = BOLD).shift(UP*2.9)
        self.play(FadeOut(introTitle),FadeOut(u1))
        self.wait(0.5)

class Setup(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        setup = Text("Setup",color = BLACK, font_size = 48, weight = BOLD).shift(UP*2.9)
        self.play(Create(setup))

        whatweneed = Text("What we need: ",color = BLACK,font_size = 37).shift(UP*1.8).shift(LEFT*4.5)
        first = Tex("• Memoryless Broadcast Channel with finite alphabets",color = DARK_BLUE,font_size=37).shift(UP).shift(LEFT*1.5)
        second = Tex("• $(2^{nR},n)$ consensus code: ",color = DARK_BLUE,font_size=37).shift(UP*0.5).shift(LEFT*3.92)
        sub21 = Tex("• Encoder $f: [1:(2^{nR},n)] -> x^{n}$",color = DARK_BLUE,font_size=37).shift(UP*0).shift(LEFT*3.28)
        sub22 = Tex("• Decoders     $g_{1}: y^{n} -> [1:(2^{nR},n)]$  and",color = DARK_BLUE,font_size=37).shift(DOWN*0.5).shift(LEFT*2.765) 
        sub23 = Tex("$g_{2}: \pounds^{n} -> [1:(2^{nR},n)]$",color = DARK_BLUE,font_size=37).shift(DOWN).shift(LEFT*2.2) 
        if1 = Tex("• If $x^{n}=f(m)$, Want : $\hat{M}_{1} = \hat{M}_{2} = m$",color=DARK_BLUE,font_size = 37).shift(DOWN*1.5).shift(LEFT*3.3)
        if2 = Tex("• If $x^{n} != f(m)$ for all m, Want : $\hat{M}_{1} = \hat{M}_{2}$",color = DARK_BLUE,font_size = 37).shift(DOWN*2).shift(LEFT*2.47)
        Pe = Tex("$P_{e}$ = max\{$max(\mathbb{P}[(\hat{M}_{1},\hat{M}_{2}) != (m,m)|f(m)]) , max(\mathbb{P}[\hat{M}_{1} != \hat{M}_{2}|x^{n}]) $\}",color = DARK_BLUE,font_size = 37).shift(DOWN*2.8)
        max1 = Tex("$m$",color = DARK_BLUE,font_size = 32).shift(DOWN*3.2).shift(LEFT*3.65)
        max2 = Tex("$x^{n}$",color = DARK_BLUE,font_size = 34).shift(DOWN*3.2).shift(RIGHT*2.37)
        self.wait(3)
        self.play(Write(whatweneed))
        
        self.wait(2)
        self.play(Write(first))
        self.wait()
        self.play(Write(second))
        self.wait()
        self.play(Write(sub21))
        self.wait(2)
        self.play(Write(sub22))
        
        self.play(Write(sub23))
        self.wait(2)
        self.wait(10)
        self.play(Write(if1))
        self.wait(22)
        self.play(Write(if2))
        self.wait(22)
        self.play(Write(Pe),Write(max1),Write(max2))
        self.wait()
        self.wait(44)
        self.play(FadeOut(Pe),FadeOut(setup),FadeOut(whatweneed),FadeOut(first),FadeOut(second),FadeOut(sub21),FadeOut(sub23),FadeOut(sub22),FadeOut(if1),FadeOut(if2),FadeOut(max1),FadeOut(max2))

class Ques(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # The authors using a case study of binary independent erasure broadcast channel prove that 
        # the byzantine capacity or the consensus capacity of the channel must be at least equal to
        # the common capacity of the channel
        # But it is to be noted that byzantine capacity is not equal to the common capacity

        i = Text("Some Important Questions : ",color = BLACK, font_size=50, weight = BOLD).shift(UP*3.5)
        Q1 = Text("Which broadcast channels allow communication with consensus?",font_size=37,color = BLACK).shift(UP*2)
        A1 = Tex("A Channel with common channel capacity equal to 0\n would have the byzantine or the consensus capacity 0 as well.\nSo, if $C_{p2p}(common_ch)>0$ then $C_{byz}>0$\n Channels with common channel capacity greater than 0\n would allow communication with consensus.",font_size=37,color = DARK_BLUE)
        self.play(Write(i))
        self.wait(6)
        self.play(Write(Q1))
        self.wait(6)
        self.play(Write(A1))
        self.wait(32)
        self.play(FadeOut(Q1),FadeOut(A1))
        Q2 = Text("What is the consensus capacity for such channels?",font_size=37,color = BLACK).shift(UP*2)
        A20 = Text("For a Binary Two-step Erasure Channel, ",font_size=33,color = DARK_BLUE).shift(UP)
        A21 = Tex("For $p=1$, $C_{byz}$ = 0",font_size=37,color = DARK_BLUE)
        A22 = Tex("For $p<1$, $C_{byz}$ = 1-$pq$ = $C_{common-msg}$",font_size=37,color = DARK_BLUE).shift(DOWN)
        A23 = Tex("$C_{byz}>0$ does not imply $C_{byz}=C_{common-msg}$ ",font_size=37,color = DARK_BLUE).shift(DOWN*2)
        self.play(Write(Q2))
        self.wait(7)
        self.play(Write(A20))
        self.play(Write(A21))
        self.play(Write(A22))
        self.wait(33)
        self.play(Write(A23))
        self.wait(8)
        self.play(FadeOut(A20),FadeOut(A21),FadeOut(A22),FadeOut(A23))
        Th = Tex("$C_{byz} = max\ min(I(U;Y),I(U;Z))$",font_size=60,color = DARK_BLUE)
        maxt = Tex("$P_{U}$",font_size=33,color = DARK_BLUE).shift(LEFT*1.98).shift(DOWN*0.38)
        self.play(Write(Th),Write(maxt))
        self.wait(17)
        self.play(FadeOut(Q2),FadeOut(i),FadeOut(Th),FadeOut(maxt))

class Thanks (Scene):
    def construct(self):
        self.camera.background_color = ORANGE
        Thank = Text("Thank", color = BLACK, font_size = 100, weight = BOLD).shift(UP*2).shift(LEFT*2)
        you = Text("You", color = BLACK, font_size = 100, weight = BOLD).shift(LEFT*0.5).shift(UP*0.3)
        circ = Circle(radius=1.7,color=BLACK).shift(LEFT*2.6).shift(UP*1.6)
        self.play(Write(Thank),Write(you))
        self.play(Create(circ))
        self.play(circ.animate.shift(RIGHT*2).shift(DOWN*2))
        self.wait(4)




class Main (Scene):
    def construct (self):
        Testing.construct(self)
        Intro.construct(self)
        Setup.construct(self)
        Ques.construct(self)
        Thanks.construct(self)