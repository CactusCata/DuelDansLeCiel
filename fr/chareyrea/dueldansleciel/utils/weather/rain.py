import entity
import libs.utils.screenProperties as screenProperties
from random import randint
import libs.cng as cng
import weather

class Rain(weather.Weather):

    def __init__(self, dropAmount):
        drops = []
        for i in range(dropAmount):
            drops.append(Drop())
        self.drops = drops

    def render(self):
        for drop in self.drops:
            drop.render()

    def tickUpdate(self):
        for drop in self.drops:
            drop.fall()

class Drop(entity.Entity):
    """
    Inspired from TheCodingTrain (https://www.youtube.com/watch?v=KkyIDI6rQJI)
    """

    def __init__(self):
        super().__init__(randint(0, screenProperties.getScreenWidth()), randint(screenProperties.getScreenWidth() + 50, screenProperties.getScreenWidth() + 500), 0)
        self.yspeed = randint(4, 20)
        self.lenght = randint(10, 40)

    def fall(self):
        self.setY(self.getY() - self.yspeed)
        self.yspeed = self.yspeed + 0.2

        if self.getY() < 0:
            self.setY(randint(screenProperties.getScreenWidth() + 50, screenProperties.getScreenWidth() + 500))
            self.yspeed = randint(4, 20)

    def render(self):
        cng.current_color((14, 1, 137))
        cng.line(self.getX(), self.getY(), self.getX(), self.getY() - self.lenght)
