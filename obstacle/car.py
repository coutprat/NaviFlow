import pyray as rl
class Car:
    def __init__(self,positions : list = [[0,0]],speed : int = 40,size : rl.Vector2 = rl.Vector2(20,40)):
        self.posList = positions
        self.pos = self.posList[0]
        self.speed = speed
        self.size = size
    def update(self):
        rl.draw_rectangle_pro(rl.Rectangle(self.pos[0],self.pos[1],self.size.x,self.size.y),)