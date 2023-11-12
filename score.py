import turtle

class Score:
    score = 0
    highScore = 0

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
        self.hud.write(self.scoreTemplate(), align="center", font=("Courier", 24, "normal"))

    def incrementScore(self):
        self.score += 1
        self.render()

    def scoreTemplate(self):
        if (self.highScore > 0):
            return "Score: %s  High score: %s" % (self.score, self.highScore)

        return "Score: %s" % (self.score)

    def reset(self):
        self.highScore = self.score
        self.score = 0
        self.render()

