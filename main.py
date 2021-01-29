from manimlib.imports import *  

class Test(Scene):
    def construct(self):
        text = TextMobject("Bão")
        self.play(Write(text))
        self.wait()

