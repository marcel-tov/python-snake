import turtle

class Score:
    score = 0
    high_score = 0

    def __init__(self):
        self.hud = turtle.Turtle()
        self.hud.speed(0)
        self.hud.shape("square")
        self.hud.color("black")
        self.hud.penup()
        self.hud.hideturtle()
        self.hud.goto(0, 260)
        self.render()

    def render(self):
        self.hud.clear()
        self.hud.write(self.score_template(), align="center", font=("Courier", 24, "normal"))

    def increment_score(self):
        self.score += 1
        self.render()

    def score_template(self):
        if self.high_score > 0:
            return f"Score: {self.score} High score: {self.high_score}"

        return f"Score: {self.score}"

    def reset(self):
        self.high_score = self.score
        self.score = 0
        self.render()
