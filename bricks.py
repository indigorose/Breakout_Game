from turtle import Turtle

"""First brick location brick.goto(-300, 350)
#Brick colours - #C25EBD, #F964A3, #FF7D85, #FFA46A, #FFCE5F
8x5 grid of bricks
"""

y_cords = [350, 350, 350, 350, 350, 350, 350, 350,
           310, 310, 310, 310, 310, 310, 310, 310,
           270, 270, 270, 270, 270, 270, 270, 270,
           230, 230, 230, 230, 230, 230, 230, 230,
           190, 190, 190, 190, 190, 190, 190, 190]

x_cords = [-280, -200, -120, -40, 40, 120, 200, 280,
           -280, -200, -120, -40, 40, 120, 200, 280,
           -280, -200, -120, -40, 40, 120, 200, 280,
           -280, -200, -120, -40, 40, 120, 200, 280,
           -280, -200, -120, -40, 40, 120, 200, 280
           ]
brick_color = ["#C25EBD", "#C25EBD", "#C25EBD", "#C25EBD", "#C25EBD", "#C25EBD", "#C25EBD", "#C25EBD",
               "#F964A3", "#F964A3", "#F964A3", "#F964A3", "#F964A3", "#F964A3", "#F964A3", "#F964A3",
               "#FF7D85", "#FF7D85", "#FF7D85", "#FF7D85", "#FF7D85", "#FF7D85", "#FF7D85", "#FF7D85",
               "#FFA46A", "#FFA46A", "#FFA46A", "#FFA46A", "#FFA46A", "#FFA46A", "#FFA46A", "#FFA46A",
               "#FFCE5F", "#FFCE5F", "#FFCE5F", "#FFCE5F", "#FFCE5F", "#FFCE5F", "#FFCE5F", "#FFCE5F",
               ]


class Bricks:

    def __init__(self):
        self.all_bricks = []

    def create_brick(self):
        for brick_index in range(0, 40):
            new_brick = Turtle(shape="square")
            new_brick.shapesize(stretch_wid=1, stretch_len=3)
            new_brick.color(brick_color[brick_index])
            new_brick.penup()
            new_brick.goto(x_cords[brick_index], y_cords[brick_index])
            self.all_bricks.append(new_brick)
