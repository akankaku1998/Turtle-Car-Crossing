import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Score()

screen.listen()
screen.onkey(player.go_up,"space")

game_start = True
count = 0
while game_start:
    time.sleep(0.1)
    screen.update()

    count += 1
    if count == 6:
        car_manager.create()
        count = 0
    car_manager.move()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_start = False
            score.game_over()

    if player.ycor() > 280:
        player.start_again()
        car_manager.level_up()
        score.update_level()


screen.exitonclick()
